import os



''' 
this function checks if the filename already exist in the destination folder
if it does not exist, it safely goes into the folder.
it already exist, this create a rename for the file that adds a number next to the filename
'''


def get_unique_filename(destination_folder, filename):
    
    # Combines the folder_path and filename
    full_path = os.path.join(destination_folder, filename)

    # returns the full path if does not exist
    if not os.path.exists(full_path):
        return full_path

    # split the filename (eg. name.png -> name, .png)
    name, file_extension = os.path.splitext(filename)

    # rename the file that already exist within the folder
    counter = 1
    while True:
        new_filename = name + "(" + str(counter) + ")" + file_extension
        new_path = os.path.join(destination_folder, new_filename)

        if not os.path.exists(new_path):
            return new_path # returns the new filename if detected that is does not exist

        counter += 1 # increment the value for the next same file


# # ===== TEST CODE =====``

# # Create a test folder
# test_folder = "test_folder"

# # Create the folder if it doesn't exist
# if not os.path.exists(test_folder):
#     os.makedirs(test_folder)

# # Test 1: File doesn't exist
# print("Test 1: File doesn't exist")
# result = get_unique_filename(test_folder, "photo.jpg")
# print(f"Result: {result}")
# print(f"Expected: {test_folder}/photo.jpg")
# print()

# # Create a dummy file to test duplicates
# test_file = os.path.join(test_folder, "photo.jpg")
# with open(test_file, "w") as f:
#     f.write("dummy content")

# # Test 2: File exists once
# print("Test 2: File exists once")
# result = get_unique_filename(test_folder, "photo.jpg")
# print(f"Result: {result}")
# print(f"Expected: {test_folder}/photo(1).jpg")
# print()

# # Create another duplicate
# test_file2 = os.path.join(test_folder, "photo(1).jpg")
# with open(test_file2, "w") as f:
#     f.write("dummy content")

# # Test 3: Multiple duplicates
# print("Test 3: Multiple duplicates exist")
# result = get_unique_filename(test_folder, "photo.jpg")
# print(f"Result: {result}")
# print(f"Expected: {test_folder}/photo(2).jpg")