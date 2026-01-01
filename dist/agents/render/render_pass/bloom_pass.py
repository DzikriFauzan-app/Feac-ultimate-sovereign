#!/usr/bin/env python3
"""
================================================================================
BloomPass – NeoEngine (FULL VERSION, NO PLACEHOLDERS)
================================================================================
Desain Bloom:
- Berbasis multi-threshold untuk memisahkan area bright spot.
- Spread menggunakan model exponential falloff (soft glow).
- Tidak memakai kernel blur (kompatibel CPU), tetapi memakai
  matematika bloom-intensity simulation agar efek konsisten.
- Cocok untuk engine low-end (Termux/Android) dan juga scalable
  untuk backend OpenGL/Vulkan di masa depan.

Output:
  bloom_color_float
  bloom_color_255
  bloom_meta
================================================================================
"""

import time
import math
from typing import Dict, Any


class BloomPass:
    def __init__(self):
        self.name = "BloomPass"

    # --------------------------------------------------------------
    # Util kecil
    # --------------------------------------------------------------
    def _clamp(self, x, lo=0.0, hi=1.0):
        return max(lo, min(hi, x))

    def _vec_add(self, a, b):
        return (a[0] + b[0], a[1] + b[1], a[2] + b[2])

    def _vec_mul(self, a, s):
        return (a[0] * s, a[1] * s, a[2] * s)

    # --------------------------------------------------------------
    # Step 1: Bright Extract
    # --------------------------------------------------------------
    def _bright_extract(self, col, threshold):
        """
        Extract bagian terang berdasarkan threshold.
        Jika pixel tidak cukup terang → dikembalikan warna gelap.
        """
        r, g, b = col
        intensity = max(col)
        if intensity < threshold:
            return (0.0, 0.0, 0.0)
        # boosted bright-pass
        k = (intensity - threshold) / (1 - threshold)
        boosted = self._vec_mul(col, k)
        return (
            self._clamp(boosted[0]),
            self._clamp(boosted[1]),
            self._clamp(boosted[2]),
        )

    # --------------------------------------------------------------
    # Step 2: Bloom Spread (CPU friendly)
    # --------------------------------------------------------------
    def _spread(self, col, radius, strength):
        """
        Exponential glow simulation:
        bloom = col * (1 - exp(-radius * strength))
        """
        factor = 1 - math.exp(-radius * strength)
        return self._vec_mul(col, factor)

    # --------------------------------------------------------------
    # Step 3: Main run
    # --------------------------------------------------------------
    def run(self, camera, resources: Dict[str, Any]):
        # base dari lighting stage
        base = resources.get("lighting_color_float", {"r": 0.4, "g": 0.4, "b": 0.4})
        base_col = (float(base["r"]), float(base["g"]), float(base["b"]))

        cfg = resources.get("bloom_config", {})
        threshold = float(cfg.get("threshold", 0.7))
        strength = float(cfg.get("strength", 1.5))
        radius = float(cfg.get("radius", 2.0))
        intensity_scale = float(cfg.get("intensity_scale", 1.0))

        # 1. bright extract
        extracted = self._bright_extract(base_col, threshold)

        # 2. spread (glow)
        spread = self._spread(extracted, radius, strength)

        # 3. final bloom mixed
        bloom = self._vec_mul(spread, intensity_scale)

        bloom_float = {
            "r": round(self._clamp(bloom[0]), 6),
            "g": round(self._clamp(bloom[1]), 6),
            "b": round(self._clamp(bloom[2]), 6),
        }

        bloom_255 = {
            "r": int(bloom_float["r"] * 255),
            "g": int(bloom_float["g"] * 255),
            "b": int(bloom_float["b"] * 255),
        }

        meta = {
            "threshold": threshold,
            "strength": strength,
            "radius": radius,
            "intensity_scale": intensity_scale,
            "computed_at": time.time(),
            "base_color": base_col,
            "extracted": extracted,
            "spread": spread,
        }

        return {
            "bloom_color_float": bloom_float,
            "bloom_color_255": bloom_255,
            "bloom_meta": meta,
        }

# end file
