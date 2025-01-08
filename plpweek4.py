def read_and_write_with_error_handling():
    # Ask the user for the filename
    input_filename = input("Please enter the filename to read from: ")
    output_filename = input("Please enter the filename to write the modified content to: ")

    try:
        # Try to open the input file and read its content
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
        
        # Modify the content (e.g., convert it to uppercase)
        modified_content = content.upper()

        # Write the modified content to the output file
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)

        print(f"Content from '{input_filename}' has been successfully modified and written to '{output_filename}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except IOError as e:
        print(f"Error reading or writing the file: {e}")

# Call the function to execute the read, modify, and write operations
read_and_write_with_error_handling()
