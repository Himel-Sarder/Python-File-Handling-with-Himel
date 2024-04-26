# Write a program to read  "Practise_container4.txt file contains binary data and convert those to ASCII form or Human readable form with another file named "10-data.txt"




























def binary_to_text(binary_file, text_file):
    # Read binary data from the binary file
    with open("../Containers/Practise_container4.txt", 'rb') as file:
        binary_data = file.read()

    # Convert binary data to text
    ascii_text = ''.join([chr(int(binary, 2)) for binary in binary_data.split()])

    # Write the text data to a text file
    with open(text_file, 'w') as file:
        file.write(ascii_text)

# Specify the paths for the binary and text files
binary_file = '../Containers/Practise_container4.txt'
text_file = '../Output/10-data.txt'

# Convert binary to text and write to the text file
binary_to_text(binary_file, text_file)
