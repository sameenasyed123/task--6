#print first and last digit integer

def sum_of_first_and_last_digit(number):
    number_str = str(number)
    return int(number_str[0]) + int(number_str[-1])

# Get input from the user
user_input = int(input("Enter an integer: "))

# Calculate and display the result
result = sum_of_first_and_last_digit(user_input)
print(f"The sum of the first and last digits of {user_input} is: {result}")
