# Program to perform arithmetic operations (+, -, *, /) using functions.
def func(a, b, c):
    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    elif c == '*':
        return a * b
    elif c == '/':
        return a / b


a = int(input())
b = int(input())
c = input()
print(func(a, b, c))
