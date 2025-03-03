# Write a Python program to find those numbers which are divisible by 7 and 5, between range 1500 and  
# 2700 (both included). -> Create an empty list to store numbers that meet the given conditions. 
lst = []
for i in range(1500, 2700):
    if(i % 5 ==0 and i % 7 ==0):
        lst.append(i)
print(lst)


# 11. Write a Python program that displays a menu with three options: 
# 1. Addition 
# 2. Subtraction 
# 3. Multiplication
# The user should select an option (1, 2, or 3) and input two numbers. The program should then perform the selected 
# operation and display the result. If the user enters an invalid option, display an error message. (use if-elif-else ladder 
# only)
print()
menu = int(input("Enter a option: "))

if(menu == 1):
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number: "))
    print("Addition of two numbers: ", num1+num2)
elif(menu == 2 ):
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number: "))
    print("Substraction of two numbers: ", num1 - num2)
elif(menu == 3):
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number: "))
    print("Multiplication of two numbers : ", num1*num2)
else:
    print("Invalid Option")
    
    