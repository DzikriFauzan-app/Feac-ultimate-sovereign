#!/usr/bin/env python3
"""
================================================================================
FinalCompositePass – NeoEngine (FULL VERSION)
================================================================================
Tugas:
  - Menggabungkan lighting + bloom + postprocess
  - Mengaplikasikan exposure
  - Menyiapkan buffer final untuk tahap tonemapping (ACES) berikutnya
  - Menghasilkan output final untuk pipeline (float & rgb8)

Input yang digunakan dari resources:
  lighting_color_float
  bloom_color_float
  postprocess_color_float
  exposure_config

Output:
  final_color_float
  final_color_255
  final_meta
================================================================================
"""

import time
from typing import Dict


class FinalCompositePass:
    def __init__(self):
        self.name = "FinalCompositePass"

    # --------------------------------------------------------------
    # Util
    # --------------------------------------------------------------
    def _clamp(self, x, lo=0.0, hi=1.0):
        return max(lo, min(hi, x))

    def _add(self, a, b):
        return (a[0] + b[0], a[1] + b[1], a[2] + b[2])

    def _mul(self, a, s):
        return (a[0] * s, a[1] * s, a[2] * s)

    # --------------------------------------------------------------
    # Run
    # --------------------------------------------------------------
    def run(self, camera, res: Dict):

        # Base lighting
        light = res.get("lighting_color_float", {"r": 0.6, "g": 0.6, "b": 0.6})
        L = (float(light["r"]), float(light["g"]), float(light["b"]))

        # Bloom
        bloom = res.get("bloom_color_float", {"r": 0.0, "g": 0.0, "b": 0.0})
        B = (float(bloom["r"]), float(bloom["g"]), float(bloom["b"]))

        # Post-process
        post = res.get("postprocess_color_float", None)
        if post:
            P = (float(post["r"]), float(post["g"]), float(post["b"]))
        else:
            P = None

        # Exposure
        e_cfg = res.get("exposure_config", {"exposure": 1.0})
        exposure = float(e_cfg.get("exposure", 1.0))

        # ----------------------------------------------------------
        # Composite
        # ----------------------------------------------------------
        # base = lighting + bloom
        base = self._add(L, B)

        # if post-process exists → apply
        if P:
            base = self._add(base, P)

        # apply exposure
        base = self._mul(base, exposure)

        # clamp
        final = (
            self._clamp(base[0]),
            self._clamp(base[1]),
            self._clamp(base[2]),
        )

        final_float = {
            "r": round(final[0], 6),
            "g": round(final[1], 6),
            "b": round(final[2], 6),
        }

        final_255 = {
            "r": int(final_float["r"] * 255),
            "g": int(final_float["g"] * 255),
            "b": int(final_float["b"] * 255),
        }

        meta = {
            "lighting": L,
            "bloom": B,
            "post": P,
            "exposure": exposure,
            "final_before_clamp": base,
            "computed_at": time.time(),
        }

        return {
            "final_color_float": final_float,
            "final_color_255": final_255,
            "final_meta": meta,
        }

# end file
