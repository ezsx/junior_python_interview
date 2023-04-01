# Generate question numbers and their weights
n = 6
questions = {}
idx = 0
for i in range(n):
    for j in range(n-i):
        idx += 1
        questions[idx] = 2*i+j

# Sort questions in descending order of weight
sorted_questions = sorted(questions.items(), key=lambda xx: xx[1], reverse=True)

# Remove any extra questions
n_all = len(sorted_questions)
n_one = 3
n_ticket = n_all // n_one
n_off = n_all - n_ticket * n_one
if n_off > 0:
    sorted_questions = sorted_questions[:-n_off]

# Find first and second range boundaries for assigning questions to tickets
n_range1 = (n_one // 2) * n_ticket
n_range2 = (n_one // 2 + (n_one % 2)) * n_ticket

# Create list of tickets
ticket_list = [[] for _ in range(n_ticket)]

# Assign questions to tickets
for idx, q in enumerate(sorted_questions):
    if idx < n_range1:
        x = idx % n_ticket
    elif idx >= n_range2:
        x = (n_ticket - 1) - (idx % n_ticket)
    elif idx >= n_range1 and idx < n_range2:
        if idx % 2:
            x = idx % n_ticket
        else:
            x = (n_ticket - 1) - (idx % n_ticket) - 1
    ticket_list[x].append(q)

# Print ticket contents and total weight
for ticket in ticket_list:
    print(ticket)
    print(sum([t[1] for t in ticket]))
