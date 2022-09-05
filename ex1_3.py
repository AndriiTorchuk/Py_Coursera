#Exercise 1: Rewrite your pay computation to give the employee 1.5
#times the hourly rate for hours worked above 40 hours.
#Enter Hours: 45
#Enter Rate: 10
#Pay: 475.0

hrs = input("How many hours ?")
hrs = int(hrs)
if hrs <= 40:
    print ("Pay: ", hrs*10)
else:
    print ("Pay: ", (hrs-40)*10*1.5 + 40*10)

#Exercise 2: Rewrite your pay program using try and except so that your
#program handles non-numeric input gracefully by printing a message
#and exiting the program. The following shows two executions of the
#program:
#Enter Hours: 20
#Enter Rate: nine
#Error, please enter numeric input
#Enter Hours: forty
#Error, please enter numeric input

hrs = input("How many hours ?")
rate = input("Enter rate ?") 
try:
    hrs = int(hrs)
    rate = int(rate)
    if hrs <= 40:
        print ("Pay: ", hrs*rate)
    else:
        print ("Pay: ", (hrs-40)*rate*1.5 + 40*rate)

except:
    print ("Please enter numeric input")

#Exercise 3: Write a program to prompt for a score between 0.0 and
#1.0. If the score is out of range, print an error message. If the score is
#between 0.0 and 1.0, print a grade using the following 
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F

score = input ("What is your score?")
score = float(score)

      
if score >= 0.0 and score <= 1.0:
    if score >= 0.9:
        print("Your grade is A")
    elif score >= 0.8:
        print("Your grade is B")
    elif score >= 0.7:
        print("Your grade is C")
    elif score >= 0.6:
        print("Your grade is D")
    elif score < 0.6:
        print("Your grade is F")
else:
    print("Score must be between 0.0 and 1.0")
