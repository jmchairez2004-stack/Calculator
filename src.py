import operations
while True:
    print("Welcome to your calculator app!")
    print("Where you can add/divide/substract/multiply/exponent")
    print("if you are done with your operations just enter [q] to close")
    op=input("Please enter your operation:\n")
    if(op.lower() == "q"):
        print("Thank you for using the calculator")
        break

    if(op.find("+")!=-1):
        num1, num2 = operations.split(op, op.find("+"))
        print(f"The answer to {op} is: {operations.add(num1,num2)}")


    elif(op.find("-")!=-1):
        num1, num2 = operations.split(op, op.find("-"))
        print(f"The answer to {op} is: {operations.sub(num1,num2)}")

    elif(op.find("/")!=-1):
        num1, num2 = operations.split(op, op.find("/"))
        print(f"The answer to {op} is: {operations.div(num1,num2)}")

    elif(op.find("*")!=-1):
        num1, num2 = operations.split(op, op.find("*"))
        print(f"The answer to {op} is: {operations.mult(num1,num2)}")


    elif(op.find("^")!=-1):
        num1, num2 = operations.split(op, op.find("^"))
        print(f"The answer to {op} is: {operations.exp(num1,num2)}")
    else:
        print("Error: operation not suported")
        print("try: (+,-,*,/,^)")
    
