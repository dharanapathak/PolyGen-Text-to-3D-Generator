"""PolyGen prompt processing and asset specification module."""

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

COLOR_KEYWORDS = {
    "red", "blue", "green", "black", "white",
    "yellow", "orange", "purple", "brown",
    "pink", "gray", "grey"
}


def tokenize_prompt(prompt):
    """Convert a prompt into normalized words."""
    return set(re.findall(r"[a-zA-Z0-9]+", prompt.lower()))


def find_shape(words):
    """Identify the requested primitive shape."""
    for shape, keywords in SHAPE_KEYWORDS.items():
        if words.intersection(keywords):
            return shape
    return None


def find_material(words):
    """Identify the material mentioned in the prompt."""
    for material, keywords in MATERIAL_KEYWORDS.items():
        if words.intersection(keywords):
            return material
    return "unspecified"


def find_color(words):
    """Identify a supported color in the prompt."""
    matching_colors = words.intersection(COLOR_KEYWORDS)
    if matching_colors:
        return sorted(matching_colors)[0]
    return "unspecified"


def generate_asset_spec(prompt):
    """Convert text descriptions into structured 3D specifications."""

    if not isinstance(prompt, str):
        raise TypeError("Prompt must be a string.")

    cleaned_prompt = " ".join(prompt.strip().split())

    if not cleaned_prompt:
        raise ValueError("Prompt cannot be empty.")

    words = tokenize_prompt(cleaned_prompt)

    shape = find_shape(words)
    material = find_material(words)
    color = find_color(words)

    dimensions = (
        DEFAULT_DIMENSIONS[shape].copy()
        if shape else None
    )

    return {
        "prompt": cleaned_prompt,
        "shape": shape,
        "dimensions": dimensions,
        "material": material,
        "color": color,
        "supported": shape is not None,
        "status": (
            "ready_for_geometry"
            if shape else "unsupported_shape"
        ),
    }
