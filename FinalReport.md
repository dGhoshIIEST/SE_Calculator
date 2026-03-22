# Software Engineering Laboratory: Final Project Report
**Project:** Extensible Calculator System - Complex Number Arithmetic
**Team:** Group 13
**Target Integration Branch:** `Group_B`

---

## 1. Introduction and Objective
The primary objective of this laboratory experiment was to gain practical experience with industry-style software development practices. This was achieved by applying all phases of the Software Development Life Cycle (SDLC) to a single, extensible Python-based calculator system. 

Our specific team, Group 13, was tasked with analyzing, designing, implementing, and testing the **Complex Number Arithmetic** extension. The goal was to build a modular feature that integrates seamlessly with the base calculator application while adhering to strict version control and testing protocols.

## 2. Requirement Analysis
During the initial phase of the SDLC, we identified the specific functional and non-functional requirements for the complex number module. 

**Functional Requirements:**
* The module must accept user input exclusively as a continuous string (e.g., `'(3+2j)*(5+3j)'`).
* It must support the standard $a+bj$ mathematical representation.
* The system must perform standard arithmetic operations: addition, subtraction, multiplication, and division of complex numbers.
* The system must compute advanced metrics: magnitude and phase.

**Non-Functional Requirements & Constraints:**
* Code must be highly modular and maintainable, isolating complex logic from the core `Calculator` class.
* All errors (like malformed strings or division by zero) must be handled gracefully without crashing the main application.

## 3. System Architecture and Design
To fulfill the requirements, we designed an independent software component to handle all complex domain logic. 

* **Object-Oriented Encapsulation:** We designed a standalone `ComplexCalculator` class. This ensures that the base system remains untouched and adheres to the Open/Closed Principle (open for extension, closed for modification).
* **String Parsing Engine:** Because inputs are strict strings, we designed a parsing layer using Python's Regular Expressions (`re` module). We engineered the pattern `r'\(([^)]+)\)([\+\-\*\/])\(([^)]+)\)'` to dynamically isolate the first operand, the arithmetic operator, and the second operand, bypassing arbitrary whitespace issues.
* **Mathematical Delegation:** Rather than manually calculating complex arithmetic, the design leverages Python's native `complex()` casting capabilities and the standard `cmath` library to guarantee mathematical precision.

## 4. Implementation Details
The implementation phase translated our design into functional Python code within the `complex.py` module. 

* **Arithmetic Execution:** Once the regex engine extracts the string components, they are cast to `complex` objects. Python's overloaded operators process the calculation, and a custom `_format_result` method reconstructs the output back into the required $a+bj$ string format.
* **Magnitude Computation:** Implemented using the built-in `abs(z)` function, which efficiently processes the underlying $\sqrt{a^2 + b^2}$ calculation.
* **Phase Computation:** Implemented using `cmath.phase(z)`, which safely maps the angle in radians across all four quadrants.
* **Exception Handling:** A robust `try-except` block is implemented to catch `ValueError` instances. If the regex fails to find a match, or if a zero-division occurs during evaluation, the module halts the calculation and returns a descriptive error string.

## 5. Software Testing and Quality Assurance
Test-driven development practices were strictly followed. A comprehensive unit test suite was developed in `test_complex.py` using Python's native `unittest` framework to ensure high code quality and test coverage.

The test suite validates the system against three core paradigms:
* **Normal Cases:** Tests verify standard execution for all operations (e.g., asserting that `(1+2j)+(2+3j)` successfully evaluates to `3.0+5.0j`).
* **Boundary Conditions:** Edge cases were tested, most notably asserting that evaluating `(5+5j)/(0+0j)` correctly raises a `ValueError` rather than triggering a system-level math fault.
* **Invalid Input Handling:** The parser's resilience was tested by injecting malformed strings (e.g., missing parentheses, alphabetic characters, and unsupported operators). The tests confirm that the system correctly identifies and rejects these inputs.

## 6. Version Control and Configuration Management
To support concurrent development across 20 groups without code conflicts, strict Git configuration management protocols were followed.

* **Repository Forking & Cloning:** The main project repository was forked to an isolated environment. As Group 13 falls into the second cohort, we specifically cloned and targeted the `Group_B` branch for our baseline code.
* **Feature Branching:** Development was conducted entirely within an isolated feature branch (`FeatureB_13`) to prevent contamination of the group's integration branch.
* **Integration and Merging:** Following successful local testing, code updates were committed incrementally. The final feature was pushed to the remote fork, and a Pull Request was generated targeting the main repository's `Group_B` branch, ensuring zero merge conflicts with other teams.

## 7. Conclusion
Through this experiment, Group 13 successfully applied the complete Software Development Life Cycle. By conducting thorough requirement analysis, designing a modular regex-driven architecture, implementing robust unit tests, and adhering to strict Git branching strategies, we successfully delivered a highly functional and reliable Complex Number Arithmetic module for the extensible calculator system.