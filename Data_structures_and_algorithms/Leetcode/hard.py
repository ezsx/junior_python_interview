s = "ADOBECODEBANC"
t = "ABC"


# нужно найти индексы вхождения элементов из
# из второй строки в первую строку

def find_indexes(s, c):
    indexes = []
    for i in range(len(s)):
        if s[i] == c:
            indexes.append(i)
    return indexes


def all_indexes(s, t):
    res = []
    for let in t:
        res.append(find_indexes(s, let))
    return res


print(all_indexes(s, t))


def merge(arr):
    res_arr = []
    for el in arr:
        res_arr += el
    return sorted(res_arr)


def librar(t, arr):
    res_arr = {}
    for i in range(len(arr)):
        res_arr.update({t[i]: arr[i]})
    return res_arr


print(merge(all_indexes(s, t)))
print(librar(t, all_indexes(s, t)))

# нужно найти такие индексы которые
# находятся к друг другу ближе всего и
# покрывают нашу строку
