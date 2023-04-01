def flipgame(fronts, backs):
    # Create a set of numbers that appear on both sides of a card
    same = set(fronts[i] for i in range(len(fronts)) if fronts[i] == backs[i])

    # Find the smallest number that doesn't appear on both sides of any card
    smallest = float('inf')
    for num in fronts + backs:
        if num not in same:
            smallest = min(smallest, num)

    return smallest if smallest != float('inf') else 0
