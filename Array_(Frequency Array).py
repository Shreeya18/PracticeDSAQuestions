P = 5


def f(arr):
    for i in range(1, P + 1):
        for j in range(len(arr)):
            if arr[j] == i:
                arr[i-1] = 0
                arr[i-1] += 1

    return arr


if __name__ == '__main__':
    arr = [2, 3, 2, 3, 5]
    f(arr)
    for i in arr:
        print(i)