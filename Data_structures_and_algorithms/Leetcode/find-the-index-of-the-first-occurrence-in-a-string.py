s = "abab"
def repeatedSubstringPattern( s: str) -> bool:
    if not s:
        return False
    ss = (s + s)[1:-1]
    print(ss)
    return ss.find(s) != -1
print(repeatedSubstringPattern(s))
