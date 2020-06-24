# Write a function that determines how many days there are in a particular month. 

# Your function will take two parameters: 
# The month as an integer between 1 and 12, and the year as a four digit integer. 

# Ensure that your function reports the correct number of days in February for leap years. 

# Include a main program that reads a month and year from the user and displays the number of days in that month. 
# You may find your solution to Exercise 57 helpful when solving this problem.
days = {        # Initiate days dictionary to store the month/num of days as key:value pair
    1 : 31,
    2 : 28,
    3 : 31,
    4 : 30,
    5 : 31,
    6 : 30,
    7 : 31,
    8 : 31,
    9 : 30,
    10 : 31,
    11 : 30,
    12 : 31
}
def NumofDays(month, year): # declare function with two parameters 
    for x in days: # Loop through days dictionary 
        if (month == x and month != 2 in days): #if month is not February 
            return days[month] #return number of days for any month thats not February
        elif (month == x and month == 2 in days and year %4 != 0): # If month is February but its not a leap year
            return days[month] # return 28
        elif (month == x and month == 2 in days and year %4 == 0): #If month is Feb and is a leap year
            return 29 
    
month = int(input("Please enter a month between 1-12: ")) # Asks user for month number
year = int(input("Please enter a year in a four digit format (i.e. 2020): ")) # Asks user for year
print(NumofDays(month, year)) # Call NumofDays function and pass month and year
