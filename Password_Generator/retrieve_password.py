from create_json import load_password
from get_create_key import decrypt_pass


def retrieve_password():
    
    password = load_password()
    
    if not password:
        print("account password not exists...")
        return
    
    account = input("Enter account name: ").strip()
    
    if account in password:
        encrypt_pass = password[account] # retrieving the value of password from the account
        decrypt_passw = decrypt_pass(encrypt_pass)
        print(f"password for {account}: {decrypt_passw}")
    else:
        print(f"No password found for {decrypt_passw}")
        
# # testing of adding and retrieving password      
# print("== TESTING ADD PASSWORD ==")
# add_password()

# print("== TESTING RETRIEVING PASSWORD ==")
# retrieve_password()

# Listing all Passwords