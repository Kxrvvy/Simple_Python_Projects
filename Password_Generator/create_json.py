import os
import json

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