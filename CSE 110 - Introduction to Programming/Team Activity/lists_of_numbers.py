numbers = []

# Step 1: Ask for numbers
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    numbers.append(num)

# Step 2: Compute the sum
total = sum(numbers)
print(f"The sum is: {total}")

# Step 3: Compute the average
if numbers:
    average = total / len(numbers)
    print(f"The average is: {average}")

# Step 4: Find the largest number
if numbers:
    largest = max(numbers)
    print(f"The largest number is: {largest}")

# Step 5: Find the smallest positive number
positive_numbers = [num for num in numbers if num > 0]
if positive_numbers:
    smallest_positive = min(positive_numbers)
    print(f"The smallest positive number is: {smallest_positive}")

# Step 6: Sort the list and display it
sorted_numbers = sorted(numbers)
print("The sorted list is:")
for num in sorted_numbers:
    print(num)
