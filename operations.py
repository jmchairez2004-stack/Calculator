def split(op, numIn):
    stnum1 =op[0:numIn].strip()
    stnum2 =op[numIn+1:].strip()

    num1 =float(stnum1)
    num2 = float(stnum2)

    return num1,num2

def add(num1, num2):
    return num1+num2


def sub(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    if(num2==0):
        return print("Error: Division by 0")
    return num1/num2

def exp(num1, num2):
    return num1**num2