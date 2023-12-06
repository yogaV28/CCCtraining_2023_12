def findMedianSortedArrays(nums1, nums2):
    # Combine the two arrays into a single sorted array
    merged = sorted(nums1 + nums2)

    # Find the median based on the length of the combined array
    n = len(merged)
    if n % 2 == 0:
        # If the length is even, return the average of the middle two elements
        return (merged[n // 2 - 1] + merged[n // 2]) / 2
    else:
        # If the length is odd, return the middle element
        return merged[n // 2]

# Input processing
N, M = map(int, input().split())
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

# Find the median of the two sorted arrays
result = findMedianSortedArrays(nums1, nums2)
print(result)
