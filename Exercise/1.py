# Write a function in python to read the content from a text file "Practise_container.txt" in Containers directory line by line and display the same on screen.




























def ReadFile():
    # Open the file relative to the current script file
    file_path = "../Containers/Practise_container.txt"
    with open(file_path, "r") as file:
        for line in file:
            print(line, end="")

ReadFile()
