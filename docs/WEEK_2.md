# Week 2 — Core Development Prototype
**Group 8 | PolyGen: Generative Text-to-3D Asset Pipeline**

## Goal
Build the first runnable interface and a basic text-prompt-to-mesh prototype.

## Implemented in this starter
- Streamlit prompt-entry UI
- Keyword detection for a few shape types (cube, sphere, cylinder, cone, robot)
- Basic color keyword detection
- Procedural geometry generation
- Interactive 3D preview using Plotly
- OBJ text export download

## Important scope note
This is a rule-based procedural prototype, not a text-to-3D AI model. It is an early pipeline/demo that validates the user flow. A real AI model or external service must be integrated and tested in a later phase before describing that capability as implemented.

## Workflow
Prompt → Keyword parsing → Primitive mesh generation → Plotly preview → OBJ download

## Week 2 checklist
- [ ] Install requirements
- [ ] Run Streamlit app
- [ ] Try sample prompts and record results
- [ ] Verify downloaded OBJ in a 3D editor
- [ ] Capture actual screenshots for GitHub/report
- [ ] Record bugs or limitations encountered
