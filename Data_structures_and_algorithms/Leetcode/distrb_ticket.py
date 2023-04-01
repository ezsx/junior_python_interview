# Генерим номера вопросов и их вес
from random import randint
d = {i: randint(1, 5) for i in range(20)}
# print(d)

# получаем отсортированный в порядке убывания список вопросов (номер_вопроса, вес)
list_ord = list(d.items())
list_ord = sorted(list_ord, key=lambda xx: xx[1], reverse=True)
# print(list_ord)
# общее число вопросов
n_all = len(list_ord)
# кол-во вопросов в билете
n_one = 4

# находим кол-во билетов
n_ticket = n_all // n_one
print(n_ticket)

# Сколько вопросов лишних?
n_off = n_all - n_ticket * n_one
# уберем n_off простых вопросов (возможно логичнее убирать с конца и с начала
# типо сложный и простой)
if n_off > 0:
    list_ord = list_ord[:-n_off]
print(list_ord)
# Находим первую и вторую границы серединных вопросов в списке
n_range1 = (n_one // 2) * n_ticket
n_range2 = (n_one // 2 + (n_one % 2)) * n_ticket
print(n_range1, n_range2)
# list сбалансированных билетов (результат)
ticket_list = [[] for _ in range(n_ticket)]

# перебираем все вопросы и назначем им номера билетов
for idx, q in enumerate(list_ord):
    # если индекс из первой половины
    # отсортированного в обратном порядке списка
    if idx < n_range1:
        # номер билета - x
        x = idx % n_ticket
    elif idx >= n_range2:
        x = (n_ticket - 1) - (idx % n_ticket)
    elif (idx >= n_range1) and (idx < n_range2):
        if idx % 2:
            x = (idx % n_ticket)
        else:
            x = (n_ticket - 1) - (idx % n_ticket) -1
    ticket_list[x].append(q)

# Результат
for ticket in ticket_list:
    print(ticket)
    print(sum([t[1] for t in ticket]))
