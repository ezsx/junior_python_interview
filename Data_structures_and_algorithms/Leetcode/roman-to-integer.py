values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
values_2 = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}

sum = 0
s = "MCMXCIV"
print(s[-1:], s[-2:])
while s != "":
    leks_1 = s[-1:]
    leks_2 = s[-2:]
    print(leks_1, leks_2)
    if leks_2 in values_2:
        sum += values_2[leks_2]
        s = s[:-2]
    elif leks_1 in values:
        sum += values[leks_1]
        s = s[:-1]
print(sum)
