#1. What is the output of the following code?
lst =[1, 2, 3, 4, 5]
print(lst[::-1])
# o/p -> [5, 4, 3, 2, 1]

# 2. What will be printed? 
lst = [10, 20, 30]
lst.append([40, 50])
print(len(lst))
# o/p -> 4

# 3. 
lst = [1, 2, 3]
lst.extend([4, 5])
lst.insert(2, 10) 
print(lst) 
# o/p -> [1, 2, 10, 4, 5]

#  4 .What is the output of this code? 
tup = (1, 2, 3, 4) 
# tup[2] = 10 
print(tup) 
# o/p -> error -> tup[2] =10

# 5. Find the output: 
tup = (10, 20, 30, 40, 50) 
print(tup[-3:]) 
# o/p -> [30, 40, 50]

# 6. Find the output: 
set1 = {1, 2, 3} 
set2 = {2, 3, 4} 
print(set1 & set2)
# o/p -> {2, 3}
 
# 7. Find the missing code to get the correct difference between two sets: 
set1 = {10, 20, 30, 40} 
set2 = {30, 40, 50, 60} 
diff =  set1 - set2   #o/p      
print(diff) 
# o/p -> {10, 20, 60}   
                        
# 8. What will be printed? 
d = {'x': 10, 'y': 20} 
d['z'] = 30 
print(d) 
# o/p -> {'x':10, 'y' : 20, 'z':30}

# 9. What will be printed? 
d = {'a': 1, 'b': 2, 'c': 3} 
d.pop('b') 
print(d)
# o/p -> {'a': 1, 'c' : 3}


