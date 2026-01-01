import numpy as np

class Camera:
    def __init__(self, position, rotation, fov, aspect_ratio, near_clip, far_clip):
        self.position = position
        self.rotation = rotation
        self.fov = fov
        self.aspect_ratio = aspect_ratio
        self.near_clip = near_clip
        self.far_clip = far_clip

    def get_view_matrix(self):
        # Kode untuk menghitung view matrix
        pass

    def get_projection_matrix(self):
        # Kode untuk menghitung projection matrix
        pass
