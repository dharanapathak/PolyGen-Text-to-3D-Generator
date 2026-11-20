"""Unit tests for the PolyGen generation module."""

import unittest

from src.generator import generate_asset_spec


class TestGenerateAssetSpec(unittest.TestCase):

    def test_cube_prompt(self):
        result = generate_asset_spec("Create a cube")

        self.assertEqual(result["shape"], "cube")
        self.assertTrue(result["supported"])

    def test_box_alias(self):
        result = generate_asset_spec("Create a box")

        self.assertEqual(result["shape"], "cube")

    def test_sphere_prompt(self):
        result = generate_asset_spec("Generate a sphere")

        self.assertEqual(result["shape"], "sphere")
        self.assertEqual(result["dimensions"]["radius"], 0.5)

    def test_cylinder_prompt(self):
        result = generate_asset_spec("Create a cylinder")

        self.assertEqual(result["shape"], "cylinder")

    def test_material_detection(self):
        result = generate_asset_spec("Create a wooden cylinder")

        self.assertEqual(result["material"], "wood")

    def test_unsupported_prompt(self):
        result = generate_asset_spec("Create a dragon")

        self.assertFalse(result["supported"])
        self.assertIsNone(result["dimensions"])

    def test_empty_prompt(self):
        with self.assertRaises(ValueError):
            generate_asset_spec("")


if __name__ == "__main__":
    unittest.main()
