def reverse(x):
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    # Check if the number is negative
    sign = 1
    if x < 0:
        sign = -1
        x = abs(x)

    # Reverse the digits
    reversed_x = int(str(x)[::-1]) * sign

    # Check if the reversed number is within the 32-bit integer range
    if reversed_x < INT_MIN or reversed_x > INT_MAX:
        return 0

    return reversed_x

# Input processing
x = int(input())

# Find the reversed integer and print the result
result = reverse(x)
print(result)
