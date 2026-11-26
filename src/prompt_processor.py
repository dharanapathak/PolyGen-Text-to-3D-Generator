"""Convert simple natural-language prompts into 3D asset specifications."""

import re
from typing import Any


SHAPE_KEYWORDS = {
    # Put robot first so a prompt such as "robot with a cube head" is a robot.
    "robot": {"robot", "android"},
    "cube": {"cube", "box", "block"},
    "sphere": {"sphere", "ball", "globe"},
    "cylinder": {"cylinder", "tube"},
    "cone": {"cone"},
}

COLOR_HEX = {
    "red": "#e53935",
    "blue": "#1e88e5",
    "green": "#43a047",
    "yellow": "#fdd835",
    "orange": "#fb8c00",
    "purple": "#8e24aa",
    "pink": "#ec407a",
    "black": "#263238",
    "white": "#f5f5f5",
    "gray": "#78909c",
    "grey": "#78909c",
    "brown": "#8d6e63",
    "cyan": "#00acc1",
}

MATERIAL_KEYWORDS = {
    "wood": {"wood", "wooden"},
    "metal": {"metal", "metallic", "steel"},
    "glass": {"glass"},
    "plastic": {"plastic"},
    "stone": {"stone", "rock"},
}


def _tokens(text: str) -> set[str]:
    """Return lowercase word tokens from text."""
    return set(re.findall(r"[a-zA-Z0-9]+", text.lower()))


def process_prompt(prompt: str) -> dict[str, Any]:
    """Parse a prompt into shape, colour, material and description fields.

    Supported shapes are cube, sphere, cylinder, cone and a simple robot
    assembled from primitive boxes and spheres. This is rule-based parsing,
    not an LLM or text-to-3D model.
    """
    if not isinstance(prompt, str):
        raise TypeError("Prompt must be a string.")

    description = " ".join(prompt.strip().split())
    if not description:
        raise ValueError("Please enter a description of a 3D object.")

    words = _tokens(description)

    detected_shape = None
    for shape, keywords in SHAPE_KEYWORDS.items():
        if words.intersection(keywords):
            detected_shape = shape
            break

    detected_color = next((colour for colour in COLOR_HEX if colour in words), None)
    # Treat grey and gray as the same visual colour, preserving the typed label.
    display_color = COLOR_HEX.get(detected_color, "#64b5f6")

    detected_material = "unspecified"
    for material, keywords in MATERIAL_KEYWORDS.items():
        if words.intersection(keywords):
            detected_material = material
            break

    return {
        "shape": detected_shape or "unsupported",
        "color": detected_color or "not specified",
        "display_color": display_color,
        "material": detected_material,
        "description": description,
        "supported": detected_shape is not None,
    }
