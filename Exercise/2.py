#Write a function in python to count the number of lines from a text file "Practise_container2.txt" which is not starting with an alphabet "T".
#The function should display the output as 6



























def LineCounter():
    count = 0
    with open("../Containers/Practise_container2.txt","r") as File:
        for line in File:
            if line[0] not in "T":
                count += 1
        File.close()

    print(count)

LineCounter()