a = [15, -2, 2, -8, 1, 7, 10, 23]
n = len(a)
Sum = 0
dic = {}
start = 0
end = -1
curSum = 0
mini = len(a)
for i in range(n):
    curSum += a[i]
    if curSum == Sum:
        start = 0
        end = i
    if (curSum - Sum) in dic.values():
        start = dic.get(curSum - Sum) + 1
        end = i
        if (end-start) > mini:
            mini = (end - start) + 1
    else:
        dic.__setitem__(curSum, i)

for i in range(start, end+1):
    print(i)

print("maxArr = ", mini)