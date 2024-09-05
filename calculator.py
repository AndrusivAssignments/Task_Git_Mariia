def calculator(): 
    expression = input('Calculate: ')
    to_calculate = expression.replace('', ' ').split()
    
    num1 = float(to_calculate[0])
    num2 = float(to_calculate[-1])

    for symbol in to_calculate: 
        if symbol == '+': 
            return num1 + num2 
        elif symbol == '-':
            return num1 - num2
        elif symbol == '*': 
            return num1 * num2
        elif symbol == '/':
            return num1 / num2
    else:
        print("Invalid operator")
        return None
print(calculator())
