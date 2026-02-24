def run_heuristics(cfg):
    score = 0
    notes = []

    if "android.ndk" in cfg:
        score += 20
        notes.append("NDK custom sering konflik di Termux")

    if "gradle_dependencies" in cfg:
        score += 15
        notes.append("Gradle manual dependency → rawan clash")

    if "source.include_exts" in cfg:
        exts = cfg["source.include_exts"]
        if "pyx" in exts:
            score += 20
            notes.append("Cython tanpa toolchain → gagal build")

    if cfg.get("android.arch") not in ("arm64-v8a", None):
        score += 25
        notes.append("Non-arm64 di Termux sering gagal")

    return score, notes
