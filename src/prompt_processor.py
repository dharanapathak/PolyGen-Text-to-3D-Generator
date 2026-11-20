COLORS = {"red":"red", "blue":"blue", "green":"green", "yellow":"yellow", "black":"black", "white":"white", "orange":"orange", "purple":"purple", "cyan":"cyan", "pink":"pink", "gray":"gray", "grey":"gray"}
SHAPES = ["robot", "sphere", "ball", "cylinder", "cone", "cube", "box"]
def process_prompt(text: str) -> dict:
    cleaned = " ".join(text.strip().split())
    low = cleaned.lower()
    color = next((v for k,v in COLORS.items() if k in low), "royalblue")
    if "robot" in low: shape = "robot"
    elif "sphere" in low or "ball" in low or "apple" in low: shape = "sphere"
    elif "cylinder" in low or "can" in low: shape = "cylinder"
    elif "cone" in low: shape = "cone"
    else: shape = "cube"
    return {"description": cleaned, "shape": shape, "color": color}
