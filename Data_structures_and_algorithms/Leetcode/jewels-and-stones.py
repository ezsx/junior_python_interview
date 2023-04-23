jewels = "aA"

stones = "aAAbbbb"

d = {}
for char in stones:
    d.setdefault(char, 0)
    d[char] += 1
count = 0
for i in jewels:
    if i in d:
        count += d[i]
print(count)
