def calculator(x, y, operator):
    if operator == '+':
        return x + y
    elif operator == '-':
        return x - y
    elif operator == '*':
        return x * y
    elif operator == '/':
        return x / y
    else:
        return 'invalid operator'
    
print(calculator(5,5,"+"))    