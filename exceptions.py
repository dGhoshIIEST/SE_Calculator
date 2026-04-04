class calculatorerror(Exception):
    def __init__(self, msg="calculator error"):
        self.msg = msg
        super().__init__(self.msg)

class invalidinputerror(calculatorerror):
    def __init__(self, msg="invalid input"):
        super().__init__(msg)

class zerodenominatorerror(calculatorerror):
    def __init__(self, msg="denominator cannot be zero"):
        super().__init__(msg)

class invalidfractionerror(calculatorerror):
    def __init__(self, msg="invalid fraction format"):
        super().__init__(msg)

class invalidcomplexerror(calculatorerror):
    def __init__(self, msg="invalid complex number"):
        super().__init__(msg)

class invalidbinaryerror(calculatorerror):
    def __init__(self, msg="invalid binary number"):
        super().__init__(msg)

class invalidoctalerror(calculatorerror):
    def __init__(self, msg="invalid octal number"):
        super().__init__(msg)

class invalidhexerror(calculatorerror):
    def __init__(self, msg="invalid hex number"):
        super().__init__(msg)

class invalidseterror(calculatorerror):
    def __init__(self, msg="invalid set format"):
        super().__init__(msg)

class invalidmatrixerror(calculatorerror):
    def __init__(self, msg="invalid matrix format"):
        super().__init__(msg)

class dimensionmismatcherror(calculatorerror):
    def __init__(self, msg="matrix dimensions dont match"):
        super().__init__(msg)

class undefinedoperationerror(calculatorerror):
    def __init__(self, msg="operation is undefined"):
        super().__init__(msg)
