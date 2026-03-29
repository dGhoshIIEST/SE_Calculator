## Main File we gonna edit!!

import re
# from exceptions import InvalidSetFormat

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