# A text file named "Practise_container3.txt" contains some text, which needs to be displayed such that every next character is separated by a symbol "_". Write a function definition for Modified() in Python that would display the entire content of the file Practise_container.txt in the desired format.
# Sample Output : H_i_ _I_ _a_m_ _H_i_m_e_l_ _S_a_r_d_e_r_



























def Modified():
    with open("../Containers/Practise_container3.txt", "r") as File:
        content = File.read()
        #NewContent = ""
        for char in content:
            #NewContent += char + "_"
            print(char, end="_")

Modified()