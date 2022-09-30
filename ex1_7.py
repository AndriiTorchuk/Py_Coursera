#Exercise 1: Write a program to read through a file and print the contents
#of the file (line by line) all in upper case. 

fname = input('Enter the file name: ')
t = open(fname)
t = t.read()

textup = t.upper()
print("Upper text: ", textup)
count = 0
for line in t:
    count = count + 1
print('Line Count:', count)

