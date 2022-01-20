print("I Love Python!")

dic = {}
s= "hheelloo"

for i in range(len(s)):
    if s[i] in dic:
        dic[s[i]] += 1
    else:
        dic.__setitem__(s[i], i)

for i in s:
    if dic[i] == 1:
        print(i)
        break



