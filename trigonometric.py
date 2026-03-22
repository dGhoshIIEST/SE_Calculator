import math
class Trignometry:
    def sin_deg(self,x):
        try:
            x = float(x)
            return math.sin(math.radians(x))
        except Exception:
            raise ValueError("Invalid input for sin")
    
    def cos_deg(self,x):
        try:
            x = float(x)
            return math.cos(math.radians(x))
        except Exception:
            raise ValueError("Invalid input for cos")


    def tan_deg(self,x):
        try:
            x = float(x)
            return math.tan(math.radians(x))
        except Exception:
            raise ValueError("Invalid input for tan")


    def asin_deg(self,x):
        try:
            x = float(x)
            if x < -1 or x > 1:
                raise ValueError("asin input must be between -1 and 1")
            return math.degrees(math.asin(x))
        except ValueError as e:
            if str(e) == "asin input must be between -1 and 1":
                raise e
            raise ValueError("Invalid input for asin")


    def acos_deg(self,x):
        try:
            x = float(x)
            if x < -1 or x > 1:
                raise ValueError("acos input must be between -1 and 1")
            return math.degrees(math.acos(x))
        except ValueError as e:
            if str(e) == "acos input must be between -1 and 1":
                raise e
            raise ValueError("Invalid input for acos")


    def atan_deg(self,x):
        try:
            x = float(x)
            return math.degrees(math.atan(x))
        except Exception:
            raise ValueError("Invalid input for atan")


    def sinh_val(self,x):
        try:
            x = float(x)
            return math.sinh(x)
        except Exception:
            raise ValueError("Invalid input for sinh")


    def cosh_val(self,x):
        try:
            x = float(x)
            return math.cosh(x)
        except Exception:
            raise ValueError("Invalid input for cosh")


    def tanh_val(self,x):
        try:
            x = float(x)
            return math.tanh(x)
        except Exception:
            raise ValueError("Invalid input for tanh")

