s = "1203"
t = "1213"
flag = 0
i_l = 0
i_r = 0
while s and t != '':
    if s[:1] == t[:1]:
        s = s[1:]
        t = t[1:]
        i_l += 1
    else:
        break
    if s[-1] == t[-1]:
        s = s[:-1]
        t = t[:-1]
        i_r += 1
    else:
        break
print(i_l,i_r)
print(s)
print(t)
