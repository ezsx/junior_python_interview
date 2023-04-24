def main():
    # Считываем данные
    n = int(input())
    c = list(map(int, input().split()))
    r = list(map(int, input().split()))
    k = int(input())
    s = list(map(int, input().split()))

    # генерируем словарь, где ххраним номер строки для каждого идентификатора
    row_dict = {c[i]: r[i] for i in range(n)}

    # Инициализирум переменную для подсчета многострочных переходов.
    multi_row_transitions = 0

    # Перебираем абстрактные символы
    # и для каждой пары соседних символов проверяем,
    # находятся ли они в разных строках, используя словарь.
    # Если это так, увеличиваем счетчик многострочных переходов.
    for i in range(1, k):
        if row_dict[s[i]] != row_dict[s[i - 1]]:
            multi_row_transitions += 1

    print(multi_row_transitions)

if __name__ == "__main__":
    main()
