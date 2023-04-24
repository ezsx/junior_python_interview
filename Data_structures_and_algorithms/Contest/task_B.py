def max_ideal_sculptures(N, X, T, sculptures):
    results = []

    for i in range(N):
        time_needed = abs(sculptures[i] - X)
        results.append((time_needed, i))

    results.sort()

    total_time = 0
    ideal_sculptures = []

    for time_needed, i in results:
        if total_time + time_needed <= T:
            total_time += time_needed
            ideal_sculptures.append(i + 1)
        else:
            break

    return len(ideal_sculptures), ideal_sculptures


N, X, T = map(int, input().split())
sculptures = list(map(int, input().split()))

k, ideal_sculptures = max_ideal_sculptures(N, X, T, sculptures)

print(k)
print(" ".join(map(str, ideal_sculptures)))