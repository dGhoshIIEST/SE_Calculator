## Main File we gonna edit!!

import re
from exceptions import InvalidSetFormat
from abc import ABC, abstractmethod


class SetParser:
    SET_PATTERN = r"^\{\s*(-?\d+\s*(,\s*-?\d+\s*)*)?\}$"

    @staticmethod
    def parse(input_str: str) -> set:

        if not re.match(SetParser.SET_PATTERN, input_str):
            raise InvalidSetFormat("Invalid set format")

        cleaned = input_str.strip("{} ")

        if cleaned == "":
            return set()

        elements = cleaned.split(",")

        return {int(e.strip()) for e in elements}


class SetOperation(ABC):

    @abstractmethod
    def execute(self, A: set, B: set):
        pass

class UnionOperation(SetOperation):

    def execute(self, A, B):
        return A.union(B)

class IntersectionOperation(SetOperation):

    def execute(self, A, B):
        return A.intersection(B)


class SubsetOperation(SetOperation):

    def execute(self, A, B):
        return A.issubset(B)


class SupersetOperation(SetOperation):

    def execute(self, A, B):
        return A.issuperset(B)
    
class DifferenceOperation(SetOperation):

    def execute(self, A, B):
        return A.difference(B)
    
class SymmetricDifferenceOperation(SetOperation):

    def execute(self, A, B):
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

    def compute(self, operation, A, B):

        if operation not in self.operations:
            raise ValueError("Unsupported set operation")

        result = self.operations[operation].execute(A, B)

        return SetFormatter.format(result)