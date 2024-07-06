def calculator():
    try:
        a=float(input("enter the value of a:"))
        b=float(input("enter the value of b:"))
        operator=input("enter the operation to be performed,(+,-,*,/,%):")
        if operator == '+':
            result=a+b
        elif operator == '-':
            result=a-b
        elif operator == '*':
            result=a*b
        elif operator == '/':
            result=a/b
        elif operator == '%':
            result=a%b
        else:
            result='invalid'
        print(a,operator,b, "is",result)
    except ZeroDivisionError:
        print("you cannot divide by zero")
    except ValueError:
        print("enter only numbers")
calculator()
