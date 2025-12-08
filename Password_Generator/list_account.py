from create_json import load_password

def list_account():
    password = load_password()
    
    if not password:
        print("No password saved yet!")
        return
    print("Saved accounts:\n")
    for i, account in enumerate(password.keys(), 1):
        print(f"{i}. {account}")