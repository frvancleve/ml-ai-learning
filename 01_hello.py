print("Hello, world!")

# This is a comment. Python ignores anything after the # on a line.
# Comments are for humans (you and future you).

name = input("What is your name? ")
age = int(input("How old are you? "))
height_m = float(input("What is your height in meters? "))
major = input("What is your major? ")
job_title = input("What is your job title? ")

print(f"My name is {name}")
print(f"I am {age} years old")
print(f"My height is {height_m:.2f} meters")
print(f"My major is {major}")
print(f"My job title is {job_title}")

print()

if age > 40:
    print("You've got a ton of real-world experience!")
else:
    print("You're building a strong foundation early on!")
