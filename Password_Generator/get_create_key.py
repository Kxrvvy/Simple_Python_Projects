import os
from cryptography.fernet import Fernet

# Creating the encryption
def get_or_create_key():
    if os.path.exists("key.key"):
        with open("key.key", "rb") as key_file:
            return key_file.read()
    else:
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
        return key
    
KEY = get_or_create_key()
cipher = Fernet(KEY)

def encrypt_pass(password):
    #Encrypting the password 
    return cipher.encrypt(password.encode()).decode() # String -> encrypts -> bytes

def decrypt_pass (encrypt_pass):
    #Decrypting the password
    return cipher.decrypt(encrypt_pass.encode()).decode() # bytes -> decrypts -> String

'''
# Test Encryption 
original = "testing12345pass"
print(f"original password: {original}")

encrypt =  encrypt_pass(original)
print(f"Encrypt pass: {encrypt}")

decrypt = decrypt_pass(encrypt)
print(f"Decrpyt pass: {decrypt}")

#Test Ssving encrypted password
passwords = {
    "gmail": encrypt_pass("testtest123"),
    "facebook": encrypt_pass("testing12345")
}

#Saving password
save_password(passwords)

#loading and decrypt
load = load_password()
print("\n Decrypting items")
for account, encrypt_val in load.items():
    decrypt_row = decrypt_pass(encrypt_val)
    print(f"{account}: {decrypt_row}")
'''