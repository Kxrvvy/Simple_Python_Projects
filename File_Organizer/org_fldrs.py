import shutil
import os
from get_file_category import get_file_category
from get_unique_filename import get_unique_filename




def organize_folders(folder_path):
    # Initialize category count

    category_count = {}

    # Get all item in the folder
    items = os.listdir(folder_path)

    # loop through each item

    for item in items:
        item_path = os.path.join(folder_path, item)

        # checks if the item is a file or folder
        if not os.path.isfile(item_path):
            continue
        # Splitting the filename into two
        name, file_extension = os.path.splitext(item)

        # getting the category(file_extension)
        category = get_file_category(file_extension)

        # Create category folder if not exists
        category_folder = os.path.join(folder_path, category)
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)
            
        # Get unique destination
        destination = get_unique_filename(category_folder, item)
        
        shutil.move(item_path, destination)
        
        # Add category counter
        if category not in category_count:
            category_count[category] = 0
        category_count[category] += 1
        
        # proggress message
        print(f"Moved: {item} -> {destination}")
        
    # Show Summary 
        
    print("\n" + "=" * 40)
    print("Organization Complete")
    print("=" * 40)
            
    # showing how many files moved
    total = sum(category_count.values())
    print(f"Total files moved: {total}")

    # shows the file counts in each category
    for category, count in category_count.items():
        print(f"  - {category}: {count} files")