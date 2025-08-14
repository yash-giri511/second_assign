# task 1: check if a number is even or odd

#take input from the user
num = int(input("Enter a number: "))

#check whether the number is even or odd
if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")

#task2: sum of integers from 1 to 50 using a loop

#initialize sum variable
total_sum = 0

#loop through number 1 to 50
for i in range(1, 51):
    total_sum += i

print(f"the sum of numbers from 1 to 50 is: {total_sum}")