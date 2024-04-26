# Write a Python program to get the file size of Practise_container2.txt file.
# Output : File size in bytes of a plain file:  828



























def FileSize(fname):
    import os
    Information = os.stat(fname)
    return Information.st_size


print("File size in bytes of a plain file: ", FileSize("../Containers/Practise_container2.txt"))
