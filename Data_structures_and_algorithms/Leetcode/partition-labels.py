s = "ababcbacadefegdehijhklij"
# print(set(s))
L = len(s)
last = {s[i]: i for i in range(L)}  # last appearance of the letter
print(last)
i, ans = 0, []
while i < L:
    end = last[s[i]]
    j = i + 1
    while j < end:  # validation of the part [i, end]
        if last[s[j]] > end:
            end = last[s[j]]  # extend the part
        j += 1
    ans.append(end - i + 1)
    i = end + 1
print(ans)
