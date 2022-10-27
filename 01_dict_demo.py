my_dict = {
    "blue": "sky",
    "double": 2,
    "half": 0.5,
    "green": "grass",
    "yellow": "sun",
    "red": "apple"
}

# List to make testing faster
to_check = ("blue", "red", "double", "half")

for item in to_check:

    # Check if it's a key (ie: a colour in our dictionary)
    if item in my_dict:
        print("{} is a key in the dictionary".format(item))

        # Look up the value associated with the key
        coloured_object = my_dict[item]

        # Output the value and the key (eg: the sky us blue)
        print("The {} is {}".format(coloured_object, item))