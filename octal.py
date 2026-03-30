
#Tejash Complement 7s and 8s (7s complement is 7 - digit for each) while 8s comp is 7s comp + 1
from validate_octal import *

def sevensComplement(octalStr):
    digits = validate_octal(octalStr) #ronak will implement
    comp = ''.join(str(7 - int(d)) for d in digits)
    return f"O'{comp}"


def eightsComplement(octalStr):
    digits = validate_octal(octalStr) #ronak will implement

    
    comp7 = [7 - int(d) for d in digits]

    
    carry = 1
    for i in range(len(comp7) - 1, -1, -1):
        temp = comp7[i] + carry
        comp7[i] = temp % 8
        carry = temp // 8

    result = ''.join(str(d) for d in comp7)
    return f"O'{result}"