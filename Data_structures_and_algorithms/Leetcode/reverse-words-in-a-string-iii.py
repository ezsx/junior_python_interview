class Solution:
    def reverseWords(self, s: str) -> str:
        string_list = s.split(" ")
        str_res=""
        for i in range(len(string_list)):
            str_res+=string_list[i][::-1]+" "
        return str_res[:-1]