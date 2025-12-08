import os
from org_fldrs import organize_folders


def main():

    print("=" * 40)
    print("Welcome to your file organizer")
    print("=" * 40)

    choose_folder_path = input("Enter Folder Path you want to organize: ")

    if not os.path.exists(choose_folder_path):
        print("No folder path exists")
        return

    organize_folders(choose_folder_path)


if __name__ == "__main__":
    main()
