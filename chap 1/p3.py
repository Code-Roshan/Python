# To print the contents of a directory in Python using the os module, you can utilize the os.listdir() function. 

import os

# Specify the directory path
directory_path = '/Users'

# Get the list of entries in the directory
entries = os.listdir(directory_path)

# Print each entry
for entry in entries:
    print(entry)
