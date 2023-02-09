import os
import random

#function to generate characters randomly
def generate_string(length):
    password_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    pw = ""
    for i in range(length):
        pw += random.choice(password_chars)
    return pw


# Place your folder directory you want renamed in the variable "folder"
folder = ""

#Renames the files in the folder. Adjust the length of the filename desired in the generate_string function
for file_name in os.listdir(folder):
    extension = os.path.splitext(file_name)
    source = folder + file_name
    destination = folder + generate_string(9) + str(extension[1])
    try:
        os.rename(source, destination)
    except FileExistsError:
        pass

print("All files renamed")

