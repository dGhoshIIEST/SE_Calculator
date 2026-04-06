class CalculatorError(Exception):
    """Base exception for calculator errors."""


class InvalidMatrixError(CalculatorError):
    """Raised when a matrix input is malformed."""


class MatrixDimensionError(CalculatorError):
    """Raised when matrix dimensions are incompatible for an operation."""
