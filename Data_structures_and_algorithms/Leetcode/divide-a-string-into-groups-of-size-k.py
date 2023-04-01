s = "abcdefghilllp"
k = 3
fill = "x"
list_s = []
while s != "":
    list_s += [s[:k]]
    s = s[k:]
while len(list_s[-1]) < k:
    list_s[-1] += fill
print(list_s)
