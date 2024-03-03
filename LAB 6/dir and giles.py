#1
import os

def list_directories(path):
    directories = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]
    return directories

def list_files(path):
    files = [name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))]
    return files

def list_all(path):
    all_entries = os.listdir(path)
    return all_entries

path = input("Enter the path to list directories and files: ")

print("Directories:")
print(list_directories(path))

print("\nFiles:")
print(list_files(path))

print("\nAll directories and files:")
print(list_all(path))



#2
import os

def check_access(path):

    if not os.path.exists(path):
        print(f"Path '{path}' does not exist.")
        return
    if not os.access(path, os.R_OK):
        print(f"Path '{path}' is not readable.")
    else:
        print(f"Path '{path}' is readable.")

    if not os.access(path, os.W_OK):
        print(f"Path '{path}' is not writable.")
    else:
        print(f"Path '{path}' is writable.")

    if os.name != 'nt':  
        if not os.access(path, os.X_OK):
            print(f"Path '{path}' is not executable.")
        else:
            print(f"Path '{path}' is executable.")

path = input("Enter the path to check: ")
check_access(path)


#3
import os

def check_path(path):
    if os.path.exists(path):
        print("Path exists.")
        directory, filename = os.path.split(path)
        print("Directory:", directory)
        print("Filename:", filename)
    else:
        print("Path does not exist.")

path = input("Enter the path to test: ")
check_path(path)


#4
def count_lines(filename):
    with open(filename, 'r') as file:
        line_count = sum(1 for line in file)
    return line_count

filename = input("Enter the name of the text file: ")

try:
    lines = count_lines(filename)
    print("Number of lines in the file:", lines)
except FileNotFoundError:
    print("File not found. Please check the filename and try again.")


#5
def write_list_to_file(filename, input_list):
    with open(filename, 'w') as file:
        for item in input_list:
            file.write(str(item) + '\n')

filename = input("Enter the name of the file to write: ")
input_list = input("Enter the elements of the list separated by space: ").split()

write_list_to_file(filename, input_list)
print(f"The list has been written to '{filename}'.")


#6
import string

def generate_files():
    for letter in string.ascii_uppercase:
        filename = letter + ".txt"
        with open(filename, 'w') as file:
            file.write("This is the content of " + filename)

generate_files()
print("Files generated successfully.")


#7
def copy_file(source_filename, destination_filename):
    try:
        with open(source_filename, 'r') as source_file:
            with open(destination_filename, 'w') as destination_file:
                for line in source_file:
                    destination_file.write(line)
        print("File copied successfully.")
    except FileNotFoundError:
        print("One of the files does not exist. Please check the filenames and try again.")

source_filename = input("Enter the name of the source file: ")
destination_filename = input("Enter the name of the destination file: ")

copy_file(source_filename, destination_filename)


#8
import os

def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.F_OK):
            if os.access(path, os.W_OK): 
                try:
                    os.remove(path)
                    print(f"File '{path}' deleted successfully.")
                except OSError as e:
                    print(f"Error: {e}")
            else:
                print(f"Error: No write access to file '{path}'.")
        else:
            print(f"Error: File '{path}' does not exist.")
    else:
        print(f"Error: Path '{path}' does not exist.")

path = input("Enter the path of the file to delete: ")
delete_file(path)
