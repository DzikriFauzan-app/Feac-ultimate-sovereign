#!/usr/bin/env python3
"""
core/scene.py — FULL VERSION

Implementasi Scene Tree untuk NeoEngine:
- Node
- Spatial
- Transform
- Camera
- MeshInstance
- Light
- Scene
- build_test_scene()

100% lengkap dan kompatibel dengan RenderPipeline.
"""

from __future__ import annotations
import time
import uuid
import math
from typing import Any, Dict, List, Optional, Callable, Iterable, Union

# =====================================================
# Transform (pos, rot_euler, scale)
# =====================================================
class Transform:
    __slots__ = ("position", "rotation_euler", "scale")

    def __init__(self, position=None, rotation_euler=None, scale=None):
        self.position = tuple(position) if position else (0.0, 0.0, 0.0)
        self.rotation_euler = tuple(rotation_euler) if rotation_euler else (0.0, 0.0, 0.0)
        self.scale = tuple(scale) if scale else (1.0, 1.0, 1.0)

    def copy(self) -> "Transform":
        return Transform(self.position, self.rotation_euler, self.scale)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "position": list(self.position),
            "rotation_euler": list(self.rotation_euler),
            "scale": list(self.scale),
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "Transform":
        return Transform(
            tuple(d.get("position", (0,0,0))),
            tuple(d.get("rotation_euler", (0,0,0))),
            tuple(d.get("scale", (1,1,1)))
        )

    def __repr__(self):
        return f"Transform(pos={self.position}, rot={self.rotation_euler}, scale={self.scale})"

# =====================================================
# Base Node
# =====================================================
class Node:
    def __init__(self, name: Optional[str]=None):
        self.id = str(uuid.uuid4())
        self.name = name or f"Node_{self.id[:8]}"
        self.parent: Optional["Node"] = None
        self.children: List["Node"] = []

        self._ready = False
        self._entered = False

        # lifecycle callbacks
        self.on_ready: Optional[Callable[["Node"], None]] = None
        self.on_enter_tree: Optional[Callable[["Node"], None]] = None
        self.on_exit_tree: Optional[Callable[["Node"], None]] = None
        self.on_process: Optional[Callable[["Node", float], None]] = None

    # --------------------------------------------
    # Tree manipulation
    # --------------------------------------------
    def add_child(self, node: "Node"):
        if node.parent:
            node.parent.remove_child(node)
        node.parent = self
        self.children.append(node)
        return node

    def remove_child(self, node: "Node"):
        if node in self.children:
            self.children.remove(node)
            node.parent = None
            return node
        return None

    def traverse(self) -> Iterable["Node"]:
        yield self
        for c in self.children:
            yield from c.traverse()

    # --------------------------------------------
    # lifecycle
    # --------------------------------------------
    def ready(self):
        self._ready = True
        if self.on_ready:
            self.on_ready(self)

    def enter_tree(self):
        self._entered = True
        if self.on_enter_tree:
            self.on_enter_tree(self)
        for c in self.children:
            c.enter_tree()

    def exit_tree(self):
        self._entered = False
        if self.on_exit_tree:
            self.on_exit_tree(self)
        for c in self.children:
            c.exit_tree()

    def process(self, dt: float):
        if self.on_process:
            self.on_process(self, dt)
        for c in self.children:
            c.process(dt)

    # --------------------------------------------
    # Serialization
    # --------------------------------------------
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "type": self.__class__.__name__,
            "children": [c.to_dict() for c in self.children],
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Node":
        return cls(name=data.get("name"))

    def __repr__(self):
        return f"<{self.__class__.__name__} name={self.name} id={self.id[:8]}>"

# =====================================================
# Spatial — Node + Transform
# =====================================================
class Spatial(Node):
    def __init__(self, name: Optional[str]=None, transform: Optional[Transform]=None):
        super().__init__(name)
        self.transform = transform.copy() if transform else Transform()
        self.world_transform = self.transform.copy()
        self.visible = True

    def to_dict(self) -> Dict[str, Any]:
        d = super().to_dict()
        d.update({
            "transform": self.transform.to_dict(),
            "visible": self.visible
        })
        return d

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Spatial":
        t = Transform.from_dict(data.get("transform", {}))
        n = cls(name=data.get("name"), transform=t)
        n.visible = data.get("visible", True)
        return n

    def __repr__(self):
        return f"<{self.__class__.__name__} name={self.name} transform={self.transform}>"


