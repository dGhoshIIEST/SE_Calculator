# 📐 Design Notes: Complex Number Arithmetic Module
**Team:** Group 13
**Target Branch:** `Group_B`

---

## 1. Architectural Approach
* **Modularity:** The feature is logically encapsulated within an independent `ComplexCalculator` class. This ensures clean integration with the base system without accidentally altering the core `Calculator` class .
* **Separation of Concerns:** The module strictly divides responsibilities into three internal domains: string parsing, mathematical execution, and error management.

## 2. Input Parsing Strategy
* **Constraint:** The system strictly requires mathematical inputs to be provided as continuous strings (e.g., `'(3+2j)*(5+3j)'`).
* **Solution:** We implemented Python's `re` (Regular Expressions) module to act as the extraction engine. 
    * *Pre-processing:* All arbitrary whitespaces are stripped to standardize the user's input.
    * *Extraction:* The regex pattern `r'\(([^)]+)\)([\+\-\*\/])\(([^)]+)\)'` dynamically isolates the first operand, the arithmetic operator, and the second operand into exact capture groups.

## 3. Mathematical Implementation
* **Object Casting:** Extracted string operands are safely cast directly to Python's native `complex()` objects, inherently supporting the required $a+bj$ mathematical representation.
***Core Arithmetic:** Standard Python overloaded operators (`+`, `-`, `*`, `/`) handle the required addition, subtraction, multiplication, and division operations.
* **Advanced Computations:** Standard mathematical libraries are utilized for complex plane metrics.
    * **Magnitude:** Calculated using the built-in `abs(z)` function to efficiently compute $\sqrt{a^2 + b^2}$.
    * **Phase:** Computed using `cmath.phase(z)` to guarantee accurate quadrant mapping and return the angle in radians.
* **Output Formatting:** Raw mathematical results are dynamically reformatted back into the strictly required `a+bj` string notation before being returned to the main process.

## 4. Error Handling & Validation
* **Syntax Validation:** The regex parser acts as the first line of defense. Unmatched patterns or invalid characters raise an immediate `ValueError`.
* **Boundary Conditions:** A programmatic check intercepts mathematical impossibilities, such as dividing by `(0+0j)`, raising a descriptive exception to prevent catastrophic system crashes.