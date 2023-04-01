# cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
cost = [10, 15, 20]

pathes = []


def rec(i):
    if i <= 1:
        return cost[i]
    else:
        return min(rec(i - 1), rec(i - 2)) + cost[i]


def minCostClimbingStairs(cost):
    cost.append(0)
    for i in range(len(cost) - 3, -1, -1):
        cost[i] += min(cost[i + 1], cost[i + 2])
    return min(cost[0], cost[1])
