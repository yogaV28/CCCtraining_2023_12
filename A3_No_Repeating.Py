def length_of_longest_substring(s):
    # Create a dictionary to store the index of each character
    char_index = {}
    max_length = 0
    start = 0

    for end in range(len(s)):
        # If the character is already in the substring, update the start index
        if s[end] in char_index and char_index[s[end]] >= start:
            start = char_index[s[end]] + 1

        # Update the index of the current character
        char_index[s[end]] = end

        # Update the maximum length if needed
        max_length = max(max_length, end - start + 1)

    return max_length

# Input processing
N = int(input())
s = input()

# Find the length of the longest substring without repeating characters
result = length_of_longest_substring(s)
print(result)
