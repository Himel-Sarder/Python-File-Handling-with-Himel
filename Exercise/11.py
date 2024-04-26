# Write a python program to find the longest word in the Practise_container3.txt file.
# Output : Bangladesh



























def LongestWord():
    with open("../Containers/Practise_container3.txt", 'r') as File:
              words = File.read().split()
    MaxLength = len(max(words, key=len))
    for word in words:
        if len(word) == MaxLength:
            print(word)

LongestWord()