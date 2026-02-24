class RenderState:
    def __init__(self):
        self.depth_test = True
        self.blend = False
        self.cull_face = True
    def set_depth_test(self, enabled):
        self.depth_test = enabled
    def set_blend(self, enabled):
        self.blend = enabled
    def set_cull_face(self, enabled):
        self.cull_face = enabled
    def apply(self, backend):
        if self.depth_test:
            backend.enable_depth_test()
        else:
            backend.disable_depth_test()
        if self.blend:
            backend.enable_blend()
        else:
            backend.disable_blend()
        if self.cull_face:
            backend.enable_cull_face()
        else:
            backend.disable_cull_face()
