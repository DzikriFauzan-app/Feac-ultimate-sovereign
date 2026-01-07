PATH = "/data/data/org.feac.ultimate.feac_sovereign/files/NeoEngine/agents/RenderAgent.py"

with open(PATH, "r") as f:
    lines = f.readlines()

out = []
inserted_import = False
inserted_init = False
patched_render = False

for line in lines:
    # Inject import RenderManager
    if not inserted_import and line.startswith("from"):
        out.append(line)
        if "render.render_manager" not in "".join(lines):
            out.append("from render.render_manager import RenderManager\n")
        inserted_import = True
        continue

    # Inject RenderManager init
    if "def __init__" in line and not inserted_init:
        out.append(line)
        out.append("        self.render_manager = RenderManager()\n")
        inserted_init = True
        continue

    # Patch render command
    if "async def _cmd_render_scene" in line and not patched_render:
        out.append(line)
        out.append("""
        # ==== NEOENGINE NATIVE RENDER (FINAL OWNER) ====
        try:
            result = self.render_manager.render(
                scene=self.scene,
                pipeline=self.pipeline
            )

            await self.emit_result(tid, {
                "status": "RENDER_OK",
                "engine": "NeoEngineNative",
                "scene": self.scene.name if self.scene else "none",
                "pipeline": self.pipeline.name if self.pipeline else "default",
                "output": result
            })
        except Exception as e:
            await self.emit_error(tid, str(e))
        return
        # =============================================
""")
        patched_render = True
        continue

    out.append(line)

with open(PATH, "w") as f:
    f.writelines(out)

print("✅ PATCH FINAL APPLIED: RenderAgent now uses NeoEngine Native Render")
