print("1: + ")
print("2: - ")
print("3: * ")
print("4: / ")
calc = int(input("Enter number: "))

if (1 <= calc <= 4):
    num1, num2 = map(int, input("Enter two number.: ").split())

    if(calc == 1):
        print(num1, ' + ', num2, ' = ', num1 + num2)

    elif(calc == 2):
        print(num1, ' - ', num2, ' = ', num1 - num2)

    elif(calc == 3):
        print(num1, ' * ', num2, ' = ', num1 * num2)

    elif(calc == 4):
        print(num1, ' / ', num2, ' = ', num1 / num2)
    
    
else : 
    print("Wrong input")  
    