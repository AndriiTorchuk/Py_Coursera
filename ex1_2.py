# Exercises 1
# Exercises 2

inp = input("Write you name: ")
print ("Hello ", inp)

# Exercises 3


wh = input("How much are you working weekly?")
hr = input("What is your hour rate?")
print ("This week earning is: ", int(wh)*int(hr))

# Exercises 4

width = 17
height = 12.0

val = width//2
typ = type(val)
print("Value: ", val, "Type: ", typ)
val = width/2.0
typ = type(val)
print("Value: ", val, "Type: ", typ)
val = height/3
typ = type(val)
print("Value: ", val, "Type: ", typ)
val = 1 + 2 *5
typ = type(val)
print("Value: ", val, "Type: ", typ)

# Exercises 5

cel = input("Write temperature in Cel:")
print("Temperature in F: ", int(cel)*9/5 + 32)