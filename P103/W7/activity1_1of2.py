""""
Author: Julio Celón
Learning Activity (1 of 2): Functions
"""

def display_regular(message):
    print(f"{message}")
    
def display_uppercase(message):
    print(f"{message.upper()}")
    
def display_lowercase(message):
    print(f"{message.lower()}") 

message = input("What is your message? ")

display_regular(message)
display_uppercase(message)
display_lowercase(message)