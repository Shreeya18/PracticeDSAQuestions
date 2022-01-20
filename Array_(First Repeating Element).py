def firstRepeated(arr, n):
    dic = {}
    mini = -1
    for i in range( n -1 ,-1 ,-1):
        if arr[i] in dic.keys():
            mini = i + 1
        else:
            dic.__setitem__(arr[i], i)
    return mini


arr = [10, 5, 3, 4, 3, 5, 6]

n = len(arr)
print(firstRepeated(arr, n))