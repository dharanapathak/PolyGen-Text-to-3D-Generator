from src.prompt_processor import process_prompt

def test_detect_sphere_and_blue():
    result = process_prompt("blue sphere")
    assert result["shape"] == "sphere"
    assert result["color"] == "blue"

def test_robot():
    assert process_prompt("small robot")["shape"] == "robot"
