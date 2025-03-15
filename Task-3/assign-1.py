# 1. Write a Python function greet(name) that takes a person's name as input and returns a greeting message like "Hello, John!".

def greet(name):
    return(f"Hello, {name}!")

# 2. Define a function add_numbers(a, b) that takes two numbers as arguments and returns their sum.
print()
def add_Numbers(a, b):
    sum = a+b
    return sum
# 3. Write a function is_even(n) that returns True if n is even and False otherwise
print("")

def is_even(n):
    if(n %2 ==0):
        return True
    else:
        return False

# 4. Write a function reverse_string(s) that takes a string as input and returns the reversed string.
print()
def reverse_string(s):
    RS = ''.join(reversed(s))
    return RS

# 5. Implement a function count_vowels(s) that counts the number of vowels in a given string.

print()
def count_vowels(s):
    count = 0
    for i in s:
        if(i=="a" or i=="e" or i == "i" or i=="o"or i=='u'):
           count +=1
    return count
        
def main():
    # 1
    name = input("Enter your name: ")
    result = greet(name)
    print(result)
    
    # 2
    text = input("Enter a string : ")
    result = count_vowels(text)
    print(result)
    
    # 3
    num = int(input("Enter a number: "))
    result = is_even(num)
    print(result)
    
    # 4
    string = input("Enter a string: ")
    result = reverse_string(string)
    print(f"Reversed string of {string} == {result}")
    
    # 5
    total = add_Numbers(10, 15)
    print(f"Sum of two numbers = {total}")
    
if __name__ == "__main__":
    main()
