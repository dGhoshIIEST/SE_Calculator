# expression_parser.py

import re
from arithmetic import *

precedence = {
    '+': 1, '-': 1,
    '*': 2, '/': 2, '%': 2,
    '**': 3
}

ops = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
    '%': modulo,
    '**': power
}

functions = {
    'sqrt': sqrt,
    'cbrt': cbrt,
    'log': log,
    'floor': floor,
    'ceil': ceil,
}

def tokenize(expr):
    expr = expr.replace(" ", "")
    return re.findall(r'\d+\.?\d*|\*\*|[()+\-*/%]|[a-zA-Z]+|!', expr)

def to_postfix(tokens):
    output = []
    stack = []

    for token in tokens:
        if re.match(r'\d', token):
            output.append(token)

        elif token in functions:
            stack.append(token)

        elif token == '!':
            output.append(token)

        elif token in ops:
            while (stack and stack[-1] in ops and
                   precedence[token] <= precedence[stack[-1]]):
                output.append(stack.pop())
            stack.append(token)

        elif token == '(':
            stack.append(token)

        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
            if stack and stack[-1] in functions:
                output.append(stack.pop())

    while stack:
        output.append(stack.pop())

    return output

def evaluate_postfix(postfix):
    stack = []

    for token in postfix:
        if re.match(r'\d', str(token)):
            stack.append(token)

        elif token == '!':
            a = stack.pop()
            stack.append(factorial(a))

        elif token in ops:
            b = stack.pop()
            a = stack.pop()
            result = ops[token](a, b)   # returns string
            stack.append(result)

        elif token in functions:
            a = stack.pop()
            result = functions[token](a)
            stack.append(result)

    return stack[0]

def evaluate_expression(expr):
    tokens = tokenize(expr)
    postfix = to_postfix(tokens)
    result = evaluate_postfix(postfix)

    # FINAL conversion → number (for your tests)
    return float(result) if '.' in result else int(result)

