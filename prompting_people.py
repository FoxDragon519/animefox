try:
    age = int(input("How old are you? "))
except ValueError:
    print(f"I'm sorry, but the age you entered must be a number.")
height = input("How tall are you? ")
weight = input("How much do you weigh? ")

print(f"So, you're {age} years old, {height} tall and {weight} heavy.")
