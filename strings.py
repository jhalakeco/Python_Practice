string_with_quotes = "Hello, it's me!"

another_with_quotes = "He said 'Hi!' to me." # Escaping: This is a way to use quote inside the quotation. Well, this can be avoided using a blackslash in front of the quotation mark (""). This is actually not a good practice

another_quote_example = "He said \"Hi!\" to me."


# Multiline ----
multiline = """Hello, world! 



I am learning python from the basic.""" # to print several lines of strings sentences in multiple lines

print(multiline)

""" multiline can also be used as a comment in python """


# Printing strings in conjunction

name = "Jacob"
greeting = "Hello, " + name + "!"

print(greeting)

age = 32

new_greet = greeting + "You are" + age + "years old!" # this will be an error. Because in Python we cannot concatenate strings and integer. Therefore, the interger has to be converted into string.

age_str = str(32) # so the int is actually converted into a string. 

new_greet_str = greeting + " You are " + age_str + " years old!" # now concatenating together.

print(new_greet_str)