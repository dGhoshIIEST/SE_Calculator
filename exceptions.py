class CalculatorError(Exception):
    """Base class for calculator-related errors."""
    pass


class InvalidExpressionError(CalculatorError):
    """Raised when the input expression is invalid."""
    pass


class DivisionByZeroError(CalculatorError):
    """Raised when division by zero is attempted."""
    pass


class DomainError(CalculatorError):
    """Raised when a trig function gets an invalid domain value."""
    pass