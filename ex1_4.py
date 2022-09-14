#Exercise 6: Rewrite your pay computation with time-and-a-half for 
# overtime and create a function called computepay which takes two parameters
#(hours and rate).
#Enter Hours: 45
#Enter Rate: 10
#Pay: 475.0

hours = input ("How many hours? ")
hours = int(hours)
rate = input ("What is rate? ")
rate = int(rate)

def computepay():
    if hours <= 40:
        print ("Pay = ", hours*rate)
    else:
        print ("Pay = ", 400+(hours-40)*rate*1.5)

computepay()

#Exercise 7: Rewrite the grade program from the previous chapter using
#a function called computegrade that takes a score as its parameter and
#returns a grade as a string.
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#Enter score: 0.95 A

score = input("What is your score? ")
score = float(score) 

def computegrade():
    if score >= 0.9:
        print ("Your grade is: A")
    elif score >= 0.8:
        print ("Your grade is: B")
    elif score >= 0.7:
        print ("Your grade is: C")
    elif score >= 0.6:
        print ("Your grade is: D")
    elif score <= 0.6:
        print ("Your grade is: E")
    

computegrade()