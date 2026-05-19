def rotate_right_inplace(arr, k):
    n = len(arr)
    if not n:
        return
    k = k % n

    def reverse(l, r):
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)

print("Enter the list of numbers (comma separated):")
arr = list(map(int, input().split(',')))
print("Enter the number of positions to rotate right:")
k = int(input())
rotate_right_inplace(arr, k)
print(arr)