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
    num = 0 # declare variable to store random number between 33-136
    password = "" #string to add characters to make password
    randRange = random.randint(7, 10) # Used to ensure random length of password between 7-10 characters
    count = 0 #incrementor for while loop
    while count < randRange: # Initiate while loop 
        num = random.randint(33, 126) # Initiate 1 new random number
        password += chr(num) # append random character to password
        count += 1 # increment
    return password # return the password when while loop completes

print(randPassword())
