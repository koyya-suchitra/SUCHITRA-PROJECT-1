def calculator():
   a=float(input("enter the vlue of a:"))
   b=float(input("enter the value ofb:"))
   operator=input("enter the operation to be performed-(+,-,*,/,%):")
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
calculator()