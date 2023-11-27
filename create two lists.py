#given list
list = [10, 501, 22, 37, 100, 999, 87, 351]

# Initialize empty lists for even and odd numbers
even_numbers = []
odd_numbers = []

# Iterate through the original list
for num in list:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

# Print the results
print("Original List:", list)
print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)
