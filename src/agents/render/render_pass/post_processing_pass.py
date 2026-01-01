#!/usr/bin/env python3
"""
================================================================================
PostProcessingPass – NeoEngine (FULL)
================================================================================
Fungsi:
- Menerapkan tahap post-processing pada final lighting buffer:
  bloom (approx), contrast, saturation, vignette, exposure fine-tune.

Desain:
- Semua efek dijalankan di CPU ALGORITMIS agar engine tetap kompatibel
  di Termux / Android low-end.
- Struktur output selalu JSON-friendly untuk debugging pipeline.

Input yang dibutuhkan pada resources:
  - lighting_color_float {r,g,b}
  - lighting_meta (optional)
  - config post-processing dapat dikirim lewat resources["post_config"]

Output:
  - final_color_float
  - final_color_255
  - post_meta
================================================================================
"""

import math
import time
from typing import Dict, Any


class PostProcessingPass:
    def __init__(self):
        self.name = "PostProcessingPass"

    # ----------------------------------------------------------------------
    # Helper vector ops
    # ----------------------------------------------------------------------
    def _clamp(self, x: float, lo: float = 0.0, hi: float = 1.0) -> float:
        return max(lo, min(hi, x))

    def _vec(self, col):
        return (col["r"], col["g"], col["b"])

    def _vec_add(self, a, b):
        return (a[0] + b[0], a[1] + b[1], a[2] + b[2])

    def _vec_mul(self, a, s):
        return (a[0] * s, a[1] * s, a[2] * s)

    def _vec_mul_elem(self, a, b):
        return (a[0]*b[0], a[1]*b[1], a[2]*b[2])

    # ----------------------------------------------------------------------
    # Post-processing effects
    # ----------------------------------------------------------------------
    def _bloom(self, col, strength):
        """
        Bloom Approximation (non-convolution):
        - Ambil warna bright spot (threshold 0.7)
        - Boost warna terang
        - Tidak menggunakan kernel blur karena CPU-friendly
        """
        r, g, b = col
        intensity = max(r, g, b)
        if intensity < 0.7:
            return col  # tidak ada bloom
        bloom_factor = strength * (intensity - 0.7)
        bloom_color = (bloom_factor, bloom_factor, bloom_factor)
        return self._vec_add(col, bloom_color)

    def _apply_contrast(self, col, k):
        """
        Contrast correction: (c - 0.5)*k + 0.5
        """
        r = (col[0] - 0.5) * k + 0.5
        g = (col[1] - 0.5) * k + 0.5
        b = (col[2] - 0.5) * k + 0.5
        return (self._clamp(r), self._clamp(g), self._clamp(b))

    def _apply_saturation(self, col, k):
        """
        Saturation: 
        mix(gray, color, k)
        """
        gray = 0.2126 * col[0] + 0.7152 * col[1] + 0.0722 * col[2]
        r = gray * (1 - k) + col[0] * k
        g = gray * (1 - k) + col[1] * k
        b = gray * (1 - k) + col[2] * k
        return (self._clamp(r), self._clamp(g), self._clamp(b))

    def _vignette(self, col, strength):
        """
        Vignette Approximation (no screen coords):
        - Hanya menurunkan brightness global agar efek mudah di-debug.
        - Pada implementasi GPU nanti baru pakai distance-based calc.
        """
        factor = 1.0 - strength * 0.1
        return (self._clamp(col[0] * factor),
                self._clamp(col[1] * factor),
                self._clamp(col[2] * factor))

    # ----------------------------------------------------------------------
    # Main run
    # ----------------------------------------------------------------------
    def run(self, camera, resources: Dict[str, Any]) -> Dict[str, Any]:

        base_col = resources.get("lighting_color_float", {"r": 0.3, "g": 0.3, "b": 0.3})
        r, g, b = base_col.get("r", 0.3), base_col.get("g", 0.3), base_col.get("b", 0.3)
        col = (float(r), float(g), float(b))

        cfg = resources.get("post_config", {})

        bloom_strength = cfg.get("bloom", 0.0)
        contrast = cfg.get("contrast", 1.0)
        saturation = cfg.get("saturation", 1.0)
        vignette_strength = cfg.get("vignette", 0.0)
        exposure_fine = cfg.get("exposure", 1.0)

        # Run effects in order
        if bloom_strength > 0:
            col = self._bloom(col, bloom_strength)

        if contrast != 1.0:
            col = self._apply_contrast(col, contrast)

        if saturation != 1.0:
            col = self._apply_saturation(col, saturation)

        if vignette_strength > 0:
            col = self._vignette(col, vignette_strength)

        # exposure refinement (small)
        col = (self._clamp(col[0] * exposure_fine),
               self._clamp(col[1] * exposure_fine),
               self._clamp(col[2] * exposure_fine))

        # Output 0..1 and 0..255
        col_float = {"r": round(col[0], 6),
                     "g": round(col[1], 6),
                     "b": round(col[2], 6)}

        col_255 = {"r": int(col[0] * 255),
                   "g": int(col[1] * 255),
                   "b": int(col[2] * 255)}

        meta = {
            "bloom_strength": bloom_strength,
            "contrast": contrast,
            "saturation": saturation,
            "vignette_strength": vignette_strength,
            "exposure": exposure_fine,
            "computed_at": time.time()
        }

        return {
            "post_color_float": col_float,
            "post_color_255": col_255,
            "post_meta": meta
        }

# End file
