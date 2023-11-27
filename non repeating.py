def first_non_repeating_element(nums):
    count_dict = {}
    
    # Count the occurrences of each number in the list
    for num in nums:
        count_dict[num] = count_dict.get(num, 0) + 1
    
    # Find the first non-repeating element
    for num in nums:
        if count_dict[num] == 1:
            return num

    # If no non-repeating element is found
    return None

# Given list
numbers = [10, 3, 5, 10, 5, 8, 3, 7]

# Find the first non-repeating element
result = first_non_repeating_element(numbers)

# Print the result
if result is not None:
    print(f"The first non-repeating element is: {result}")
else:
    print("There is no non-repeating element in the list.")
