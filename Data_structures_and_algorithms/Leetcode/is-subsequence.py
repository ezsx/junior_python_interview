s = "abc"
t = "ahbgdc"

count_s = 0
for el in t:
    if s[count_s] == el:
        count_s += 1
print(count_s == len(s))
