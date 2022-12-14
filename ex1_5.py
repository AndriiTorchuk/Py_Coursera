#Exercise 1: Write a program which repeatedly reads numbers until the
#user enters “done”. Once “done” is entered, print out the total, count,
#and average of the numbers. If the user enters anything other than a
#number, detect their mistake using try and except and print an error
#message and skip to the next number.
#Enter a number: 4
#Enter a number: 5
#Enter a number: bad data
#Invalid input
#Enter a number: 7
#Enter a number: done
#16 3 5.333333333333333

sum = 0
count = 0

while True:
    dat = input("Enter data: ")
    
    if dat == 'done':
        break
    try:
        dat = int(dat)
        sum = sum + dat
        count = count + 1
    except:
        print("Only numbers, please")
        continue
     
print ("We finished ", "Sum =", sum, "Average =", sum/count)


#Exercise 2: Write another program that prompts for a list of numbers
#as above and at the end prints out both the maximum and minimum of
#the numbers instead of the average.
print("============================================")
lis = []

while True:
    inp = input ("Enter number: ")
    if inp == 'done':
        break
    try:
        inp = int(inp)
        lis.append(inp)
        
    except:
        print("Only numbers, please")
        continue

print("List of numbers is: ", lis)

larg = lis[0]
for i in lis:
    if i > larg:
        larg = i
print("Largest numver is: ", larg)