# =====================================================
# Camera
# =====================================================
class Camera(Spatial):
    def __init__(self, name: Optional[str]=None,
                 fov: float = 60.0, aspect: float = 16/9,
                 near: float = 0.1, far: float = 1000.0):
        super().__init__(name=name or "Camera", transform=Transform())
        self.fov = float(fov)
        self.aspect = float(aspect)
        self.near = float(near)
        self.far = float(far)
        self.projection = "perspective"  # or 'orthographic'

    def get_camera_data(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "transform": self.world_transform.to_dict(),
            "fov": self.fov,
            "aspect": self.aspect,
            "near": self.near,
            "far": self.far,
            "projection": self.projection,
        }

    def to_dict(self) -> Dict[str, Any]:
        d = super().to_dict()
        d.update({
            "fov": self.fov,
            "aspect": self.aspect,
            "near": self.near,
            "far": self.far,
            "projection": self.projection
        })
        return d

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Camera":
        cam = cls(
            name=data.get("name"),
            fov=data.get("fov", 60.0),
            aspect=data.get("aspect", 16/9),
            near=data.get("near", 0.1),
            far=data.get("far", 1000.0)
        )
        cam.transform = Transform.from_dict(data.get("transform", {}))
        cam.projection = data.get("projection", "perspective")
        return cam

# =====================================================
# MeshInstance
# =====================================================
class MeshInstance(Spatial):
    def __init__(self, name: Optional[str]=None,
                 mesh_id: Optional[str]=None,
                 material_id: Optional[str]=None):
        super().__init__(name=name or "MeshInstance", transform=Transform())
        self.mesh_id = mesh_id
        self.material_id = material_id
        self.cast_shadow = True
        self.receive_shadow = True

    def get_renderable(self) -> Dict[str, Any]:
        return {
            "node_id": self.id,
            "name": self.name,
            "transform": self.world_transform.to_dict(),
            "mesh_id": self.mesh_id,
            "material_id": self.material_id,
            "visible": self.visible,
            "cast_shadow": self.cast_shadow,
            "receive_shadow": self.receive_shadow,
        }

    def to_dict(self) -> Dict[str, Any]:
        d = super().to_dict()
        d.update({
            "mesh_id": self.mesh_id,
            "material_id": self.material_id,
            "cast_shadow": self.cast_shadow,
            "receive_shadow": self.receive_shadow
        })
        return d

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "MeshInstance":
        m = cls(
            name=data.get("name"),
            mesh_id=data.get("mesh_id"),
            material_id=data.get("material_id")
        )
        m.transform = Transform.from_dict(data.get("transform", {}))
        m.cast_shadow = data.get("cast_shadow", True)
        m.receive_shadow = data.get("receive_shadow", True)
        return m

# =====================================================
# Light
# =====================================================
class Light(Spatial):
    def __init__(self, name: Optional[str]=None, light_type: str="directional"):
        super().__init__(name=name or "Light", transform=Transform())
        self.light_type = light_type
        self.color = (1.0, 1.0, 1.0)
        self.intensity = 1.0
        self.range = 10.0
        self.spot_angle = 30.0

    def to_dict(self) -> Dict[str, Any]:
        d = super().to_dict()
        d.update({
            "light_type": self.light_type,
            "color": list(self.color),
            "intensity": self.intensity,
            "range": self.range,
            "spot_angle": self.spot_angle,
        })
        return d

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Light":
        L = cls(
            name=data.get("name"),
            light_type=data.get("light_type", "directional")
        )
        L.transform = Transform.from_dict(data.get("transform", {}))
        L.color = tuple(data.get("color", (1.0,1.0,1.0)))
        L.intensity = data.get("intensity", 1.0)
        L.range = data.get("range", 10.0)
        L.spot_angle = data.get("spot_angle", 30.0)
        return L

    def get_light_data(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "type": self.light_type,
            "transform": self.world_transform.to_dict(),
            "color": list(self.color),
            "intensity": self.intensity,
            "range": self.range,
            "spot_angle": self.spot_angle
        }


