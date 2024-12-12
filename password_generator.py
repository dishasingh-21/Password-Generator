#We'll create a password manager which creates a pass of our desired length. Further asking the user if they want any specific kind of chracters in their password. More or less this is gonna be a dynamic code. 

import random
import string   
#to get all lower and upper case letters, special characters, numbers, etc..

#now we need to ask the user 1) what length of password they want. 2) What all they want to add - numbers, special characters, etc..
def generate_password(minimum_length, numbers= True, special_characters = True):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special_chars

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False
    
    while not meets_criteria or len(pwd) < minimum_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special_chars:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd


min_length = int(input("Enter the minimum length of password: "))
has_number = input("Do you want to have numbers? (y/n)").lower() == 'y'
has_special = input("Do you want to have special characters? (y/n)").lower() == 'y'
pwd = generate_password(min_length, has_number, has_special)
print(f"The generated password is: {pwd}")

