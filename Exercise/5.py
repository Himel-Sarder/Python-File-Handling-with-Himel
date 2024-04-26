#Write a function display_words() in python to read lines from a text file "Practise_container.txt", and display those words, which are less than 5 characters.
#Output : 90



























def FourWCounter():
    count = 0
    with open("../Containers/Practise_container2.txt", "r") as File:
        content = File.read()
        words = content.split()  # Split the content into words
        for word in words:
            if len(word) <= 5:
                count += 1

    print(count)

FourWCounter()