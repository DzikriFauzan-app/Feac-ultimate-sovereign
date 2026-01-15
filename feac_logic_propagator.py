import sys
import os

sys.path.insert(0, os.path.expanduser("~/neo_internal"))
from core.world_registry import WorldRegistry

# Inisialisasi Dunia
WorldRegistry.register_region("Forest_B", "forest")
WorldRegistry.register_region("City_A", "city")

# Memicu Krisis
print("📉 [FEAC] Memicu kegagalan produksi di Forest_B...")
WorldRegistry.update_status("Forest_B", "CRISIS")

print("⚠️ [FEAC] Menganalisis dampak kedaulatan...")
WorldRegistry.update_status("City_A", "THREATENED")

print("🏁 [FEAC] Propagasi Selesai & Data Tersimpan.")
