num1 = int(input('The first number is :')) # takes input from the user
num2 = int(input('The second number is :')) # takes input from the user
operator = input('Enter the operator (+,-,*,/) : ') # takes input from the user

if(operator == '+'): # addition operator
    print(num1 + num2)

elif(operator == '-'): # subtraction operator
    print(num1 - num2)

elif(operator == '*'): # multiplication operator
    print(num1 * num2)

elif(operator == '/'): # division operator
    if num2 != 0:
        print(num1 / num2)
    else:
        print('Number not divisible by zero')    

else: # runs when if condition is false
    print('Invalid operator')