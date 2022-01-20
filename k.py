

a = [557, 217, 627, 358, 527, 358, 338, 272, 870, 362, 897, 23, 618, 113, 718, 697, 586, 42, 424, 130, 230,
     566, 560, 933]
n = len(a)
for i in range(n):
    for j in range(n):
        for k in range(n):
            if a[i] + a[j] + a[k] == 986:
                print(a[i], a[j], a[k])