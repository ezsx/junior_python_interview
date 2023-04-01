s1 = "hello"
s2 = "ooolleoooleh"

n = len(s1)
for i in range(len(s2) - n + 1):
    substring = s2[i:i+n]
    if sorted(s1) == sorted(substring):
        print(s1, substring)
        print(set(s1),set(substring))
        print(True)
        break
print("NO")