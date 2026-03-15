# Set Operations Module — Design & Development Roadmap

## 1. Overview

This module implements **set operations** for the calculator system.
It allows users to perform operations such as:

* Union
* Intersection
* Difference
* Symmetric Difference
* Subset check
* Superset check

The module accepts **string-based set input**, for example:

```
{1, 2, 5}
```

This string is parsed and converted into an internal set representation before performing operations.

The goal is to implement the module using **clean OOP design, modular architecture, and proper testing**, ensuring seamless integration with the overall calculator system.

---

# 2. Objectives

The module must satisfy the following:

### Functional Requirements

1. Parse set input strings
2. Perform core set operations
3. Validate input format
4. Produce readable output
5. Integrate with calculator mode system

### Non-Functional Requirements

* Modular architecture
* Object-oriented design
* Maintainability
* Extensibility
* Unit test coverage

---

# 3. Module Placement in Project

The module will be implemented inside:

```
set.py
```

with testing in:

```
test_set.py
```

### Project Structure Context

```
calculator_system
│
├── calculator.py
├── arithmetic.py
├── fraction.py
├── complex.py
├── trigonometric.py
├── bitwise.py
├── binary.py
├── octal.py
├── hex.py
├── set.py
├── matrix.py
├── exceptions.py
│
├── test_set.py
```

---

# 4. High Level Workflow

User → Calculator → Set Module → Result

### Workflow Steps

1. User enables **Set Mode**
2. User inputs set expressions
3. Parser converts string → Python set
4. Operation class executes set operation
5. Formatter prepares output
6. Result returned to calculator

---

# 5. System Architecture

The module follows a **layered architecture**.

```
            +-------------------+
            |   Calculator UI   |
            +---------+---------+
                      |
                      v
            +-------------------+
            |   SetCalculator   |
            | (operation router)|
            +---------+---------+
                      |
        +-------------+--------------+
        |                            |
        v                            v
+--------------+             +----------------+
|   SetParser  |             | SetOperations  |
| (input parse)|             | (core logic)   |
+--------------+             +----------------+
        |
        v
+--------------+
| SetFormatter |
+--------------+
```

---

# 6. UML Class Diagram

```
                   +------------------+
                   |   SetCalculator  |
                   +------------------+
                   | operations dict  |
                   +------------------+
                           |
          ------------------------------------------
          |            |           |               |
          v            v           v               v

+---------------+ +---------------+ +---------------+ +---------------+
| UnionOperation| |IntersectOper. | |DifferenceOper.| |SymDiffOper.   |
+---------------+ +---------------+ +---------------+ +---------------+
| execute()     | | execute()     | | execute()     | | execute()     |
+---------------+ +---------------+ +---------------+ +---------------+

                All inherit from

                +----------------+
                |  SetOperation  |
                +----------------+
                | execute()      |
                +----------------+

Additional Utility Classes

+-------------+
| SetParser   |
+-------------+
| parse()     |
+-------------+

+-------------+
|SetFormatter |
+-------------+
| format()    |
+-------------+
```

---

# 7. Component Responsibilities

### SetParser

Responsible for converting user input into a valid set.

Example:

```
Input  : "{1,2,3}"
Output : {1,2,3}
```

Responsibilities:

* Remove braces
* Split elements
* Convert to integers
* Handle empty sets

---

### SetOperation (Abstract Base Class)

Defines the common interface for all operations.

```
execute(A, B)
```

This ensures **consistent operation behavior** across all subclasses.

---

### Operation Classes

Each operation is implemented as a separate class.

Examples:

```
UnionOperation
IntersectionOperation
DifferenceOperation
SymmetricDifferenceOperation
SubsetOperation
SupersetOperation
```

Each class implements:

```
execute(A, B)
```

---

### SetCalculator

Acts as the **operation controller**.

Responsibilities:

* Receive operation request
* Select correct operation class
* Execute operation
* Return formatted result

---

### SetFormatter

Formats output for display.

Example:

```
Internal: {3,1,2}
Output  : {1,2,3}
```

---

# 8. Data Flow Diagram

```
User Input
   |
   v
+-----------+
| Calculator|
+-----------+
      |
      v
+-----------+
| SetParser |
+-----------+
      |
      v
+---------------+
| SetCalculator |
+---------------+
      |
      v
+------------------+
| SetOperation     |
| (Union/Inter...) |
+------------------+
      |
      v
+-------------+
| Formatter   |
+-------------+
      |
      v
  Final Output
```

---

# 9. Supported Operations

| Operation            | Symbol | Example                 |
| -------------------- | ------ | ----------------------- |
| Union                | A ∪ B  | {1,2} ∪ {2,3} = {1,2,3} |
| Intersection         | A ∩ B  | {1,2} ∩ {2,3} = {2}     |
| Difference           | A − B  | {1,2,3} − {2} = {1,3}   |
| Symmetric Difference | A △ B  | {1,2} △ {2,3} = {1,3}   |
| Subset               | A ⊆ B  | {1,2} ⊆ {1,2,3}         |
| Superset             | A ⊇ B  | {1,2,3} ⊇ {1,2}         |

---

# 10. Error Handling

The module should handle the following errors:

| Error                | Description         |
| -------------------- | ------------------- |
| InvalidSetFormat     | Incorrect set input |
| UnsupportedOperation | Unknown operation   |
| Empty input          | Missing elements    |

Custom exceptions should be implemented in:

```
exceptions.py
```

---

# 11. Unit Testing Plan

Testing will be implemented using **Python unittest**.

Test file:

```
test_set.py
```

### Test Categories

| Test Type            | Example         |
| -------------------- | --------------- |
| Parsing              | "{1,2,3}"       |
| Empty set            | "{}"            |
| Union                | {1,2} ∪ {2,3}   |
| Intersection         | {1,2} ∩ {2,3}   |
| Difference           | {1,2,3} - {2}   |
| Symmetric Difference | {1,2} △ {2,3}   |
| Subset check         | {1,2} ⊆ {1,2,3} |
| Superset check       | {1,2,3} ⊇ {1,2} |
| Invalid input        | "{1,,2}"        |

---

# 12. Development Roadmap

### Phase 1 — Requirement Analysis

* Define supported operations
* Define input format
* Define error cases

### Phase 2 — Design

* Design architecture
* Create UML diagrams
* Define class responsibilities

### Phase 3 — Implementation

* Implement SetParser
* Implement operation classes
* Implement SetCalculator

### Phase 4 — Testing

* Write unit tests
* Validate edge cases

### Phase 5 — Integration

* Connect with calculator mode system

---

# 13. Example Usage

```
A = "{1,2,3}"
B = "{3,4}"

Operation: union

Result: {1,2,3,4}
```

---

# 14. Future Extensions

The architecture allows easy addition of new operations such as:

* Power set
* Cartesian product
* Disjoint set check
* Set size
* Membership test

Only a new **operation class** needs to be added.

---

# 15. Advantages of This Design

* Clean OOP architecture
* Modular and scalable
* Easy to extend
* Well testable
* Suitable for team development

---

# 16. Conclusion

This module will implement **robust and extensible set operations** within the calculator system using a structured development process and object-oriented design.

The architecture ensures that the module is **maintainable, scalable, and easily testable**, aligning with good software engineering practices.
