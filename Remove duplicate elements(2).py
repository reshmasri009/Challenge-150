def remove_duplicates(arr):
    if not arr:
        return 0
    arr.sort()   
    i = 0
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
    return i + 1
arr = [23, 7, 23, 70, 42, 67]
i = remove_duplicates(arr)
print(i, arr[:i])
