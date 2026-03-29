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