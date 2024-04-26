# How do you lock a file in Python to prevent other processes from accessing it?




























import fcntl

# Open the file in read-write mode
file = open("example.txt", "r+")

# Acquire an exclusive lock on the file
fcntl.flock(file, fcntl.LOCK_EX)

# Now the file is locked, and other processes cannot access it

# Perform operations on the file

# Release the lock
fcntl.flock(file, fcntl.LOCK_UN)

# Close the file
file.close()
