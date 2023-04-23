
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        def str2int(num):
            numDict = {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5,
                       '6' : 6, '7' : 7, '8' : 8, '9' : 9}
            output = 0
            for d in num:
                output = output * 10 + numDict[d]
            return output

        return str(str2int(num1) + str2int(num2))

#
# arr = [1, 2, 3, 4, 5, 9, 10, 11, 13]+[0]
# result = "1->5, 9->11, 13"
# res = ""
# lastel = 0
# for i in range(1, len(arr)):
#     if arr[i] - arr[i - 1] != 1:
#         res += f"{arr[lastel]}->{arr[i - 1]}, " if lastel != i - 1 else f"{arr[lastel]}, "
#         lastel = i
# print(res[:-2])
