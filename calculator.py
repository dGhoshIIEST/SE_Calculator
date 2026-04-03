class Calculator:
    # mode can be 1: Fraction, 2: Bin, 3: Oct, 4: Hex, 5: Set, 6: Matrix, default  = 0
    mode = 0
    
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero")
        return a / b

    def evaluate(mode = 0):
        #check the mode and based on its values execute for different mode
        print('evaluate method to extend for multiple derived classes')
