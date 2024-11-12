# Prompt the user to enter the filename
input_filename = input("Enter the filename to read: ")

# Specify the name of the new file to write the modified content
output_filename = "output_modified.txt"

try:
    with open(input_filename, 'r') as input_file:
        content = input_file.read()
    modified_content = content.upper() 
  
    with open(output_filename, 'w') as output_file:
        output_file.write(modified_content)

    print(f"The modified content has been successfully written to: {output_filename}")

except FileNotFoundError:
    print("Error: The specified file does not exist.")
except IOError:
    print("Error: An issue occurred while reading or writing the files.")￼Enter
