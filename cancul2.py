def calculator (num1, num2, operator):
 if operator == "+":
    print (num1+num2)
 elif operator == "-":
    print (num1-num2 )
 elif operator == "*":
    print (num1*num2 )
 elif operator == "/":
    print (num1/num2 )
 elif operator == "%":
    print (num1*num2/100 )
 elif operator == "^":
    print (num1**num2 )
 else:
     print("Неверная операция")

calculator(4,9, "*")