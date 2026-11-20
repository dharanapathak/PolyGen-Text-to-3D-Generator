# PolyGen Prototype Architecture

```text
┌────────────────────┐
│ User Text Prompt  │
└─────────┬──────────┘
          ↓
┌────────────────────┐
│ Prompt Processor   │  keyword-based shape/color detection
└─────────┬──────────┘
          ↓
┌────────────────────┐
│ Mesh Generator    │  procedural primitive geometry
└─────────┬──────────┘
          ↓
┌────────────────────┐
│ 3D Preview (Plotly)│
└─────────┬──────────┘
          ↓
┌────────────────────┐
│ OBJ Export         │
└────────────────────┘

Future extension: replace or augment procedural generator with a connected AI text-to-3D service.
```
