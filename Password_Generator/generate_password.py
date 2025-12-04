import string
import random

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