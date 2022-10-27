my_dict = {
    "blue": "sky",
    "double": 2,
    "half": 0.5,
    "green": "grass",
    "yellow": "sun",
    "red": "apple"
}

your_num = int(input("Enter a number: "))
to_do = input("Double or half").lower()

# Look up value
multiply_by = my_dict[to_do]

# Do math!
answer = your_num * multiply_by
print("{} x {} = {}".format(your_num, multiply_by, answer))