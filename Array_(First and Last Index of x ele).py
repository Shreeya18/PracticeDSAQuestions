print("Hello World!")

v = [1, 4, 7, 7, 7, 7, 8]
x = 7
# Binary Search
start = 0
end = len(v) - 1
while start < end:
    mid = (start + end) // 2
    if v[mid] == x:
        print(mid)
    if x < v[mid]:
        end = mid - 1
    if x > v[mid]:
        start = mid + 1
    else:
        print(-1)