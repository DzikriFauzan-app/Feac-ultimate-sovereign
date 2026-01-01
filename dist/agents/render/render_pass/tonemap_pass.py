#!/usr/bin/env python3
"""
ToneMappingPass (ACES-filmic approximation) - NeoEngine (FULL IMPLEMENTATION)

Fungsi:
  - Menerima input warna HDR float (dict / tuple / list) dari resources.
  - Menerapkan exposure (EV), white point scaling, lalu kurva filmic (Hable/ACES aprox).
  - Mengembalikan:
      * tone_mapped_float: {'r':..., 'g':..., 'b':...} (0.0..1.0)
      * tone_mapped_255: {'r':..., 'g':..., 'b':...} (0..255)
      * tonemap_meta: detail per-step untuk debugging dan pengujian.

Parameter yang didukung di resources (name keys):
  - 'final_color_float' (recommended, dict with r,g,b floats) OR
    fallback ke 'final_color' / 'lighting_color_float'
  - 'tonemap_config' optional:
      {
        "exposure": 1.0,        # linear multiplier before tone mapping
        "white": 11.2,         # white point (pre-scale); typical HDR white ~11.2
        "apply_saturation": True,
        "saturation": 1.0,
        "gamma": 2.2
      }

Referensi implementasi:
  - Common filmic fit: out = (x*(a*x + b)) / (x*(c*x + d) + e)  with a=2.51,b=0.03,c=2.43,d=0.59,e=0.14
  - This is a widely used ACES-like approximation (John Hable / Uncharted2 fit).
"""

import math
import time
from typing import Dict, Any, Tuple

# Filmic fit parameters (Hable / Uncharted2 style) — empirically chosen
_A = 2.51
_B = 0.03
_C = 2.43
_D = 0.59
_E = 0.14

class ToneMappingPass:
    def __init__(self):
        self.name = "ToneMappingPass"

    # -------------------------
    # Helpers
    # -------------------------
    def _to_rgb_tuple(self, val: Any) -> Tuple[float, float, float]:
        """
        Normalize input variations to (r,g,b) floats.
        Accepts dict with keys r,g,b or list/tuple of 3 floats or single float (grayscale).
        """
        if val is None:
            return (0.0, 0.0, 0.0)
        if isinstance(val, dict):
            return (float(val.get("r", 0.0)), float(val.get("g", 0.0)), float(val.get("b", 0.0)))
        if isinstance(val, (list, tuple)) and len(val) >= 3:
            return (float(val[0]), float(val[1]), float(val[2]))
        # single numeric
        try:
            f = float(val)
            return (f, f, f)
        except Exception:
            return (0.0, 0.0, 0.0)

    def _clamp01(self, x: float) -> float:
        if x != x:
            return 0.0
        if x < 0.0:
            return 0.0
        if x > 1.0:
            return 1.0
        return x

    def _apply_filmic(self, x: float) -> float:
        """
        Apply filmic curve (approximation).
        x is assumed non-negative (linear HDR).
        Returns tone-mapped value in 0..1 (before gamma).
        Formula: (x*(A*x + B)) / (x*(C*x + D) + E)
        """
        num = x * (_A * x + _B)
        den = x * (_C * x + _D) + _E
        if den == 0:
            return 0.0
        return num / den

    def _saturate(self, rgb: Tuple[float,float,float], sat: float) -> Tuple[float,float,float]:
        """
        Simple saturation around luminance: lerp(luminance, color, sat)
        Uses Rec.709 luma weights.
        """
        r, g, b = rgb
        lum = 0.2126*r + 0.7152*g + 0.0722*b
        return (
            lum + (r - lum) * sat,
            lum + (g - lum) * sat,
            lum + (b - lum) * sat
        )

    # -------------------------
    # Main run
    # -------------------------
    def run(self, camera, resources: Dict[str, Any]):
        """
        Execute tone mapping pass.
        Returns dict to be merged into resources.
        """
        # 1) read input color (HDR linear)
        hdr = None
        for key in ("final_color_float", "final_color", "lighting_color_float", "lighting_color"):
            if key in resources:
                hdr = resources[key]
                break

        rgb_in = self._to_rgb_tuple(hdr)

        # 2) config
        cfg = resources.get("tonemap_config", {})
        exposure = float(cfg.get("exposure", 1.0))
        white = float(cfg.get("white", 11.2))          # typical "white" range for HDR scenes
        apply_saturation = bool(cfg.get("apply_saturation", True))
        saturation = float(cfg.get("saturation", 1.0))
        gamma = float(cfg.get("gamma", 2.2))

        # 3) pre-scale: apply exposure and white balance scale
        # We do simple exposure (linear) then normalize by white point so white maps to 1 before filmic curve
        pre_scaled = (
            rgb_in[0] * exposure / (white if white != 0 else 1.0),
            rgb_in[1] * exposure / (white if white != 0 else 1.0),
            rgb_in[2] * exposure / (white if white != 0 else 1.0)
        )

        # 4) apply filmic curve per channel
        mapped = (
            self._apply_filmic(pre_scaled[0]),
            self._apply_filmic(pre_scaled[1]),
            self._apply_filmic(pre_scaled[2])
        )

        # 5) optional saturation adjustment in LCH-ish simple method
        if apply_saturation and abs(saturation - 1.0) > 1e-6:
            mapped = self._saturate(mapped, saturation)

        # 6) gamma correction (sRGB-like) — convert linear to sRGB/gamma
        def apply_gamma(v: float) -> float:
            if v <= 0.0:
                return 0.0
            return pow(v, 1.0 / gamma)

        mapped_gamma = ( apply_gamma(mapped[0]), apply_gamma(mapped[1]), apply_gamma(mapped[2]) )

        # 7) clamp to 0..1 and prepare outputs
        mapped_clamped = ( self._clamp01(mapped_gamma[0]), self._clamp01(mapped_gamma[1]), self._clamp01(mapped_gamma[2]) )

        tone_mapped_float = {"r": round(mapped_clamped[0], 6), "g": round(mapped_clamped[1], 6), "b": round(mapped_clamped[2], 6)}
        tone_mapped_255 = {"r": int(tone_mapped_float["r"] * 255), "g": int(tone_mapped_float["g"] * 255), "b": int(tone_mapped_float["b"] * 255)}

        meta = {
            "input_hdr": {"r": rgb_in[0], "g": rgb_in[1], "b": rgb_in[2]},
            "pre_scaled": {"r": pre_scaled[0], "g": pre_scaled[1], "b": pre_scaled[2]},
            "mapped_linear": {"r": mapped[0], "g": mapped[1], "b": mapped[2]},
            "mapped_gamma": {"r": mapped_gamma[0], "g": mapped_gamma[1], "b": mapped_gamma[2]},
            "params": {
                "exposure": exposure,
                "white": white,
                "saturation": saturation,
                "apply_saturation": apply_saturation,
                "gamma": gamma,
                "film_params": {"A": _A, "B": _B, "C": _C, "D": _D, "E": _E}
            },
            "computed_at": time.time()
        }

        return {
            "tone_mapped_float": tone_mapped_float,
            "tone_mapped_255": tone_mapped_255,
            "tonemap_meta": meta
        }

# end file
