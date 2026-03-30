class CalculatorError(Exception):
    """Base Calculator Exceptions"""
    pass

class InvalidInputError(CalculatorError):
    """Raised when Input is Invalid"""
    def __init__(self,message="Invalid Input"):
        super().__init__(message)

class InvalidFormatError(CalculatorError):
    """Raised when Fraction Format is Invalid"""
    def __init__(self,message="Invalid Format"):
        super().__init__(message)

class InvalidFractionError(CalculatorError):
    """Raised when Fraction is Invalid"""
    def __init__(self,message="Invalid Fraction"):
        super().__init__(message)
