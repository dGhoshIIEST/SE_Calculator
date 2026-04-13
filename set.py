import re
from abc import ABC, abstractmethod

# Exception Handling
class CalculatorError(Exception):
    """
    Base class for all calculator-related exceptions.
    """
    pass

class InvalidSetFormat(CalculatorError):
    """
    Exception raised when a string does not conform to
    the expected set input format.
    """

    def __init__(self, message: str = "Invalid set format provided.") -> None:
        super().__init__(message)


class UnsupportedOperation(CalculatorError):
    """
    Exception raised when an unsupported set operation
    is requested.
    """

    def __init__(self, operation: str) -> None:
        message = f"Operation '{operation}' is not supported."
        super().__init__(message)


# Basic Classes for implementation of Set Operations

class SetParser:
    '''
    Parser for set input strings. It validates the format and converts
    them into Python sets of integers.
    '''
    SET_PATTERN = r"^\{\s*(-?\d+\s*(,\s*-?\d+\s*)*)?\}$"

    @staticmethod
    def parse(input_str: str) -> set:

        input_str = input_str.strip()

        if not re.fullmatch(SetParser.SET_PATTERN, input_str):
            raise InvalidSetFormat(f"Invalid set format: {input_str}")

        cleaned = input_str.strip("{} ")

        if cleaned == "":
            return set()

        elements = cleaned.split(",")

        return {int(e.strip()) for e in elements}

class SetFormatter:
    '''
    Formatter for set results. It converts Python sets of integers
    into the expected string format for output.
    '''
    @staticmethod
    def format(result):

        if isinstance(result, bool):
            return result

        return "{" + ", ".join(map(str, sorted(result))) + "}"

class SetOperation(ABC):
    '''
    Abstract base class for set operations. Each specific operation
    (union, intersection, etc.) will override the execute method accordingly.
    '''
    @abstractmethod
    def execute(self, A: set[int], B: set[int]) -> set[int] | bool:
        """
        Perform operation on two sets.
        """
        raise NotImplementedError

# Set Operations
class UnionOperation(SetOperation):
    '''
    Perform the union of two sets A and B.
    '''
    def execute(self, A: set[int], B: set[int]) -> set[int]:
        return A.union(B)

class IntersectionOperation(SetOperation):
    '''
    Perform the intersection of two sets A and B.
    '''
    def execute(self, A: set[int], B: set[int]) -> set[int]:
        return A.intersection(B)


class SubsetOperation(SetOperation):
    '''
    Checks if set A is a subset of set B.
    '''
    def execute(self, A: set[int], B: set[int]) -> bool:
        return A.issubset(B)


class SupersetOperation(SetOperation):
    '''
    Checks if set A is a superset of set B.
    '''
    def execute(self, A: set[int], B: set[int]) -> bool:
        return A.issuperset(B)
    
class DifferenceOperation(SetOperation):
    '''
    Performs the difference of two sets A and B  as (A - B).
    '''
    def execute(self, A: set[int], B: set[int]) -> set[int]:
        return A.difference(B)
    
class SymmetricDifferenceOperation(SetOperation):
    '''
    Performs the symmetric difference of two sets A and B as (A Δ B).
    '''
    def execute(self, A: set[int], B: set[int]) -> set[int]:
        return A.symmetric_difference(B)
    
# Main Set Calculator Class
# whose instance will be used for set operations
class SetCalculator:

    def __init__(self):

        self.operations = {
            "union": UnionOperation(),
            "intersection": IntersectionOperation(),
            "difference": DifferenceOperation(),
            "symmetric_difference": SymmetricDifferenceOperation(),
            "subset": SubsetOperation(),
            "superset": SupersetOperation()
        }

    def compute(self, operation: str, A: set[int], B: set[int]):
        '''
        Compute the result of the specified operation on sets A and B.
        Returns the formatted result, or raises an exception if the operation is unsupported.
        '''
        operation = operation.lower()
        if operation not in self.operations:
            raise UnsupportedOperation(operation)

        result = self.operations[operation].execute(A, B)
        return SetFormatter.format(result)
    
'''
Sample Usage : 
if __name__ == "__main__":
    calc = SetCalculator()
    A = SetParser.parse("{1, 2, 3}")
    B = SetParser.parse("{3, 4}")

    print(calc.compute("union", A, B))                # Output: "{1, 2, 3, 4}"
    print(calc.compute("intersection", A, B))         # Output: "{3}"
    print(calc.compute("difference", A, B))           # Output: "{1, 2}"
    print(calc.compute("symmetric_difference", A, B)) # Output: "{1, 2, 4}"
    print(calc.compute("subset", {1, 2}, {1, 2, 3})) # Output: True
    print(calc.compute("superset", {1, 2, 3}, {1, 2})) # Output: True   
'''