

FILE_CATEGORIES = {
    'Images': ['.png', '.jpg', '.gif', '.svg'],
    'Documents': ['.pdf', '.txt', '.docx', '.doc', '.xlsx'],
    'Videos': ['.mp4', '.mov', '.avi', '.mpg', '.mpeg']
}

def get_file_category(extension):
    extension = extension.lower()  # converts the value into lowercase

    # loops through the FILE_CATEGORIES
    # get key and value within the FILE_CATEGORIES' items
    for category, file_extension in FILE_CATEGORIES.items():
        if extension in file_extension:  # check if the value of parameter 'extension' is inside the file_extension
            return category  # returns the category(key) if True
    return 'Others'  # return others if theirs no match

# test-case
# file = get_file_category('.PDF')
# print(file)