# PolyGen — Group 8
**Generative Text-to-3D Asset Pipeline | Infotact Solutions internship**

## Current prototype status
This Week 2 starter is a working **rule-based procedural prototype**: it reads a text prompt, detects a few shape/color keywords, previews a basic mesh, and exports OBJ. It does **not** connect to a Generative AI text-to-3D model/API yet. AI model integration is planned as a subsequent step and should only be described as implemented after it is actually connected and tested.

## Run locally
1. Install Python 3.10+.
2. From this folder, create and activate a virtual environment:
   - Windows: `py -m venv .venv` then `.venv\\Scripts\\activate`
   - macOS/Linux: `python3 -m venv .venv` then `source .venv/bin/activate`
3. Install: `pip install -r requirements.txt`
4. Run: `streamlit run app.py`
5. Enter prompts like `blue sphere`, `red cube`, `green cylinder`, `yellow cone`, or `small robot` and download the OBJ.

## Folder guide
- `app.py` — Streamlit interface and preview
- `src/prompt_processor.py` — simple keyword-based prompt parsing
- `src/primitive_generator.py` — procedural mesh generation and OBJ export text
- `docs/` — Week 1 and Week 2 notes, architecture, and progress log
- `tests/` — basic unit tests

## Project workflow
Text Prompt → Keyword Prompt Processing → Procedural Mesh Generator → 3D Preview → OBJ Export

## Planned next phase
Replace/extend rule-based geometry with a real text-to-3D model/API, add robust API configuration, validate generated file formats, and evaluate output quality with a documented test set.
