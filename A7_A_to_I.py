def myAtoi(s):
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    # Remove leading whitespaces
    s = s.lstrip()

    # Check if the string is empty
    if not s:
        return 0

    # Check if the number is positive or negative
    sign = 1
    if s[0] in ['-', '+']:
        sign = -1 if s[0] == '-' else 1
        s = s[1:]

    # Read in characters until a non-digit or the end of the string is reached
    result = 0
    for char in s:
        if char.isdigit():
            result = result * 10 + int(char)
        else:
            break

    # Apply sign and clamp the result to the 32-bit signed integer range
    result *= sign
    result = max(min(result, INT_MAX), INT_MIN)

    return result

# Input processing
s = input()

# Find the integer using myAtoi and print the result
result = myAtoi(s)
print(result)
