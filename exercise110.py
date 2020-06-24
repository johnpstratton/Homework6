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

def PerfectNum(num): # Initiate function with num parameter
    divisor = num       #Set a divisor equal to parameter
    values = []         # Blank list to append values to
    while divisor > 0:  #Initiate while loop
        solution = num %divisor #divide the num by %divisor to see if its a proper divisor
        if solution == 0:           #if return value has 0 remainder append to values
            values.append(divisor)
        divisor -= 1        #decrement divisor
    for x in values: #Loop through values
        if x == num:    #Remove the actual num 
            values.remove(x)
        elif sum(values) == num: #determine whether it is a perfect number and return True or False
            return True
        else:
            return False
    
perfectnumbers = [] #blank list to store perfect numbers

for x in range(1, 10001):       #loop through 1-10000 and append to list if a perfect number
    if PerfectNum(x) == True:
        perfectnumbers.append(x)

print(perfectnumbers)


