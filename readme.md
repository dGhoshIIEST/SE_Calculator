# Multi-Mode Calculator

A calculator system where the user must **set a mode first** and then perform operations specific to that mode.

`````md
## 🔑 Mode System

The calculator works in **mode-based execution**.

| Mode Value | Mode Name   |
| ---------- | ----------- |
| 1          | Fraction    |
| 2          | Binary      |
| 3          | Octal       |
| 4          | Hexadecimal |
| 5          | Set         |
| 6          | Matrix      |

Currently implemented: **Hexadecimal (mode = 4)**

## 🚀 Features

- Mode-based execution (`set_mode()` required)
- Modular architecture (easy to extend)
- HEX operations supported:
  - Addition, Subtraction, Multiplication, Division
  - HEX ↔ Decimal conversion
  - 15’s & 16’s complement
- Input validation & error handling

---

## 📁 Project Structure

```bash
SE_Calculator/
│
├── calculator.py # Main calculator controller (mode handler)
├── hex.py # Hexadecimal calculator implementation
├── test_calculator.py # Unit tests for calculator controller
├── test_hex.py # Unit tests for hexadecimal calculator
└── README.md # Project documentation
```

## 📒 A sample program to demonstrate how to use

```python
from calculator import Calculator

from calculator import Calculator

def main(): # Create calculator object
    calc = Calculator()

        # -------------------------------
        # Step 1: Set Mode
        # -------------------------------
        calc.set_mode(4)   # 4 = HEX mode
        print("Current Mode:", calc.get_mode())
        print("-" * 50)

        # -------------------------------
        # Arithmetic Operations
        # -------------------------------
        print("Arithmetic Operations:")
        print("H'A' + H'5'   =", calc.evaluate("add", "H'A'", "H'5'"))
        print("H'F' - H'5'   =", calc.evaluate("subtract", "H'F'", "H'5'"))
        print("H'3' * H'4'   =", calc.evaluate("multiply", "H'3'", "H'4'"))
        print("H'1A' / H'3'  =", calc.evaluate("divide", "H'1A'", "H'3'"))
        print("-" * 50)

        # -------------------------------
        # Conversion Operations
        # -------------------------------
        print("Conversion Operations:")
        print("HEX to Decimal H'1A' =", calc.evaluate("hex_to_decimal", "H'1A'"))
        print("Decimal to HEX D'26' =", calc.evaluate("decimal_to_hex", "D'26'"))
        print("-" * 50)

        # -------------------------------
        # Complement Operations
        # -------------------------------
        print("Complement Operations:")
        print("15's complement of H'A' =", calc.evaluate("fifteen_complement", "H'A'"))
        print("16's complement of H'A' =", calc.evaluate("sixteen_complement", "H'A'"))
        print("-" * 50)

        # -------------------------------
        # More HEX Examples
        # -------------------------------
        print("More HEX Examples:")
        print("H'AB' + H'CD'   =", calc.evaluate("add", "H'AB'", "H'CD'"))
        print("H'100' - H'1'   =", calc.evaluate("subtract", "H'100'", "H'1'"))
        print("H'AB' * H'CD'   =", calc.evaluate("multiply", "H'AB'", "H'CD'"))
        print("H'88EF' / H'AB' =", calc.evaluate("divide", "H'88EF'", "H'AB'"))
        print("-" * 50)

        # -------------------------------
        # Error Handling Examples
        # -------------------------------
        print("Error Handling Examples:")

        try:
            print("Trying division by zero...")
            print(calc.evaluate("divide", "H'A'", "H'0'"))
        except ValueError as e:
            print("Caught Error:", e)

        try:
            print("Trying invalid HEX input...")
            print(calc.evaluate("add", "H'G1'", "H'2'"))
        except ValueError as e:
            print("Caught Error:", e)

        try:
            print("Trying unsupported operation...")
            print(calc.evaluate("modulus", "H'A'", "H'2'"))
        except ValueError as e:
            print("Caught Error:", e)

if __name__ == "__main__":
    main()

```

````md
## Expected Output

```text
## Current Mode: 4

Arithmetic Operations:
H'A' + H'5' = H'F'
H'F' - H'5' = H'A'
H'3' \* H'4' = H'C'
H'1A' / H'3' = H'8'

---

Conversion Operations:
HEX to Decimal H'1A' = D'26'
Decimal to HEX D'26' = H'1A'

---

Complement Operations:
15's complement of H'A' = H'5'
16's complement of H'A' = H'6'

---

More HEX Examples:
H'AB' + H'CD' = H'178'
H'100' - H'1' = H'FF'
H'AB' \* H'CD' = H'88EF'
H'88EF' / H'AB' = H'CD'

---

Error Handling Examples:
Trying division by zero...
Caught Error: Division by zero
Trying invalid HEX input...
Caught Error: Invalid hexadecimal digits
Trying unsupported operation...
Caught Error: Unsupported HEX operation: modulus
```
````

````md
## 🧪 Unit Testing

This project uses Python’s built-in `unittest` framework.

### Run all tests

```bash
python -m unittest
```
````

**Run specific HEX tests**

```bash
python -m unittest test_calculator.py
```

**Run specific hex funxtions**

```bash
python -m unittest test*hex.TestHexCalculator.test*<function name> -v
```

**Run calculator tests**

```bash
python -m unittest test_calculator.py
```
`````
