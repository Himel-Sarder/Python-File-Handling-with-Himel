# Write a Python program to read a random line from Practise_container3.txt file.




























import random
def RandomLine():
    lines = open("../Containers/Practise_container3.txt").read().splitlines()
    print(random.choice(lines))

RandomLine()
