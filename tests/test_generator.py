
"""Unit tests for the PolyGen prompt processing module."""

import unittest

from src.generator import generate_asset_spec


class TestPolyGenGenerator(unittest.TestCase):

    def test_cube_generation(self):
        result = generate_asset_spec("Create a cube")
        self.assertEqual(result["shape"], "cube")
        self.assertTrue(result["supported"])

    def test_box_alias(self):
        result = generate_asset_spec("Create a box")
        self.assertEqual(result["shape"], "cube")

    def test_sphere_generation(self):
        result = generate_asset_spec("Generate a sphere")
        self.assertEqual(result["shape"], "sphere")

    def test_cylinder_generation(self):
        result = generate_asset_spec("Create a cylinder")
        self.assertEqual(result["shape"], "cylinder")

    def test_cone_generation(self):
        result = generate_asset_spec("Create a cone")
        self.assertEqual(result["shape"], "cone")

    def test_material_detection(self):
        result = generate_asset_spec("Create a wooden cube")
        self.assertEqual(result["material"], "wood")

    def test_unsupported_shape(self):
        result = generate_asset_spec("Create a dragon")
        self.assertFalse(result["supported"])
        self.assertIsNone(result["shape"])

    def test_empty_prompt(self):
        with self.assertRaises(ValueError):
            generate_asset_spec("")

    def test_non_string_prompt(self):
        with self.assertRaises(TypeError):
            generate_asset_spec(123)

    # Additional test cases

    def test_color_detection(self):
        result = generate_asset_spec("Create a red cube")
        self.assertEqual(result["color"], "red")

    def test_default_cube_dimensions(self):
        result = generate_asset_spec("Create a cube")

        expected_dimensions = {
            "width": 1.0,
            "height": 1.0,
            "depth": 1.0
        }

        self.assertEqual(
            result["dimensions"],
            expected_dimensions
        )

    def test_whitespace_normalization(self):
        result = generate_asset_spec("  Create   a   cube  ")

        self.assertEqual(result["prompt"], "Create a cube")
        self.assertEqual(result["shape"], "cube")


if __name__ == "__main__":
    unittest.main()
