"""Create procedural triangle meshes for supported PolyGen primitives."""

from math import cos, pi, sin
from typing import Iterable


# A mesh is represented by vertices and triangle faces. Each returned mesh
# also contains Plotly arrays and an OBJ text fragment for downloading.


def _triangulate(polygons: Iterable[tuple[int, ...]]) -> list[tuple[int, int, int]]:
    triangles: list[tuple[int, int, int]] = []
    for polygon in polygons:
        for index in range(1, len(polygon) - 1):
            triangles.append((polygon[0], polygon[index], polygon[index + 1]))
    return triangles


def _package_mesh(
    name: str,
    vertices: list[tuple[float, float, float]],
    faces: list[tuple[int, int, int]],
    obj_vertex_offset: int,
) -> dict:
    x = [vertex[0] for vertex in vertices]
    y = [vertex[1] for vertex in vertices]
    z = [vertex[2] for vertex in vertices]

    obj_lines = [f"o {name}"]
    obj_lines.extend(f"v {vx:.6f} {vy:.6f} {vz:.6f}" for vx, vy, vz in vertices)
    for a, b, c in faces:
        # OBJ indices are one-based and must remain unique across combined parts.
        obj_lines.append(
            f"f {a + 1 + obj_vertex_offset} {b + 1 + obj_vertex_offset} {c + 1 + obj_vertex_offset}"
        )

    return {
        "name": name,
        "x": x,
        "y": y,
        "z": z,
        "i": [face[0] for face in faces],
        "j": [face[1] for face in faces],
        "k": [face[2] for face in faces],
        "obj": "\n".join(obj_lines),
        "vertex_count": len(vertices),
    }


def _box_mesh(
    name: str,
    size: tuple[float, float, float] = (1.0, 1.0, 1.0),
    center: tuple[float, float, float] = (0.0, 0.0, 0.0),
    obj_vertex_offset: int = 0,
) -> dict:
    sx, sy, sz = (dimension / 2.0 for dimension in size)
    cx, cy, cz = center
    vertices = [
        (cx - sx, cy - sy, cz - sz),
        (cx + sx, cy - sy, cz - sz),
        (cx + sx, cy + sy, cz - sz),
        (cx - sx, cy + sy, cz - sz),
        (cx - sx, cy - sy, cz + sz),
        (cx + sx, cy - sy, cz + sz),
        (cx + sx, cy + sy, cz + sz),
        (cx - sx, cy + sy, cz + sz),
    ]
    polygons = [
        (0, 3, 2, 1),
        (4, 5, 6, 7),
        (0, 1, 5, 4),
        (1, 2, 6, 5),
        (2, 3, 7, 6),
        (3, 0, 4, 7),
    ]
    return _package_mesh(name, vertices, _triangulate(polygons), obj_vertex_offset)


def _sphere_mesh(
    name: str,
    radius: float = 0.5,
    center: tuple[float, float, float] = (0.0, 0.0, 0.0),
    segments: int = 20,
    rings: int = 12,
    obj_vertex_offset: int = 0,
) -> dict:
    cx, cy, cz = center
    vertices: list[tuple[float, float, float]] = []
    for ring in range(rings + 1):
        phi = pi * ring / rings
        for segment in range(segments + 1):
            theta = 2.0 * pi * segment / segments
            vertices.append((
                cx + radius * sin(phi) * cos(theta),
                cy + radius * sin(phi) * sin(theta),
                cz + radius * cos(phi),
            ))

    faces: list[tuple[int, int, int]] = []
    row_length = segments + 1
    for ring in range(rings):
        for segment in range(segments):
            a = ring * row_length + segment
            b = a + row_length
            faces.append((a, b, a + 1))
            faces.append((a + 1, b, b + 1))

    return _package_mesh(name, vertices, faces, obj_vertex_offset)


