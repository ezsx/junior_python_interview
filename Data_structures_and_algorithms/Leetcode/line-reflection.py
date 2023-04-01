class Solution:
    def isReflected(self, points: list[list[int]]) -> bool:
        if not points:
            return True

        x_sum = 0
        point_set = set()
        for point in points:
            x_sum += point[0]
            point_set.add((point[0], point[1]))

        x_reflection = x_sum / len(points)
        for point in points:
            mirror_point = (2 * x_reflection - point[0], point[1])
            if mirror_point not in point_set:
                return False

        return True
