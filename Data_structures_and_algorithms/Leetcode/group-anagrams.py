strs = ["eat", "tea", "tan", "ate", "nat", "bat"]


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dict_anagrams = {}

        for el in strs:
            if el == "":
                key = ("",)
            else:
                key = tuple(sorted(el))
            dict_anagrams.setdefault(key, []).append(el)

        res = list(dict_anagrams.values())
        return res
