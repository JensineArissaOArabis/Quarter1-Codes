full_name = input("Enter your full name (First, Middle, Last): ")

name_parts = full_name.split(',')

first = name_parts[0].strip().capitalize()
middle = name_parts[1].strip().capitalize()
last = name_parts[2].strip().title()

middle_initial = middle[0] + '.'

formatted_name = f"{last}, {first} {middle_initial}"

print(f"Formatted Name: {formatted_name}")