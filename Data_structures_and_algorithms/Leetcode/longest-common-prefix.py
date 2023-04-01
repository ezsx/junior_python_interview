strs = ["dog","racecar","car"]


str_ = ""
for i in zip(*strs):
    if all(elem == i[0] for elem in i):
        str_ += i[0]
    else:
        break
print(str_)
