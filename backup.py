import os
import shutil

src = input("Enter The Source Directory: ")
des = input("Enter The Destination Directory: ")
source = src + '/'
destination = des + '/'
list_of_files = os.listdir(source)
for file in list_of_files:
    try:
        shutil.copy((source + file), destination)
        print("File Was Backed Up Successfully")
    except:
        print("No File Or Directory Found!")

