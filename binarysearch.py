# write a program to perform binary search using recursion.
def B_rec(arr, first, last, x):
    if last >= first:
        mid = (first + last) // 2
        if arr[mid] == x:
            return mid
        elif x > arr[mid]:
            return B_rec(arr, mid + 1, last, key)
        else:
            return B_rec(arr, first, mid - 1, key)
    else:
        return -1


a = []
n = int(input())
for i in range(n):
    y = int(input())
    a.append(y)
key = int(input())
ans = B_rec(a, 0, n - 1, key)
print(ans + 1)