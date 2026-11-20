"""
PolyGen prompt processing module.

Converts simple natural-language descriptions
into structured 3D primitive specifications.
"""

import re

SHAPE_KEYWORDS = {
    "cube": {"cube", "box", "block"},
    "sphere": {"sphere", "ball", "globe"},
    "cylinder": {"cylinder", "tube"},
    "cone": {"cone"},
}

DEFAULT_DIMENSIONS = {
    "cube": {"width": 1.0, "height": 1.0, "depth": 1.0},
    "sphere": {"radius": 0.5},
    "cylinder": {"radius": 0.5, "height": 1.0},
    "cone": {"radius": 0.5, "height": 1.0},
}

MATERIAL_KEYWORDS = {
    "wood": {"wood", "wooden"},
    "metal": {"metal", "metallic", "steel"},
    "glass": {"glass"},
    "plastic": {"plastic"},
    "stone": {"stone", "rock"},
}


def find_shape(words):
    """Identify a supported primitive shape."""
    for shape, keywords in SHAPE_KEYWORDS.items():
        if words.intersection(keywords):
            return shape

    return None


def find_material(words):
    """Identify a material mentioned in the prompt."""
    for material, keywords in MATERIAL_KEYWORDS.items():
        if words.intersection(keywords):
            return material

    return "unspecified"


def generate_asset_spec(prompt):
    """
    Convert a text prompt into a structured 3D asset specification.

    Supported shapes: cube, sphere, cylinder and cone.
    This function prepares specifications, not actual 3D meshes.
    """

    if not isinstance(prompt, str):
        raise TypeError("Prompt must be a string.")

    cleaned_prompt = " ".join(prompt.strip().split())

    if not cleaned_prompt:
        raise ValueError("Prompt cannot be empty.")

    words = set(
        re.findall(r"[a-zA-Z0-9]+", cleaned_prompt.lower())
    )

    shape = find_shape(words)
    material = find_material(words)

    dimensions = None

    if shape:
        dimensions = DEFAULT_DIMENSIONS[shape].copy()

    result = {
        "prompt": cleaned_prompt,
        "shape": shape,
        "dimensions": dimensions,
        "material": material,
        "supported": shape is not None,
        "status": (
            "ready_for_geometry"
            if shape
            else "unsupported_shape"
        ),
    }

    return result
