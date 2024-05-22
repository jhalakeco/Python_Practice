# String formating

age = 34
age_as_str = str(age)
print("You are " + age_as_str) # this is a general way to print str and int together. but it can be problematic. Therefore, the next process is handy

# Using fstring to print str and int together
print(f"You are {age}")

# another example

name = "Jose"
greeting = f"How are you, {name}?"
print(greeting) # fstring can also be used to print two variables together without using any logical operations



