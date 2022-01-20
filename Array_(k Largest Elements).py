print("I Love Python")


"""
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i - 1
    if left < n and arr[largest] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)
    for i in range(n//2-1, -1, -1):
        heapify(arr, n, i)


arr = [5, 8, 10, 4, 3, 15]
k = 3
s = []
def kP():
    s = []
    for j in range(k):
        heapify(arr, len(arr), 0)
        s.append(arr[0])
        arr.remove(arr[0])
    return s"""


"""ans = kP()
for j in ans:
    print(j)"""


class Solution:
    def heapify(self, arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[largest] < arr[i]:
            largest = left
        if right < n and arr[largest] < arr[right]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

    def delete(self,arr, ele):
        n = len(arr)
        for i in range((len(arr) // 2) - 1, -1, -1):
            self.heapify(arr, len(arr), i)
        d = arr[0]
        arr.remove(d)
        return d


    def kLargest(self,arr, n, k):
        s = []
        for i in range(k):
            u = self.delete(arr, arr[0])
            s.append(u)
        return s

sol = Solution()
arr = [8, 9, 15, 10, 4, 7]
n = len(arr)
k = 3
ans = sol.kLargest(arr, n, k)
for i in ans:
    print(i)
