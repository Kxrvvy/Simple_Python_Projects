from retrieve_password import retrieve_password
from add_password import add_password
from list_account import list_account
from delete_password import del_password
from update_password import update_passw





def main():
    
    print("=" * 40)
    print("PASSWORD MANAGER")
    print("=" * 40)
    
    
    while True:
        print(
            "\nMenu:",
            "1. Add new password",
            "2. Retrieve password",
            "3. List all accounnts",
            "4. Update Password",
            "5. Delete Password",
            "6. Exit",
            sep= "\n"
        )
        choice = int(input("Enter your choice: "))
        
        match choice:
            case 1: 
                add_password()
            case 2: 
                retrieve_password()
            case 3:
                list_account() 
            case 4:
                update_passw()
            case 5:
                del_password()
            case 6:
                break
            case _:
                print("Invalid option")
    
        
if __name__ == "__main__":
    main()
     