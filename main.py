from calculator import Calculator

calc = Calculator()
expression = input("Enter expression : ")
result = calc.calculate(expression)
print(f"Result: {result}")