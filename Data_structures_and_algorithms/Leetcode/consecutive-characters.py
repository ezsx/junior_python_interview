s = "abbcccddddeeeeedcba"

print(s[1:])
cur = s[:1]
s = s[1:]
cur_num = 1
max_num = 0
while s != "":
    if s[:1] == cur:
        cur_num += 1
    else:
        cur = s[:1]
        cur_num = 1
    max_num = max(max_num, cur_num)
    s = s[1:]
print(max_num)