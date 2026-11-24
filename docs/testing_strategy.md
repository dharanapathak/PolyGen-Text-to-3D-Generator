# PolyGen – Testing Strategy

## 1. Introduction

Testing is an important part of the PolyGen project. It helps verify that the prompt-processing module correctly interprets user input and prepares structured specifications for supported 3D primitive objects.

This document defines the testing approach, test scenarios, expected results, and validation process for the project.

## 2. Testing Objectives

- Verify correct shape identification.
- Validate natural-language prompt processing.
- Check material and colour detection.
- Verify default object dimensions.
- Handle empty and invalid inputs.
- Identify unsupported object descriptions.
- Improve the reliability of the generation module.

## 3. Testing Scope

The initial testing scope focuses on the Python function `generate_asset_spec()`.

The supported primitive shapes include:

- Cube
- Sphere
- Cylinder
- Cone

The tests also cover alternative names, material information, colour information, and input validation.

## 4. Test Scenarios

| Test Case | Input | Expected Result |
|---|---|---|
| Cube Recognition | Create a cube | Shape identified as cube |
| Sphere Recognition | Create a sphere | Shape identified as sphere |
| Cylinder Recognition | Create a cylinder | Shape identified as cylinder |
| Cone Recognition | Create a cone | Shape identified as cone |
| Alias Recognition | Create a box | Shape identified as cube |
| Material Detection | Wooden cube | Material identified as wood |
| Colour Detection | Red cube | Colour identified as red |
| Empty Input | Empty string | ValueError raised |
| Invalid Input | Numeric value | TypeError raised |
| Unsupported Object | Create a dragon | Unsupported status returned |

These scenarios describe expected behaviour and should be verified against the implemented generator.

## 5. Testing Tools

- Python
- unittest
- GitHub
- Python command-line interface

## 6. Test Execution

The test suite can be executed from the project root directory using:

```bash
python -m unittest discover -s tests -v
```

The command discovers test files inside the tests directory and executes the available test cases.

## 7. Expected Outcomes

- Supported shapes should be identified correctly.
- Object properties should be extracted when available.
- Invalid prompts should be handled safely.
- Unsupported shapes should return an appropriate status.
- The generator should provide consistent structured output.

## 8. Error Handling

The testing process should verify that invalid inputs do not cause unexpected application failures.

Empty prompts, non-string values, and unsupported object descriptions should be handled through appropriate validation and status responses.

## 9. Testing Status

**Current Status:** Testing documentation prepared.

**Execution Status:** Pending local test execution and verification.

Test results should be recorded only after running the test suite.

## 10. Conclusion

This testing strategy establishes a structured approach for validating the PolyGen prompt-processing module. It provides a foundation for improving code quality, reliability, and future integration with 3D geometry generation components.
