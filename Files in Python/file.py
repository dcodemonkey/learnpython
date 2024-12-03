# file I/O in python: reading and writing files
# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

f = open("demo.txt", 'r') # open file in read mode
data = f.read(5)
print(data)
f.close()

new_file = open("sample.txt", 'w') # open file in write mode if file name does not exist, else it will create the file.

new_file.write("Test")

f.close()

g = open('sample.txt', 'a')

g.write("Hey! This is a new line in the file.\n")

g.close()