def _cylinder_mesh(
    name: str,
    radius: float = 0.5,
    height: float = 1.0,
    segments: int = 24,
    center: tuple[float, float, float] = (0.0, 0.0, 0.0),
    obj_vertex_offset: int = 0,
) -> dict:
    cx, cy, cz = center
    bottom_z = cz - height / 2.0
    top_z = cz + height / 2.0
    vertices: list[tuple[float, float, float]] = []
    for z_value in (bottom_z, top_z):
        for segment in range(segments):
            angle = 2.0 * pi * segment / segments
            vertices.append((cx + radius * cos(angle), cy + radius * sin(angle), z_value))

    bottom_center = len(vertices)
    vertices.append((cx, cy, bottom_z))
    top_center = len(vertices)
    vertices.append((cx, cy, top_z))

    faces: list[tuple[int, int, int]] = []
    for segment in range(segments):
        following = (segment + 1) % segments
        bottom_a, bottom_b = segment, following
        top_a, top_b = segments + segment, segments + following
        faces.extend([
            (bottom_a, bottom_b, top_b),
            (bottom_a, top_b, top_a),
            (bottom_center, bottom_b, bottom_a),
            (top_center, top_a, top_b),
        ])

    return _package_mesh(name, vertices, faces, obj_vertex_offset)


def _cone_mesh(
    name: str,
    radius: float = 0.5,
    height: float = 1.0,
    segments: int = 24,
    center: tuple[float, float, float] = (0.0, 0.0, 0.0),
    obj_vertex_offset: int = 0,
) -> dict:
    cx, cy, cz = center
    base_z = cz - height / 2.0
    apex_z = cz + height / 2.0
    vertices = [
        (cx + radius * cos(2.0 * pi * segment / segments),
         cy + radius * sin(2.0 * pi * segment / segments), base_z)
        for segment in range(segments)
    ]
    apex_index = len(vertices)
    vertices.append((cx, cy, apex_z))
    center_index = len(vertices)
    vertices.append((cx, cy, base_z))

    faces: list[tuple[int, int, int]] = []
    for segment in range(segments):
        following = (segment + 1) % segments
        faces.append((segment, following, apex_index))
        faces.append((center_index, following, segment))

    return _package_mesh(name, vertices, faces, obj_vertex_offset)


def _robot_meshes() -> list[dict]:
    """Build a simple robot from separate procedural box and sphere parts."""
    parts: list[tuple[str, dict]] = [
        ("robot_torso", {"size": (0.65, 0.38, 0.75), "center": (0.0, 0.0, 0.0)}),
        ("robot_head", {"size": (0.48, 0.42, 0.42), "center": (0.0, 0.0, 0.62)}),
        ("robot_left_arm", {"size": (0.18, 0.22, 0.62), "center": (-0.43, 0.0, 0.0)}),
        ("robot_right_arm", {"size": (0.18, 0.22, 0.62), "center": (0.43, 0.0, 0.0)}),
        ("robot_left_leg", {"size": (0.22, 0.28, 0.55), "center": (-0.19, 0.0, -0.62)}),
        ("robot_right_leg", {"size": (0.22, 0.28, 0.55), "center": (0.19, 0.0, -0.62)}),
    ]

    meshes: list[dict] = []
    offset = 0
    for name, parameters in parts:
        mesh = _box_mesh(name, obj_vertex_offset=offset, **parameters)
        meshes.append(mesh)
        offset += mesh["vertex_count"]

    for eye_name, eye_x in (("robot_left_eye", -0.11), ("robot_right_eye", 0.11)):
        mesh = _sphere_mesh(
            eye_name, radius=0.045, center=(eye_x, -0.218, 0.67),
            segments=10, rings=6, obj_vertex_offset=offset,
        )
        meshes.append(mesh)
        offset += mesh["vertex_count"]

    return meshes


def build_asset(parsed: dict) -> list[dict]:
    """Build Plotly-ready meshes and OBJ fragments from process_prompt output."""
    if not isinstance(parsed, dict):
        raise TypeError("Parsed asset specification must be a dictionary.")

    if not parsed.get("supported"):
        raise ValueError("This prompt does not describe a supported 3D shape.")

    shape = parsed.get("shape")
    builders = {
        "cube": lambda offset: _box_mesh("cube", obj_vertex_offset=offset),
        "sphere": lambda offset: _sphere_mesh("sphere", obj_vertex_offset=offset),
        "cylinder": lambda offset: _cylinder_mesh("cylinder", obj_vertex_offset=offset),
        "cone": lambda offset: _cone_mesh("cone", obj_vertex_offset=offset),
    }

    if shape == "robot":
        return _robot_meshes()
    if shape not in builders:
        raise ValueError(f"Unsupported shape: {shape!r}")

    mesh = builders[shape](0)
    return [mesh]
