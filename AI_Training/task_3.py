number = int(input('Enter the number :')) # takes number from the user 

if(number %2 == 0): # %2 == 0 is used to check whether number is even
    print('The number is even')

elif(number %2 != 0): # %2 != 0 is used to check whether number is odd

    print('The number is odd')

else: # runs when if condition if false
    print('Invalid number')    