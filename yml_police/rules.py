def run_hard_rules(cfg):
    errors = []

    py = str(cfg.get("python", ""))
    if py.startswith("3.11") or py.startswith("3.12"):
        errors.append("Python >=3.11 TIDAK didukung buildozer stabil")

    api = int(cfg.get("android.api", 0))
    if api and api < 30:
        errors.append("android.api < 30 → gagal dependency modern")

    reqs = cfg.get("requirements", "")
    if isinstance(reqs, str) and "numpy>=2" in reqs:
        errors.append("numpy>=2.x known-break di python-for-android")

    if "android.permissions" in cfg:
        perms = cfg["android.permissions"]
        if "SYSTEM_ALERT_WINDOW" in perms:
            errors.append("SYSTEM_ALERT_WINDOW memicu Play Store rejection")

    return errors
