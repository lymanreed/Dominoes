x = float(input())
y = float(input())
op = input()

if op in ('/', 'mod', 'div') and y == 0:
    print('Division by 0!')
elif op == '+':
    print(x + y)
elif op == '-':
    print(x - y)
elif op == '/':
    print(x / y)
elif op == '*':
    print(x * y)
elif op == 'mod':
    print(x % y)
elif op == 'pow':
    print(x ** y)
elif op == 'div':
    print(x // y)
