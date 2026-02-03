a=float(input("Введите первое число:  "))
b=float(input("Введите второе число:  "))
m=input("Введите +,-,*,/,%,^: ")
def add(a, b):
        return a+b
def sub(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a, b):
    if b != 0:
        return a/b
    else:
        return"На ноль делить нельзя"
def percent(a, b):
    return a*b/100
def power(a, b):
    return a**b

if m == "+":
    result = add(a, b)
elif m == "-":
    result = sub(a, b)
elif m == "*":
    result = mul(a, b)
elif m == "/":
    result = div(a, b)
elif m == "%":
    result = percent(a, b)
elif m == "^":
    result = power(a, b)
else:
    result = "Неверная операция"

print (" Ответ:", result )
