a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("press (1 = Addition / 2 = Subtraction / 3 = Multiplication / 4 = Division): ")
operation = input("Enter: ")

if operation == '1':
    result = a + b
    print("The result is: {}".format(result))
elif operation == '2':
    result = a - b 
    print("The result is: {}".format(result))
elif operation == '3':
    result = a * b 
    print("The result is: {}".format(result))
elif operation == '4':
    if b != 0:
        result = a / b
        print("The result is: {}".format(result))
    else:
        print("Not Define")
else:
    print("Something went wrong. Please check your input!!!")
print("Thank you!")