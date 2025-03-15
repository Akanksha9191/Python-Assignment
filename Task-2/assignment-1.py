x = 5
while x > 0:
 print(x, end=" ")
 x -= 2
# c. 5, 3, 1

# How many times will this loop execute?
count = 0
for i in range(2, 10, 3):
 count += 1
print(count) 
# o/p -> a. 3

# What does this loop print?
for i in range(4):
 if i == 2:
    break
 print(i) 
# o/p -> c. 0, 1
 
# What happens in this loop?
x = 10
while x > 0:
 if x == 5:
    break
 print(x, end=" ")
 x -= 2 
# o/p -> 10, 8, 6
 
# Identify the error (if any) in this code:
# for i in range(5, 0, -1):
# print(i)
# o/p -> syntax error

# What is wrong with this code?
# while True:
#  print("Hello")
# o/p -> A. Infinity loop