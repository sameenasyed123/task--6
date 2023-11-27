def find_sublist_with_sum_zero(nums):
    # Iterate through the list
    for i in range(len(nums)):
        current_sum = 0
        # Check for sublists with sum equal to zero
        for j in range(i, len(nums)):
            current_sum += nums[j]
            if current_sum == 0:
                return nums[i:j+1]
    # If no sublist is found
    return None

# Given list
numbers = [4, 2, -3, 1, 6]

# Find a sublist with sum equal to zero
result = find_sublist_with_sum_zero(numbers)

# Print the result
if result is not None:
    print(f"A sublist with sum zero is: {result}")
else:
    print("No sublist with sum zero found.")
