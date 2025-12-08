from create_json import load_password, save_password
from generate_password import password_generator
from get_create_key import encrypt_pass

def add_password():
    ### Add a new password ###
    
    account = input("Enter account name(e.g. email, yt, fb): ").strip()
    choice = input("Do you want to automatically generate password? (y/n): ").lower()
    
    if choice == 'y':
        length = input("Enter the password length (default is 12): ")
        length = int(length) if length else 12
        password = password_generator(length)
        print(f"Generated Password: {password}")
    else:
        password = input("Input your password: ")
        
    
    # checks if password exists
    passwords = load_password()

    # Encrypt and save the password
    passwords[account] = encrypt_pass(password)
    save_password(passwords)
    
    # Indicate that the password is saved
    print(f"Password for '{account}' has been successfully saved!")
    