class RenderCommand:
    def __init__(self, mesh, material, transform):
        self.mesh = mesh
        self.material = material
        self.transform = transform
    def execute(self, backend, camera):
        # Set the transform matrix
        backend.set_transform_matrix(self.transform)
        # Bind the material
        self.material.bind(backend)
        # Bind the mesh
        self.mesh.bind(backend)
        # Draw the mesh
        self.mesh.draw(backend)
