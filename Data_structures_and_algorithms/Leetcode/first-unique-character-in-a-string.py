s = "leetcode"

d = {}
for el in s:
    if el not in d:
        d.update({el: 1})
    else:
        d[el] += 1
print(d)
for el in d:
    if d[el]==1:
        print(s.index(el))