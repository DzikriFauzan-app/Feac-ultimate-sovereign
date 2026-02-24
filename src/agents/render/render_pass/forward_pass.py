import numpy as np

class ForwardPass:
    def __init__(self, render_target=None):
        self.render_target = render_target

    def execute(self, backend, scene, camera):
        # Set the render target
        if self.render_target:
            backend.set_render_target(self.render_target)
        else:
            backend.set_render_target(None)

        # Clear the render target
        backend.clear_render_target()

        # Set the view and projection matrices
        view_matrix = camera.get_view_matrix()
        projection_matrix = camera.get_projection_matrix()
        backend.set_view_matrix(view_matrix)
        backend.set_projection_matrix(projection_matrix)

        # Render the scene
        for mesh in scene.meshes:
            material = mesh.material
            shader = material.shader

            # Bind the shader
            shader.bind(backend)

            # Set material properties
            material.bind_properties(backend)

            # Set model matrix
            backend.set_uniform_matrix4(shader.program, "model", mesh.model_matrix)

            # Bind the mesh
            mesh.bind(backend)

            # Draw the mesh
            mesh.draw(backend)
