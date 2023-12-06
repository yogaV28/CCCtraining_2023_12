
def isPalindrome(x):
    str_x = str(x)

    return str_x == str_x[::-1]

x = int(input())


result = isPalindrome(x)
print(str(result).lower())
