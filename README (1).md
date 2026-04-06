# Group B - Feature 10 - Matrix Operations

This submission implements **Feature 10** from the Software Engineering calculator assignment.

## Scope covered
- Row-major matrix input parsing from string
- Matrix addition
- Matrix subtraction
- Matrix multiplication
- Matrix transpose
- Dimension compatibility checks
- Invalid input handling
- Unit tests for normal, boundary, and invalid cases

## Files
- `calculator.py` - base calculator plus dispatch for matrix mode
- `matrix.py` - matrix parsing and matrix operations
- `exceptions.py` - custom exceptions for matrix errors
- `test_calculator.py` - base arithmetic tests
- `test_matrix.py` - matrix feature tests

## Matrix mode
Mode `6` is used for matrix operations.

### Supported inputs
- `[[1,2],[3,4]]`
- `[[1,2],[3,4]] + [[5,6],[7,8]]`
- `[[1,2],[3,4]] - [[5,6],[7,8]]`
- `[[1,2],[3,4]] * [[5,6],[7,8]]`
- `transpose([[1,2,3],[4,5,6]])`

## Run tests
```bash
python -m unittest test_calculator.py test_matrix.py -v
```

## Run program
```bash
python calculator.py
```
