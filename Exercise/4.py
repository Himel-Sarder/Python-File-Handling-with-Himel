#Write a function in Python to read lines from a text file "Practise_container2.txt". Your function should find and display the occurrence of the word "the" or "The"
#Output : 17



























def TheCounter():
    count = 0
    with open("../Containers/Practise_container2.txt", "r") as File:
        content = File.read()
        words = content.split()  # Split the content into words
        for word in words:
            if word == "the" or word == "The":
                count += 1

    print(count)

TheCounter()
