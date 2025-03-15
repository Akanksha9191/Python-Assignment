# 7. Python program to calculate the sum of all numbers from 1 to 20.
sum = 0
for i in range(1, 21):
    sum = sum + i
print(sum)

# 8. Python program to print a multiplication table of a given number. 
num = int(input("Enter a number: "))
for table in range(1, 10+1):
    print(table * num)

# 9. Python program to count the total number of digits in a number. 
num1 = int(input("Enter a number : "))
sum =0
while(num1>0):
    remainder = num1 % 10
    sum = sum + remainder
    num1 = num1 //10
print("Sum of total number of digit= ", sum)    
# 10. Write a Python program that prompts the user to enter a number and evaluates it based on the 
# following conditions:  (use nested if-else) 
#  If the number is 55 or less, display "Number is less or equal to 55". 
#  If the number is greater than 45, display "Number is above 45". Otherwise, display "Number 
# is below 45". 
#  If the number is greater than 55, display "Number is greater than 55".

number = int(input("Enter a number = "))

if(number<55):
    if(number>45):
        print("Number is above 45")
    else:
        print("Number is below 45")
    if(number>55):
        print("Number is greater than 55")
else:
    print("Invalid number")
    