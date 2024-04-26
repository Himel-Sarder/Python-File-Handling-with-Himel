# Write a Python program to read first n lines of Practise_container.txt.
# Input : 1
# Output : Hi I am Himel Sarder


























lines = []
def readNline(file_path, n):
    # Open the file
    with open("../Containers/Practise_container3.txt", 'r') as file:
        for _ in range(n):
            line = file.readline()
            lines.append(line)

# File path and number of lines to read
file_path = "../Containers/Practise_container3.txt"
n = int(input("Enter the number of Lines you want: "))

# Call the function and print the first n lines
First_N_line = readNline(file_path, n)
for line in lines:
    print(line.strip())  # strip() removes any leading or trailing whitespace
