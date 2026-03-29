# Set Module Usage Guide

This file explains how to use the set calculator in [set.py](set.py) and how to run its tests in [test_set.py](test_set.py).

## Supported Set Operations 

- union
- intersection
- difference
- symmetric_difference
- subset
- superset

## Input Format

Use set strings such as:

- {1, 2, 3}
- {-1, 0, 5}
- {}

**NOTE**: Only integer elements are supported.

## Usage Example

```python
from set import SetParser, SetCalculator

calc = SetCalculator()
A = SetParser.parse("{1, 2, 3}")
B = SetParser.parse("{3, 4}")

print(calc.compute("union", A, B))                 # {1, 2, 3, 4}
print(calc.compute("intersection", A, B))          # {3}
print(calc.compute("difference", A, B))            # {1, 2}
print(calc.compute("symmetric_difference", A, B))  # {1, 2, 4}
print(calc.compute("subset", {1, 2}, {1, 2, 3}))  # True
print(calc.compute("superset", {1, 2, 3}, {1, 2}))# True
```

## Run Set Tests

From project root, using **pytest**:

```powershell
python -m pytest -q test_set.py
```

Or using **unittest**:

```powershell
python -m unittest test_set.py -v
```

## Notes

- Invalid set strings raise **InvalidSetFormat**.
- Unknown operation names raise **UnsupportedOperation**.
- Operation names are **case-insensitive**.
