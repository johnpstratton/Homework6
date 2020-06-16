# Write a function that generates a random password. 
# Your function will not take any parameters.
# The password should have a random length of between 7 and 10 characters. 
# Each character should be randomly selected from positions 33 to 126 in the ASCII table. 
# It will return the randomly generated password as its only result. 
# Display the randomly generated password in your file’s main program. 
# Your main program should only run when your solution has not been imported into another file.

# Hint: You will probably find the chr function helpful when completing this exercise. 
# Detailed information about this function is available online.
import random 
def randPassword():
    num = 0 # declare integer variable to 
    password = ""
    randRange = random.randint(7, 10)
    count = 0
    while count < randRange:
        num = random.randint(33, 126)
        password += chr(num)
        count += 1
    return password

print(randPassword())