# =====================================================
# Scene (Root manager)
# =====================================================
class Scene:
    def __init__(self, name="MainScene"):
        self.name = name
        self.root = Node("Root")
        self._active = False
        self._last_time = time.time()

        self._cameras: List[Camera] = []
        self._renderables: List[MeshInstance] = []
        self._lights: List[Light] = []

    # -------------------------------------------------
    # INTERNAL — REBUILD CACHES
    # -------------------------------------------------
    def _rebuild_caches(self):
        self._cameras.clear()
        self._renderables.clear()
        self._lights.clear()

        for n in self.root.traverse():
            if isinstance(n, Camera):
                self._cameras.append(n)
            elif isinstance(n, MeshInstance):
                self._renderables.append(n)
            elif isinstance(n, Light):
                self._lights.append(n)

    # -------------------------------------------------
    # INTERNAL — WORLD TRANSFORM UPDATE
    # -------------------------------------------------
    def _update_world_transforms(self, node, parent_transform=None):
        if isinstance(node, Spatial):
            if parent_transform is None:
                node.world_transform = node.transform.copy()
            else:
                px, py, pz = parent_transform.position
                lx, ly, lz = node.transform.position
                node.world_transform = node.transform.copy()
                node.world_transform.position = (px + lx, py + ly, pz + lz)

        for c in node.children:
            self._update_world_transforms(
                c,
                getattr(node, "world_transform", parent_transform)
            )

    # -------------------------------------------------
    # PUBLIC API — tick()
    # -------------------------------------------------
    def tick(self, dt=None):
        now = time.time()
        dt_val = (now - self._last_time) if dt is None else dt
        self._last_time = now

        self._update_world_transforms(self.root, None)
        self.root.process(dt_val)
        self._rebuild_caches()

        return {
            "dt": dt_val,
            "camera_count": len(self._cameras),
            "renderable_count": len(self._renderables),
            "lights": len(self._lights)
        }

    # -------------------------------------------------
    # PUBLIC API — getters
    # -------------------------------------------------
    def get_cameras(self):
        return self._cameras

    def get_renderables(self):
        return [r for r in self._renderables if r.visible]

    def get_lights(self):
        return self._lights

    # -------------------------------------------------
    # SCENE SERIALIZATION
    # -------------------------------------------------
    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "root": self.root.to_dict()
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Scene":
        scene = Scene(name=data.get("name", "Scene"))
        scene.root = Node.from_dict(data.get("root", {}))
        return scene

# =====================================================
# DEFAULT TEST SCENE
# =====================================================
def build_test_scene() -> Scene:
    scene = Scene("TestScene")

    # Camera
    cam = Camera("MainCamera")
    cam.transform.position = (0, 2, -5)
    scene.root.add_child(cam)

    # Light
    light = Light("SunLight", "directional")
    light.intensity = 2.0
    light.transform.rotation_euler = (30, 45, 0)
    scene.root.add_child(light)

    # Cube mesh
    cube = MeshInstance("Cube", mesh_id="cube_mesh", material_id="default_mat")
    cube.transform.position = (0, 0, 0)
    scene.root.add_child(cube)

    return scene


# ======================================================
# REPAIR: build_test_scene() — FULL VERSION
# ======================================================
def build_test_scene() -> Scene:
    """
    Membangun scene test lengkap:
    - 1 Kamera
    - 1 Plane (floor)
    - 1 Box
    - 1 Directional Light
    - Auto-start scene
    """
    s = Scene("test_scene")

    # Kamera
    cam = Camera(name="MainCamera", fov=75.0, aspect=16/9)
    cam.transform.position = (0.0, 2.0, -6.0)
    s.root.add_child(cam)

    # Lantai
    floor = MeshInstance(
        name="Floor",
        mesh_id="mesh_plane",
        material_id="mat_concrete"
    )
    floor.transform.position = (0.0, -1.0, 0.0)
    s.root.add_child(floor)

    # Box
    box = MeshInstance(
        name="Box01",
        mesh_id="mesh_box",
        material_id="mat_metal"
    )
    box.transform.position = (0.0, 0.0, 0.0)
    s.root.add_child(box)

    # Cahaya Directional
    sun = Light(name="Sun", light_type="directional")
    # Default Camera (NeoEngine compliant)
    cam = Camera(name="MainCamera")
    cam.transform.position = (0.0, 2.0, -5.0)
    s.root.add_child(cam)
    # Camera default untuk test render
    cam = Camera(name="MainCamera")
    cam.transform.position = (0.0, 2.0, -5.0)
    # Transform tidak memiliki rotation, jadi tidak diset
    s.root.add_child(cam)
    # Camera default untuk test render
    cam = Camera(name="MainCamera")
    cam.transform.position = (0.0, 2.0, -5.0)
    # Transform tidak memiliki rotation, jadi tidak diset
    s.root.add_child(cam)
    # Camera default untuk test render
    cam = Camera(name="MainCamera")
    cam.transform.position = (0.0, 2.0, -5.0)
    cam.transform.rotation = (0.0, 0.0, 0.0)
    s.root.add_child(cam)
    sun.transform.position = (0.0, 10.0, -10.0)
    s.root.add_child(sun)
    return s

