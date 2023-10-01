import os

def DisplayMenu():
    print("""Welcome to the File Management System!

1. Create a new file
2. Write data to a file
3. Read data from a file
4. List files in a directory
5. Delete a file
6. Search for a file by name
7. Quit""")

def CreateFile():
    file_name = input("Enter the file name (with extension):")
    directory_path = input("Enter the directory path:")
    full_path = os.path.join(directory_path, file_name)
    try:
        if not os.path.isdir(directory_path):
            print(f"The directory '{directory_path}' does not exist.")
        else:
            if os.path.exists(full_path):
                print(f"The file '{file_name}' already exists.")
            else:
                if not os.path.basename(file_name) == file_name:
                    print(f"The file name '{file_name}' is not valid.")
                else:
                    with open(full_path, 'w') as file:
                        print(f"File '{file_name}' created successfully in '{directory_path}'.")
    except PermissionError:
        print(f"Permission denied. You don't have the necessary permissions to create '{full_path}'.")
    except Exception as e:
        print(f"An error occured : {e}")


def WriteToFile():
    file_name = input("Enter the file name: ")
    directory_path = input("Enter the directory path: ")
    data = input("Enter the data to write to the file: ")
    full_path = os.path.join(directory_path, file_name)
    try:
        if not os.path.isdir(directory_path):
             print(f"The directory '{directory_path}' does not exist.")
        else:
            if not os.path.exists(full_path):
                print(f"The file '{file_name}' does not exist.")
            else:
                with open(full_path, "w") as file:
                    file.write(data)

                print(f"Data written successfully to '{file_name}' in '{directory_path}'.")

    except PermissionError:
        print(f"Permission denied. You don't have the necessary permissions to write to '{full_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


def ReadFromFile():
    file_name = input("Enter the file name: ")
    directory_path = input("Enter the directory path: ")
    full_path = os.path.join(directory_path, file_name)
    try:
        if not os.path.isdir(directory_path):
             print(f"The directory '{directory_path}' does not exist.")
        else:
            if not os.path.exists(full_path):
                print(f"The file '{file_name}' does not exist.")
            else:
                with open(full_path, "r") as file:
                    file_content = file.read()
                    print(f"Contents of '{file_name}':\n{file_content}")

    except PermissionError:
        print(f"Permission denied. You don't have the necessary permissions to write to '{full_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

def ListOfFiles():
    directory_path = input("Enter the directory path: ")
    try:
        if not os.path.isdir(directory_path):
             print(f"The directory '{directory_path}' does not exist.")
        else:
            files_in_directory = os.listdir(directory_path)
            for file_name in files_in_directory:
                print(file_name)

    except PermissionError:
        print(f"Permission denied. You don't have the necessary permissions to access '{directory_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

def DeleteFile():
    file_name = input("Enter the file name: ")
    directory_path = input("Enter the directory path: ")
    full_path = os.path.join(directory_path, file_name)
    try:
        if not os.path.isdir(directory_path):
             print(f"The directory '{directory_path}' does not exist.")
        else:
            if not os.path.exists(full_path):
                print(f"The file '{file_name}' does not exist.")
            else:
                os.remove(full_path)
                print(f"File '{file_name}' deleted successfully.")

    except PermissionError:
        print(f"Permission denied. You don't have the necessary permissions to write to delete '{full_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

def SearchFileByName():
    file_name = input("Enter the file name: ")
    directory_path = input("Enter the directory path: ")
    try:
        if not os.path.isdir(directory_path):
             print(f"The directory '{directory_path}' does not exist.")
        else:
            files_in_directory = os.listdir(directory_path)
            found = False
            for filename in files_in_directory:
                if filename == file_name:
                    found = True
                    break
            if found:
                 print(f"File '{file_name}' exists in '{directory_path}'.")
            else:
                print(f"File '{file_name}' does not exist in '{directory_path}'.")

    except PermissionError:
        print(f"Permission denied. You don't have the necessary permissions to access '{directory_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")




def main():
    while True:
        DisplayMenu()
        choice = input("Please enter your choice (1-7): ")
        if choice == '1':
            CreateFile()
        elif choice == '2':
            WriteToFile()
        elif choice == '3':
            ReadFromFile()
        elif choice == '4':
            ListOfFiles()
        elif choice == '5':
            DeleteFile()
        elif choice == '6':
            SearchFileByName()
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please enter a valid option (1-7).")
            
if __name__ == "__main__":
    main()