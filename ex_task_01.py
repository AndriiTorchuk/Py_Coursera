# Print all odd numbers between min and max.

min_value = input("Enter min value: ")
max_value = input("Enter max value: ")

min_value = int(min_value)
max_value = int(max_value)

for odd_num in range(min_value, max_value + 1):
    if odd_num % 2 != 0:
        print(odd_num)