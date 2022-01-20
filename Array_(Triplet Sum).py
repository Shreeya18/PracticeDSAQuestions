
a = [557, 217, 627, 358, 527, 358, 338, 272, 870, 362, 897, 23, 618, 113, 718, 697, 586, 42, 424, 130, 230,
     566, 560, 933]
n = len(a)
a = sorted(a)
x = 986
i = 1
j = 2
f = []
while True:
    k = a[i] + a[j]
    for s in range(n):
        if i == s or j == s:
            continue
        elif a[s] == (x-k):
            m = a[s]
            f.append(a[i])
            f.append(a[j])
            f.append(a[s])

    if len(f) != 0:
        print(f)
        break
    elif j < n-1:
        j += 1
    elif j == n-1 and i < n-1:
        i += 1
    else:
        break

if f:
    for i in range(len(f)):
        print(f[i])
else:
    print(None)




