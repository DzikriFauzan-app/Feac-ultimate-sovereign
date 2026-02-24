from render.render_pipeline import RenderPipeline
from render.render_context import RenderContext
from core.scene import Scene

# Create scene
scene = Scene("VALIDATION_SCENE")

# Create render context
context = RenderContext()

# Bind scene to context (INI KUNCI)
if hasattr(context, "set_scene"):
    context.set_scene(scene)
else:
    context.scene = scene

# Create pipeline (WAJIB name + config)
pipeline = RenderPipeline(
    name="deferred_pbr",
    config={
        "passes": ["gbuffer", "lighting", "post"]
    }
)

# Bind context to pipeline
if hasattr(pipeline, "bind_context"):
    pipeline.bind_context(context)
else:
    pipeline.context = context

# Execute pipeline
pipeline.prepare()
pipeline.execute()

print("RENDER VALIDATION RESULT:")
print("Pipeline executed successfully")
print("Scene bound to context:", context.scene.name)
