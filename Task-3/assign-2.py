# 6. Define a function is_palindrome(s) that checks if a given string is a palindrome.
def is_palindrome(s):
    str1 = ''.join(reversed(s))
    return str1 == s
 
# 7. Create a function sum_of_list(lst) that returns the sum of all elements in a given list.
def sum_of_list(lst):
    sum = 0
    for i in lst:
        sum = sum + i
    return sum
    
# 8. Implement a function unique_elements(lst) that returns a list with only unique elements from the input list.
print()
def unique_elements(lst):
    return set(lst)
def main():
    # 6
    string = input("Enter a string: ")
    result = is_palindrome(string)
    print(f"Give {string} string is a palindrome or not :", result)
    # 7
    user_lst = []
    size = int(input("Enter a size : "))
    print("enter a value: ")
    
    for i in range(size):
        value = int(input())
        user_lst.append(value)
    print("User list = ", user_lst)
    
    result = sum_of_list(user_lst)
    print(f"Sum of all element of give list==> {result}")
    
    # 8
    userList = []
    size = int(input("Enter a size : "))
    print("Enter a values: ")
    
    for i in range(size):
        value = int(input())
        userList.append(value)
    print("User list = ", userList)
    
    result = unique_elements(userList)
    print(result)
if __name__ == "__main__":
    main()
    

# 9. Define a function calculate_area(shape, **kwargs) that calculates the area of different shapes (circle, rectangle, triangle) based on keyword arguments. area circle = 3.14*R*R  ar = l*w  at =1/2 *b*h
