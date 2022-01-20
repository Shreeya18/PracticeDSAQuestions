
# Naive Approach
"""a = [2,4,1,3,5]

Max = 0
for i in range(len(a)):
    if Max < a[i]:
        Max = a[i]
Max1 = 0
a.remove(Max)
print(a)
for j in range(len(a)):
    if Max1 < a[j]:
        Max1 = a[j]

Max2 = 0
a.remove(Max1)
print(a)
for j in range(len(a)):
    if Max2 < a[j]:
        Max2 = a[j]

print(Max2)"""

# Efficient Approach

a = [2, 4, 1, 3, 5]
first = a[0]
second = -1
third = -1
for i in range(1, len(a)):
    if a[i] > first:
        third = second
        second = first
        first = a[i]

    elif a[i] > second:
        third = second
        second = a[i]

    elif a[i] > third:
        third = a[i]

print(third)




