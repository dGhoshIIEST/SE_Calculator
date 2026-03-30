import math

try:
    from ..exceptions import DomainError
except ImportError:
    from exceptions import DomainError

class Trigonometric:

    def to_radians(self, x):
        return math.radians(float(x))

    def sin(self, x):
        return math.sin(self.to_radians(x))

    def cos(self, x):
        return math.cos(self.to_radians(x))

    def tan(self, x):
        x = float(x)

          # tan is undefined at 90 + k*180
        if x % 180 == 90:
           raise ValueError("tan undefined at 90 + k*180")

        return math.tan(self.to_radians(x))

    def asin(self, x):
        x = float(x)
        if x < -1 or x > 1:
            raise DomainError("asin domain is [-1,1]")
        return math.degrees(math.asin(x))

    def acos(self, x):
        x = float(x)
        if x < -1 or x > 1:
            raise DomainError("acos domain is [-1,1]")
        return math.degrees(math.acos(x))

    def asin_value(self, x):
        return math.degrees(math.asin(float(x)))

    def acos_value(self, x):
        return math.degrees(math.acos(float(x)))

    def atan(self, x):
        return math.degrees(math.atan(float(x)))

    def sinh(self, x):
        return math.sinh(float(x))

    def cosh(self, x):
        return math.cosh(float(x))

    def tanh(self, x):
        return math.tanh(float(x))
    