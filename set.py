## Main File we gonna edit!!

import re
from abc import ABC, abstractmethod

class CalculatorError(Exception):
    """
    Base class for all calculator-related exceptions.

    This allows catching all custom exceptions using:
        except CalculatorError:
            ...
    """
    pass

class InvalidSetFormat(CalculatorError):
    """
    Exception raised when a string does not conform to
    the expected set input format.

    Expected format:
        "{1, 2, 3}"

    Examples of invalid formats:
        "{1,,2}"
        "{a, b}"
        "1,2,3"
    """

    def __init__(self, message: str = "Invalid set format provided.") -> None:
        super().__init__(message)


class UnsupportedOperation(CalculatorError):
    """
    Exception raised when an unsupported set operation
    is requested.

    Example:
        compute("invalid_operation", A, B)
    """

    def __init__(self, operation: str) -> None:
        message = f"Operation '{operation}' is not supported."
        super().__init__(message)


class SetParser:
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


class SetOperation(ABC):

    @abstractmethod
    def execute(self, A: set[int], B: set[int]) -> set[int]:
        """
        Perform operation on two sets.
        """
        raise NotImplementedError

class UnionOperation(SetOperation):

    def execute(self, A: set[int], B: set[int]) -> set[int]:
        return A.union(B)

class IntersectionOperation(SetOperation):

    def execute(self, A: set[int], B: set[int]) -> set[int]:
        return A.intersection(B)


class SubsetOperation(SetOperation):

    def execute(self, A: set[int], B: set[int]) -> set[int]:
        return A.issubset(B)


class SupersetOperation(SetOperation):

    def execute(self, A: set[int], B: set[int]) -> set[int]:
        return A.issuperset(B)
    
class DifferenceOperation(SetOperation):

    def execute(self, A: set[int], B: set[int]) -> set[int]:
        return A.difference(B)
    
class SymmetricDifferenceOperation(SetOperation):

    def execute(self, A: set[int], B: set[int]) -> set[int]:
        return A.symmetric_difference(B)
    

class SetFormatter:

    @staticmethod
    def format(result):

        if isinstance(result, bool):
            return result

        return "{" + ", ".join(map(str, sorted(result))) + "}"
    

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

        operation = operation.lower()
        
        if operation not in self.operations:
            raise UnsupportedOperation(operation)

        result = self.operations[operation].execute(A, B)

        return SetFormatter.format(result)