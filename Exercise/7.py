#Write a function in Python to count uppercase character in Practise_container3.txt text file.
#Output : 18



























def UpperCharcounter():
    count = 0
    with open("../Containers/Practise_container3.txt", "r") as File:
        content = File.read()
        for char in content:
            if char.isupper():
                count += 1

    print(count)

UpperCharcounter()