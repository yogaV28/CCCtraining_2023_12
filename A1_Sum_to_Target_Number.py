def two_sum(nums, target):
    # Create a dictionary to store the complement of each element
    complement_dict = {}

    for i, num in enumerate(nums):
        complement = target - num

        # Check if the complement is in the dictionary
        if complement in complement_dict:
            # If found, return the indices of the two numbers
            return [complement_dict[complement], i]
        
        # Otherwise, add the current element and its index to the dictionary
        complement_dict[num] = i

# Input processing
N = int(input())
nums = list(map(int, input().split()))
target = int(input())

# Find the indices and print the result
result = two_sum(nums, target)
print(result[0], result[1])
