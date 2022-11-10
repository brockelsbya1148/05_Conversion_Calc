from time import sleep
# Functions go here


# Puts series of symbols at start and end of text (for emphasis)
def statement_generator(text, decoration):

    # Make string with five characters
    ends = decoration * 5

    # Add decoration to start and end of statement
    statement = "{}  {}  {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


# Displays instructions / information
def instructions():

    statement_generator("Instructions / Information", "=")
    print("Please choose a unit to convert from and a unit to convert to")
    print()
    sleep(1)
    print("This program converts measurements of time, mass, and distance")
    print()
    sleep(1)
    print("Complete as many calculations as necessary, pressing <enter> at the end of each calculation or any key to quit")
    print()
    return ""


# checks input is a number more than given value
def num_check(question):
    # Check that users enter a number that is more than zero
    valid = False
    while not valid:

        error = "Please enter an integer that is more than 0 and less than 201"

        try:
        
            low_num = 1
        

            # Ask user to enter a number
            response = int(input(question))

            # Checks number is more than zero or under 200
            if low_num <= response:
                return response

            # outputs error if input is invalid
            else: 
                print(error)
                print()

        except ValueError:
            print(error)
            print()


# Checks user choice is 'weight', 'length', or 'time'
def user_choice():

    valid = False
    while not valid:

        response = input("Measurement (Weight / Distance / Time): ").lower()

        weight_ok = ["weight", "mass", "w", "wt"]
        if response in weight_ok:
            return "weight"

        distance_ok = ["length", "distance", "dist", "d"]
        if response in distance_ok:
            return "distance"

        time_ok = ["time", "t"]
        if response in time_ok:
            return "time"
        
        else:
            print("Please choose a valid measurement!")
            print()


# Asks user what unit they want to convert from and to
def weight_conv():

    if user_choice == "weight":
        weight_from = input("Which unit would you like to convert from (mg, g, kg, t)? ")
        weight_to = input("Which unit would you like to convert to?")

        if weight_from == "mg" or "milligrams":
            return "from milligrams"

        elif weight_from == "g" or "grams":
            return "from grams"
        
        elif weight_from == "kg" or "kilograms":
            return "from kilograms"

        elif weight_from == "t" or "tonnes":
            return "from tonnes"

        if weight_to == "mg" or "milligrams":
            return "to milligrams"

        elif weight_to == "g" or "grams":
            return "to grams"
        
        elif weight_to == "kg" or "kilograms":
            return "to kilograms"

        elif weight_to == "t" or "tonnes":
            return "to tonnes"


# Main Routine goes here

# Heading
statement_generator("Conversion Calculator for Weight, Distance & Time", "-")

# Display instructions if user has not used the program before
first_time = input("Press <enter> to see instructions or any key to continue ")

if first_time == "":
    instructions()

# Loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":
    
    # Ask the user for the file type
    data_type = user_choice()
    print()
    print("You chose", data_type)
    print()

    print()
    keep_going = input("Press <enter> to continue or any key to quit ")
    print()
