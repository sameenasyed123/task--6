def find_minimum_element(sorted_list):
    # Check if the list is not empty
    if not sorted_list:
        return None
    
    # The minimum element in a sorted list is the first element
    return sorted_list[0]

# Given sorted list
sorted_numbers = [2, 5, 8, 12, 15, 18, 22]

# Find the minimum element
min_element = find_minimum_element(sorted_numbers)

# Print the result
if min_element is not None:
    print(f"The minimum element in the list is: {min_element}")
else:
    print("The list is empty.")
