from create_json import load_password, save_password
from generate_password import password_generator
from get_create_key import encrypt_pass



def update_passw():
    
    password = load_password()
    
    if not password:
        print("No password to update.")
        return
    
    account = input("Enter the account you want to update: ")
    
    if account in password:
        choice = input("Would you like to create an automatic generated password? (y/n): ")
        
        
        if choice == 'y':
            length = input("Input you password length (press 'Enter' for default 12): ")
            length = int(length) if length else 12
            new_password = password_generator(length)
            print(f"New password: {new_password} ")
        else:
            new_password = input("New password: ")
            
        password[account] = encrypt_pass(new_password)
        save_password(password)
        print(f"Your '{account}' password has updated successfully!")
    else:
        print(f"No password found for {account}")
        
            