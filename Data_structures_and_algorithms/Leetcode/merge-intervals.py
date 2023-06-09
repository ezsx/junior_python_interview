# intervals [[1, 3], [2, 6], [8, 10], [15, 18]]
# intervals.sort [[1, 3], [2, 6], [8, 10], [15, 18]]
#
# interval = [1,3]
# merged =[]
# not merged:
# 	merged =[ [1,3] ]
#
# interval =[2,6]
# merged = [ [1,3] ]
# merged[-1][-1] = 3 > interval[0] = 2:
# 	merged[-1][-1] = max(merged[-1][-1] = 3 ,interval[-1] = 6) =6
# merged = [[1,6]]
# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         intervals.sort(key =lambda x: x[0])
#         merged =[]
#         for i in intervals:
# 			# if the list of merged intervals is empty
# 			# or if the current interval does not overlap with the previous,
# 			# simply append it.
#             if not merged or merged[-1][-1] < i[0]:
#                 merged.append(i)
# 			# otherwise, there is overlap,
# 			#so we merge the current and previous intervals.
#             else:
#                 merged[-1][-1] = max(merged[-1][-1], i[-1])
#         return merged


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        merged = []
        for i in range(len(intervals)):
            if merged == []:
                merged.append(intervals[i])
            else:
                previous_end = merged[-1][1]
                current_start = intervals[i][0]
                current_end = intervals[i][1]
                if previous_end >= current_start:  # overlap
                    merged[-1][1] = max(previous_end, current_end)
                else:
                    merged.append(intervals[i])
        return merged
