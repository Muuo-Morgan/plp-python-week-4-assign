# Creating a new file called Rio.txt and writing something into it

def create_file():
    filename = "Rio.txt"

    try:
        # Open file in write mode ("w" creates the file if it doesn't exist)
        with open(filename, "w") as file:
            file.write("Rio de Janeiro,[a] or simply Rio,[8] is the capital of the state of Rio de Janeiro. \n")
            file.write("It is the second-most-populous city in Brazil (after São Paulo) and the sixth-most-populous city in the Americas.\n")

        print(f"File '{filename}' created successfully!")

    except Exception as e:
        print(f"An error occurred while creating the file: {e}")

# Run the function
create_file()

# Reading from an existing file and writing modified content to a new file

def file_read_write():
    # Ask user for filename
    filename = input("Enter the filename to read: ")

    try:
        # Try to open and read the file
        with open(filename, "r") as file:
            content = file.read()

        # Modify the content (example: make it uppercase)
        modified_content = content.upper()

        # Create a new filename for the modified file
        new_filename = "modified_" + filename

        # Write the modified content to the new file
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"File has been read and modified successfully!")
        print(f"Modified file saved as: {new_filename}")

    except FileNotFoundError:
        print("Error: The file was not found. Please check the filename and try again.")
    except PermissionError:
        print("Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
file_read_write()



