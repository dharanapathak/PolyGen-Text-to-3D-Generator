# PolyGen – System Architecture

## 1. Introduction

This document describes the proposed system architecture of PolyGen, a Generative AI-based project designed to explore text-driven 3D asset creation.

The architecture follows a modular approach in which each component performs a specific task, making the application easier to develop, test, and maintain.

## 2. Architecture Overview

The proposed system follows this workflow:

```text
       User
        |
        v
   Text Prompt Input
        |
        v
   Input Validation
        |
        v
   Prompt Processing
        |
        v
  Object Specification
        |
        v
   3D Geometry Builder
        |
        v
   3D Visualization
        |
        v
    Asset Export
```

The prompt-processing module is the initial development focus. Geometry generation, visualization, and export are further stages of the proposed pipeline.

## 3. Main System Components

### 3.1 User Input Module

Accepts natural-language descriptions of the 3D object that the user wants to create.

Example:

"Create a wooden cube."

### 3.2 Input Validation Module

Checks whether the entered prompt is valid and contains usable text.

It handles empty prompts and invalid input types before further processing.

### 3.3 Prompt Processing Module

Processes the user's description and identifies relevant information.

Its responsibilities include:

- Normalizing the input text.
- Identifying supported object shapes.
- Recognizing object properties.
- Preparing structured generation parameters.

### 3.4 Object Specification Module

Stores the extracted information in a structured format.

The specification may contain:

- Original prompt
- Object shape
- Dimensions
- Material
- Processing status

Example structure:

```python
{
    "prompt": "Create a wooden cube",
    "shape": "cube",
    "dimensions": {
        "width": 1.0,
        "height": 1.0,
        "depth": 1.0
    },
    "material": "wood",
    "supported": True,
    "status": "ready_for_geometry"
}
```

This is an illustrative example of the intended data structure.

### 3.5 3D Geometry Builder

This component is responsible for converting structured object specifications into 3D geometry.

It is part of the proposed architecture and requires further implementation and integration.

### 3.6 Visualization Module

This component is intended to provide a visual preview of generated 3D objects.

Interactive visualization will be integrated as the application develops.

### 3.7 Asset Export Module

The export component is planned to support saving generated 3D assets in suitable file formats.

Actual export functionality will depend on the implemented geometry pipeline.

## 4. Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Application Interface | Streamlit |
| Version Control | Git |
| Code Repository | GitHub |
| Testing | Python unittest |
| Prompt Processing | Python |

## 5. Project Module Organization

```text
PolyGen-Text-to-3D-Asset-Pipeline/
|
|-- app.py
|-- requirements.txt
|-- README.md
|-- .gitignore
|
|-- src/
|   |-- __init__.py
|   |-- generator.py
|
|-- docs/
|   |-- project_documentation.md
|   |-- architecture.md
|
|-- tests/
    |-- test_generator.py
```

## 6. Data Flow

The system processes information through the following stages:

1. The user provides a text description.
2. The application validates the input.
3. The prompt-processing module analyzes the text.
4. Object properties are extracted.
5. A structured object specification is prepared.
6. The specification is intended to be passed to the geometry-generation component.
7. The generated object can subsequently be visualized and exported.

## 7. Current Development Scope

The current architecture separates the initial prompt-processing functionality from the future 3D generation components.

The initial implementation focuses on converting simple text descriptions into structured object specifications.

Full AI-based 3D mesh generation, visualization, and export should be considered pending until those components are implemented and tested.

## 8. Future Improvements

- Integration with advanced text-to-3D models.
- Support for more complex 3D objects.
- Improved prompt interpretation.
- Geometry and mesh generation.
- Material and texture support.
- Interactive 3D visualization.
- Additional asset export formats.

## 9. Conclusion

The proposed PolyGen architecture provides a modular foundation for developing a text-driven 3D asset generation pipeline.

Separating prompt processing, geometry generation, visualization, and export makes the system easier to extend and improve as development progresses.
