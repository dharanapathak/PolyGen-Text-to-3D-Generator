# PolyGen — Generative Text-to-3D Asset Pipeline

> A Python-based Text-to-3D asset generation prototype developed as part of a Generative AI internship project.

## About the Project

**PolyGen** is a Text-to-3D Asset Pipeline project that aims to simplify 3D asset creation through text-based prompts. Users can describe a basic object using natural language, and the system processes the prompt to generate a corresponding procedural 3D object that can be visualized and exported.

The project explores the integration of Python, interactive visualization, prompt processing, procedural 3D geometry, and Generative AI workflows.

This project is being developed as part of a one-month project completion timeline under the internship program at Infotact Solutions.

---

## Project Information

| Field | Details |
|---|---|
| Project Name | PolyGen |
| Project Title | Generative Text-to-3D Asset Pipeline |
| Organization | Infotact Solutions |
| Internship Domain | Generative AI |
| Internship Role | Associate L1 Intern |
| Group | Group 8 |
| Project Duration | 1 Month |
| Development Language | Python |

---

## Problem Statement

Traditional 3D asset creation often requires specialized modeling skills, time, and manual effort. Creating simple objects through conventional modeling workflows can be challenging for beginners and may slow down rapid prototyping.

PolyGen explores a text-driven workflow where users can describe objects in natural language and generate basic 3D assets through a simplified interface.

---

## Project Objectives

- Develop a simple text-to-3D asset generation interface.
- Process natural-language prompts to identify object characteristics.
- Generate basic procedural 3D geometries.
- Visualize generated objects interactively.
- Enable users to export generated 3D assets.
- Explore the integration of Generative AI into 3D modeling workflows.
- Develop practical skills in Python application development and AI pipeline design.

---

## Key Features

- Text-based prompt input
- Interactive web-based interface
- Basic procedural 3D object generation
- Shape and color interpretation from prompts
- 3D object visualization
- OBJ model export
- Modular Python project structure
- Basic testing and documentation

---

## System Workflow

```text
        User
         |
         v
   Enter Text Prompt
         |
         v
  Prompt Processing
         |
         v
 Object / Shape Identification
         |
         v
 Procedural 3D Generation
         |
         v
   Interactive Preview
         |
         v
   Export 3D Asset
```

---

## Project Architecture

The project follows a modular architecture to separate the user interface, prompt processing, object generation, and output handling.

- **Frontend:** Streamlit-based interactive interface
- **Prompt Processing:** Identifies relevant object and shape information from user text
- **3D Generation:** Creates procedural 3D geometries
- **Visualization:** Displays generated objects
- **Export:** Supports exporting 3D objects in OBJ format

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core development language |
| Streamlit | Interactive web application |
| 3D Geometry Libraries | Procedural object generation |
| Plotly | Interactive 3D visualization |
| NumPy | Numerical operations and geometry support |
| Git & GitHub | Version control and project hosting |

---

## Project Development Timeline

The project is organized into a four-week development plan covering research, development, integration, testing, and final documentation.

### Week 1 — Research, Requirement Analysis & Project Setup

**Objective:** Establish the foundation of the project.

Work planned and organized:

- Understand the Text-to-3D generation concept.
- Research AI-based 3D asset generation approaches.
- Define the problem statement.
- Identify project objectives and scope.
- Analyze functional requirements.
- Plan the system architecture and workflow.
- Set up the Python development environment.
- Create the project folder structure.
- Identify required libraries and tools.

**Deliverables:**
- Project requirements
- Problem statement and objectives
- Initial architecture
- Development environment
- Project structure

### Week 2 — Core Development & Prototype Implementation

**Objective:** Develop the initial working prototype.

Work planned and implemented in the prototype:

- Create the Streamlit application interface.
- Implement text prompt input.
- Process basic prompt descriptions.
- Identify supported object shapes and colors.
- Generate procedural 3D geometries.
- Display generated objects interactively.
- Implement OBJ export functionality.
- Organize source code into modules.

**Deliverables:**
- Initial application interface
- Prompt processing
- Procedural 3D generation
- 3D preview
- OBJ export prototype

### Week 3 — Integration, Testing & Improvements

**Objective:** Validate the application and improve its workflow.

Planned activities:

- Test the application with multiple text prompts.
- Validate object and shape generation.
- Check generated 3D visualization.
- Test file export functionality.
- Identify and fix bugs.
- Improve prompt handling and error handling.
- Improve the application interface.
- Record testing observations.

