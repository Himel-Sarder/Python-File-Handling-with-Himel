#Write a function in Python to count words in a Practise_container2.txt file those are ending with alphabet "e".
#Output : 27



























def Ecounter():
    count = 0
    with open("../Containers/Practise_container2.txt", "r") as File:
        content = File.read()
        words = content.split()  # Split the content into words
        for word in words:
            #if word[len(word) - 1] == 'e':
            if word.endswith('e'):
                count += 1

    print(count)

Ecounter()