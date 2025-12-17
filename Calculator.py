def Calculator(a,b,op):
    match op:
        case '+':
            return a+b
        case '-':
            return a-b
        case '*':
            return a*b
        case '/':
            if b==0:
                return None
            return a/b
        case _:
            return "Invalid Operator"

while(True):
    print("Enter Your operator: +, -, *, /")
    print("Enter q for Exiting Calculator")
    op = input("Enter your Operator: ").strip()

    if op=='q':
        print("Exiting Calculator")
        break

    if op not in ['+', '-', '*', '/']:
        print("Invalid Operator")
        continue

    a = float(input("Enter Your First Number: "))
    b = float(input("Enter Your Second Number: "))

    Answer = Calculator(a,b,op)
    if Answer is None:
        print("Error in Calculation")
    else:
        print("Result:" , Answer)