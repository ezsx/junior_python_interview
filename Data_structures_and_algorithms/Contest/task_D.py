def find_countries(N, min_incomes, higher_ed_req, family_reloc, Q, classmates_income, classmates_higher_ed,
                   parents_citizenship):
    countries_no_higher_ed = sorted([(min_incomes[i], i) for i in range(N) if not higher_ed_req[i]])
    countries_higher_ed = sorted([(min_incomes[i], i) for i in range(N) if higher_ed_req[i]])

    result = []
    for i in range(Q):
        income = classmates_income[i]
        higher_ed = classmates_higher_ed[i]
        parent_citizenship = parents_citizenship[i]

        suitable_country = 0
        if parent_citizenship > 0 and family_reloc[parent_citizenship - 1] == 1:
            suitable_country = parent_citizenship
        else:
            countries_to_check = countries_higher_ed if higher_ed else countries_no_higher_ed
            for min_income, idx in countries_to_check:
                if income >= min_income:
                    suitable_country = idx + 1
                    break

        result.append(suitable_country)

    return result


# Read input values
N = int(input())
min_incomes = list(map(int, input().split()))
higher_ed_req = list(map(int, input().split()))
family_reloc = list(map(int, input().split()))

Q = int(input())
classmates_income = list(map(int, input().split()))
classmates_higher_ed = list(map(int, input().split()))
parents_citizenship = list(map(int, input().split()))

# Find the countries each classmate can move to
result = find_countries(N, min_incomes, higher_ed_req, family_reloc, Q, classmates_income, classmates_higher_ed,
                        parents_citizenship)

# Print the result
print(" ".join(map(str, result)))
