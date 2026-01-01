PATH = "/sdcard/Buku saya/Fauzan engine/NeoEngine/agents/RenderAgent.py"

with open(PATH, "r") as f:
    lines = f.readlines()

out = []
inside = False

for line in lines:
    if line.strip().startswith("async def _cmd_render_scene"):
        inside = True
        out.append(line)
        out.append("""
        # === NEOENGINE FORCED RENDER EXECUTION ===
        if not self.scene:
            await self.emit_error(tid, "No scene loaded")
            return

        try:
            self.renderer.render(self.scene)

            result = {
                "status": "RENDER_OK",
                "engine": "NeoEngine",
                "pipeline": getattr(self, "pipeline_name", "unknown"),
                "scene": self.scene.name,
                "renderables": len(self.scene.get_renderables()),
                "lights": len(self.scene.get_lights()),
                "output": "memory"
            }

            await self.emit_result(tid, result)

        except Exception as e:
            await self.emit_error(tid, str(e))
        return
        # ========================================
""")
        continue

    if inside:
        # Skip old function body
        if line.startswith("async def") or line.startswith("    def"):
            inside = False
            out.append(line)
        else:
            continue
    else:
        out.append(line)

with open(PATH, "w") as f:
    f.writelines(out)

print("PATCH APPLIED: _cmd_render_scene fully replaced with emit-based render")
