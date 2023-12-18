def longest_onely_sequence(n, m, arr):
    left = 0
    right = 0
    max_len = 0
    max_left = 0
    zero_count = 0

    while right < n:
        if arr[right] == 0:
            zero_count += 1

        while zero_count > m:
            if arr[left] == 0:
                zero_count -= 1
            left += 1

        if right - left + 1 > max_len:
            max_len = right - left + 1
            max_left = left

        right += 1

    return max_left + 1, max_left + max_len

# Input reading
n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Function call and output printing
start, end = longest_onely_sequence(n, m, arr)
print(start, end)
