import os
import shutil

x = input("Enter The Source Folder Name: ")
y = input("Enter The Destination Folder Name: ")
source = x + '/'
destination = y + '/'
list_of_files = os.listdir(source)
for file in list_of_files:
    try:
        shutil.move((source + file), destination)
        print("File Moved Successfully")
    except:
        print("No File Or Directory Found!")