**Deliverables:**
- Test cases
- Bug fixes
- Improved workflow
- Testing documentation
- Test observations

### Week 4 — Finalization & Documentation

**Objective:** Prepare the project for final internship submission.

Planned activities:

- Perform final application checks.
- Review project code and folder structure.
- Complete final testing.
- Prepare project documentation.
- Write the project report.
- Create presentation slides.
- Capture project screenshots.
- Prepare the final demonstration.
- Organize the final deliverables.

**Deliverables:**
- Final source code
- README documentation
- Project report
- Internship presentation
- Screenshots
- Final demonstration

---

## Project Structure

```text
PolyGen-Text-to-3D-Asset-Pipeline/
│
├── app.py
├── requirements.txt
├── README.md
│
├── src/
│   ├── __init__.py
│   └── generator.py
│
├── docs/
│   ├── week1_progress.md
│   ├── week2_progress.md
│   ├── architecture.md
│   └── project_notes.md
│
└── tests/
    └── test_generator.py
```

---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/PolyGen-Text-to-3D-Asset-Pipeline.git
```

### 2. Navigate to the Project Folder

```bash
cd PolyGen-Text-to-3D-Asset-Pipeline
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Environment

**Windows:**

```powershell
.venv\Scripts\activate
```

**Linux/macOS:**

```bash
source .venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## Usage

1. Launch the PolyGen application.
2. Enter a description of the desired 3D object.
3. Select or generate the object through the available workflow.
4. View the generated 3D object in the interactive preview.
5. Export the generated asset if the export option is available.

### Example Prompts

```text
Generate a red cube.
```

```text
Create a blue sphere.
```

```text
Generate a green cylinder.
```

```text
Create a basic 3D robot.
```

```text
Generate a low-poly sports car.
```

---

## Testing

The project can be tested using different text prompts and supported geometric shapes.

| Test Case | Input Prompt | Purpose |
|---|---|---|
| TC-01 | Red cube | Verify cube generation and color processing |
| TC-02 | Blue sphere | Verify spherical geometry generation |
| TC-03 | Green cylinder | Verify cylinder generation |
| TC-04 | Yellow cone | Verify cone generation |
| TC-05 | Empty prompt | Check input validation |
| TC-06 | Unsupported prompt | Check handling of unsupported objects |
| TC-07 | Export 3D object | Verify OBJ export functionality |

Actual test results should be recorded after running the application.

---

## Applications

PolyGen's text-driven 3D asset workflow has potential applications in:

- Game development
- 3D prototyping
- Educational demonstrations
- Product visualization
- Animation workflows
- Virtual Reality (VR)
- Augmented Reality (AR)
- Digital content creation

---

## Limitations

- The current prototype focuses on basic procedural geometry.
- Complex objects may not be accurately represented.
- Prompt understanding is limited to the implemented processing logic.
- Detailed textures and realistic materials are limited.
- Advanced AI-generated meshes require additional model/API integration.
- Generation quality depends on the supported implementation.

---

## Future Scope

Future development may include:

- Integration of real AI text-to-3D models.
- Support for complex object generation.
- Advanced prompt understanding using LLMs.
- Texture and material generation.
- Improved mesh quality.
- Additional export formats such as GLB and STL.
- Customization of object dimensions.
- AI-powered prompt enhancement.
- Cloud-based generation.
- Improved user experience and asset management.

---

## Learning Outcomes

Through the PolyGen project, the following technical and professional skills are explored:

- Python application development
- Generative AI concepts
- Prompt processing
- Procedural 3D modeling
- Interactive application development
- Software architecture
- Testing and debugging
- Version control using Git
- Technical documentation
- Project planning and teamwork

---

## Team Information

**Group:** Group 8  
**Organization:** Infotact Solutions  
**Domain:** Generative AI  
**Project:** PolyGen — Generative Text-to-3D Asset Pipeline

---

## Acknowledgement

This project is being developed as part of the Generative AI internship program at Infotact Solutions. The internship provides an opportunity to explore practical software development, AI workflows, project documentation, testing, and the implementation of a prototype application.

---

## Conclusion

PolyGen explores a simplified text-driven approach to 3D asset creation by combining prompt processing, procedural geometry generation, visualization, and asset export in a Python-based application.

The project provides a foundation for understanding how natural-language interfaces can simplify 3D creation workflows and how Generative AI technologies can be integrated into creative software applications.

---

## License

This project is developed for educational and internship purposes.

---

**Developed as part of the Generative AI Internship | Group 8 | Infotact Solutions**
