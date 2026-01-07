from core.render_kernel.kernel import RenderKernel
_kernel = RenderKernel()
def render_headless(pipeline: str, passes: list):
    return _kernel.execute(pipeline, passes)
