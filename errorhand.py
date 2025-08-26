# Program:Read a file and write a modified version to a new file

# Ask the user for the input filename
filename = input("Enter the name of the file to read: ")

try:
    # Try opening the file for reading
    with open(filename, "r") as infile:
        data = infile.read()

    # Modify the content (example: uppercase)
    modified_data = data.upper()

    # Define output filename (can also be user input)
    output_file = "modified_" + filename

    # Write to the new file
    with open(output_file, "w") as outfile:
        outfile.write(modified_data)

    print(f"File has been modified and written to '{output_file}'")

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except PermissionError:
    print(f"Error: You don't have permission to read '{filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


# Ask the user for the input filename
filename = input("Enter the name of the file to read: ")

try:
    # Try opening the file for reading
    with open(filename, "r") as infile:
        data = infile.read()

    # Modify the content (example: uppercase)
    modified_data = data.upper()

    # Define output filename (can also be user input)
    output_file = "modified_" + filename

    # Write to the new file
    with open(output_file, "w") as outfile:
        outfile.write(modified_data)

    print(f"File has been modified and written to '{output_file}'")

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except PermissionError:
    print(f"Error: You don't have permission to read '{filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
