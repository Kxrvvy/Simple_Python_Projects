import random
import string
import json 
import os 
from cryptography.fernet import Fernet

# Generates random password
def password_generator(length = 12):
    
    # create all the possible characters
    letters = string.ascii_letters # Alphabets (upper/lowercase)
    numbers = string.digits # numnbers
    symbols = string.punctuation # special characters
    
    # Combine
    combination = letters + numbers + symbols
    
    #Create random password 
    password = ''.join(random.choice(combination) for _ in range(length))
    
    return password
    
    
# print(password_generator())

#Create the json file
def load_password ():
    ### Load the password/s from the file ###
    if os.path.exists("password.json"):
        with open("password.json", "r") as file: # 'r' means read
            return json.load(file) # returns the password
    return {} # return an empty dictionary if not exist   


def save_password(passwords):
    with open("password.json", "w") as file:
        json.dump(passwords, file, indent = 4)
    
    
    
    
# passw = {
#     "gmail": "test1234",
#     "fb": "helo1234"
# }

# print("Saving password...")
# save_password(passw)
# print("successfully save")


# print("Loading password")
# loaded = load_password()
# print(f"passwords: {loaded}")


# Creating the encryption

