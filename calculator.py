class Calculator:
    # mode can be 1: Fraction, 2: Bin, 3: Oct, 4: Hex, 5: Set, 6: Matrix, default  = 0
    mode = 0
    def evaluate(self, a, b, mode = 0):
        #check the mode and based on its values execute for different mode
        print('evaluate method to extend for multiple derived classes')

        if (mode == 1) :
            pass
        elif (mode == 2) :
            pass
        elif (mode == 3) :
            pass
        elif (mode == 4) :
            pass
        elif (mode == 5) :  # Set mode
            self.set_operations(a, b)
        elif (mode == 6) :
            pass


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
    
    # Set operations driver function
    def set_operations(self, a, b) :
        from set import SetParser, SetCalculator
        from set import UnsupportedOperation
        
        set_calc = SetCalculator()
        parser = SetParser()

        A = parser.parse(a)
        B = parser.parse(b)

        print("Enter set operation to perform\n" \
        "1. Union\n" \
        "2. Intersection\n" \
        "3. Difference\n" \
        "4. Symmetric Difference\n"
        "5. Subset\n" \
        "6. Superset\n")
        choice = int(input("Enter Choice : "))

        if (choice == 1) :
            return set_calc.compute("union", A, B)
        elif (choice == 2) :
            return set_calc.compute("intersection", A, B)
        elif (choice == 3) :
            return set_calc.compute("difference", A, B)
        elif (choice == 4) :
            return set_calc.compute("symmetric_difference", A, B)
        elif (choice == 5) :
            return set_calc.compute("subset", A, B)
        elif (choice == 6) :
            return set_calc.compute("superset", A, B)
        else :
            raise UnsupportedOperation(str(choice))
