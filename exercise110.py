# An integer, n , is said to be perfect when the sum of all of the proper divisors of n is equal to   n . 
# For example, 28 is a perfect number because:
#  Its proper divisors are 1, 2, 4, 7 and 14, and 1 + 2 + 4 + 7 + 14 = 28.

# Write a function that determines whether or not a positive integer is perfect. 
# Your function will take one parameter. 
# If that parameter is a perfect number then your function will return true. 
# Otherwise it will return false. 
# In addition, write a main program that uses your function to:
# Identify and display all of the perfect numbers between 1 and 10,000. 
# Import your solution to Exercise 109 when completing this task.

def PerfectNum(num):
    divisor = num
    values = []
    while divisor > 0:
        solution = num %divisor
        if solution == 0:
            values.append(divisor)
        divisor -= 1
    for x in values:
        if x == num:
            values.remove(x)
        elif sum(values) == num:
            return True
        else:
            return False
    
perfectnumbers = []

for x in range(1, 10001):
    if PerfectNum(x) == True:
        perfectnumbers.append(x)

print(perfectnumbers)


