name = "Jose"
final_greeting = "How are you {}?"
jose_greeting = final_greeting.format(name)
print(jose_greeting)




# self practice
welcome_text = "Dear {}, welcome to FIDATA's {} section." # defining the sentence with changable words
client_name = "Robin" 
section = "06"
final_wt = welcome_text.format(client_name, section) # creating a new sentence using .format to filling up the values
print(final_wt)

n = "Rolf"
street  = "123 no name"
pc = "PY10C"
address = f"""Name: {n}
Street: {street}
Postcode: {pc}
"""
print(address)

des = "{} is {} years old."
print(des.format("Bob", 30))