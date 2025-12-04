from create_json import save_password, load_password



def del_password():
    ### Delete Password Entry ###
    password = load_password()
    
    if not password:
        print("No password to delete.")
        return
    
    account = input("Enter an account to delete: ").strip()
    
    if account in password:
        del password[account] # Delete the password with the key value of account name 
        save_password(password) # save the update dictionary
        print(f"Password for '{account}' has been deleted")
    else:
        print(f"No password found for '{account}'")