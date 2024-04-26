'''
"Abonti, the princess of Himland, wants to send an encrypted message to her beloved prince, Antu, so that no one can read it.
Long ago, the prince suggested to her that if she wanted to send him an encrypted message, she should replace all occurrences
of 'M' with 'A', maintaining the case (capital to capital and lowercase to lowercase). Can you help her replace all 'M's with 'A's?"
'''
#Sample Output : PLAASA Maat with ma (PLEASE Meet with me)























def Encrypted():
    with open("../Containers/Practise_container3.txt", "r") as File:
        content = File.read()
        new = content.replace('E', 'A').replace('e', 'a')
        print(new)

Encrypted()