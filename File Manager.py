import os
import re
import shutil


def copy_file(source_path, destination_path):
    print(f"The file is copied form {source_path} to {destination_path}")
    shutil.copy(source_path, destination_path)
    print("The file is successfully copied!")

def delete_file(source_directory):
    print(f"Deleting file {source_directory}")
    file = input("Enter the filename: ")
    if os.path.exists(source_directory):
        os.remove(file)
        print("The file is successfully deleted!")

def rename_file(source_path):
    if os.path.exists(source_path):
        os.rename(source_path)
        print("this file is successfully renamed!")
    else:
        print("The {} does not exist".format(source_path))

def create_directory(new_directory):
    print(f"Creating directory {new_directory}")
    pattern = r"^([A-Za-z:])\(A-Za-z)\(A-Za-z)\+"
    if re.match(pattern,new_directory):
        os.mkdir(new_directory)
    else:
        print("{} is an incorrect directory".format(new_directory))

def rename_directory(old_directory, new_directory):
    print(f"Renaming directory form {old_directory} to {new_directory}")
    pattern = r"^([A-Z])\(A-Z)\(A-Z)\+"
    if re.match(pattern, old_directory):
        os.chdir(new_directory)
    else:
        print("{} is an incorrect directory".format(old_directory))


def main():
    while True:
        print("Copy file: 1")
        print("Delete File: 2")
        print("Rename File: 3")
        print("Create Directory: 4")
        print("Rename Directory: 5")

        file_operation = int(input("Enter the file operation you want to perform: "))

        if file_operation == 1:
            source_path = input("Enter the source path: ")
            destination_path = input("Enter the destination path: ")
            copy_file(source_path, destination_path)
        elif file_operation == 2:
            source_directory = input("Enter the source directory: ")
            delete_file(source_directory)
        elif file_operation == 3:
            source_path = input("Enter the source path: ")
            rename_file(source_path)
        elif file_operation == 4:
            new_directory = input("Enter the new directory: ")
            create_directory(new_directory)
        elif file_operation == 5:
            old_directory = input("Enter the old directory: ")
            new_directory = input("Enter the new directory: ")
            rename_directory(old_directory, new_directory)
        else:
            print("Invalid input!")

if __name__ == "__main__":
    main()