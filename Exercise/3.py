#Write a function in Python to count and display the total number of words in Practise_container.txt file.
#Output : 136



























def WordCounter():
    count = 0
    with open("../Containers/Practise_container.txt", "r") as File:
        file = File.read()
        words = file.split()
        for w in words:
                count += 1
        File.close()

    print(count)

WordCounter()


'''
---------------
Description:
----------------

The split() method in Python is used to split a string into a list of substrings based on a specified separator. Here are some common uses of the split() method:

Splitting a String into Words: 
==============================
You can split a sentence or paragraph into a list of words by using whitespace as the separator.

sentence = "This is a sample sentence."
words = sentence.split()
print(words)  # Output: ['This', 'is', 'a', 'sample', 'sentence.']


Splitting a String by a Specific Separator: 
===========================================
You can split a string based on a specific character or substring.

data = "apple,banana,orange"
fruits = data.split(",")
print(fruits)  # Output: ['apple', 'banana', 'orange']


Splitting Lines in a Text File: 
==============================
You can split the lines of a text file into a list of strings.

with open("file.txt", "r") as file:
    lines = file.read().splitlines()
print(lines)


Limiting the Number of Splits: 
==============================
You can specify the maximum number of splits using the maxsplit parameter.

sentence = "apple banana orange grape"
words = sentence.split(maxsplit=2)
print(words)  # Output: ['apple', 'banana', 'orange grape']


Removing Empty Strings: 
=======================
By default, split() includes empty strings in the result if there are consecutive separators. You can remove them by passing maxsplit=0.


data = "apple,,banana,,orange"
fruits = data.split(",")
print(fruits)  # Output: ['apple', '', 'banana', '', 'orange']

fruits = data.split(",", maxsplit=0)
print(fruits)  # Output: ['apple', 'banana', 'orange']


Splitting a String into Characters: 
===================================
Although not common, you can split a string into individual characters by passing an empty string as the separator.

word = "hello"
characters = list(word)
print(characters)  # Output: ['h', 'e', 'l', 'l', 'o']
'''