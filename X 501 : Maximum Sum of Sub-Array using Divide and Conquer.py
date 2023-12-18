def max_crossing_sum(arr, low, mid, high):
    left_sum = float('-inf')
    sum = 0
    for i in range(mid, low - 1, -1):
        sum += arr[i]
        if sum > left_sum:
            left_sum = sum

    right_sum = float('-inf')
    sum = 0
    for i in range(mid + 1, high + 1):
        sum += arr[i]
        if sum > right_sum:
            right_sum = sum

    return left_sum + right_sum


def max_subarray_sum(arr, low, high):
    if low == high:
        return arr[low]

    mid = (low + high) // 2

    left_sum = max_subarray_sum(arr, low, mid)
    right_sum = max_subarray_sum(arr, mid + 1, high)
    crossing_sum = max_crossing_sum(arr, low, mid, high)

    return max(left_sum, right_sum, crossing_sum)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    result = max_subarray_sum(arr, 0, n - 1)
    print(result)
