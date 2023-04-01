from random import randint

rnd = [randint(0, 1) for i in range(20)]
print(rnd)


def find_max_gap(arr):
    m_gap = (0, 0)
    cur_gap = (0, 0)
    save_len = len(arr)
    arr = [-1] + arr + [-1]
    for i in range(0, save_len):
        if arr[i] != arr[i - 1]:
            if abs(cur_gap[0] - cur_gap[1]) > abs(m_gap[0] - m_gap[1]) and arr[i] != 0:
                m_gap = cur_gap
            cur_gap = (i - 1, i)
        else:
            cur_gap = (cur_gap[0], i)
    m_gap = (m_gap[0] + 1, m_gap[1])
    return m_gap


def chose_sit(m_gap):
    sum_ = abs(m_gap[1] - m_gap[0]) + 1
    if m_gap[0] == 1 or m_gap[1] == m_gap[:-2]:
        print(sum_)
    elif sum_ % 2 == 0:
        print((sum_ // 2))
    else:
        print(sum_ // 2 + 1)


def findb(a):
    # вернет самый длинный интервал нулей
    # в цикле ищем и запоминаем начало нулей и их длину
    p, cur_len = 0, 0
    max_g = (-1, -1)
    for i in range(len(a)):
        if a[i] == 0:
            if cur_len == 0:
                p = i
            cur_len += 1
        else:
            if cur_len > max_g[1]:
                max_g = (p, cur_len)
            cur_len = 0
    return max_g[0], max_g[1] + max_g[0]

def max_zero_interval(arr):
    return max(((i, j) for i in range(len(arr)) if arr[i:i+2] == [1,0] for j in range(i+1, len(arr)) if arr[j] == 1), key=lambda x: x[1]-x[0], default=(-1,-1))

a = [1, 0, 0, 0, 1]
# chose_sit(find_max_gap(rnd))
# print(a)
print(max_zero_interval(rnd))
print(find_max_gap(rnd))
print(findb(rnd))
