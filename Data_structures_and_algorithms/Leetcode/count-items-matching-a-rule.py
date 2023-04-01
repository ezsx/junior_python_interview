def math_rule(item, ruleKey, ruleValue):
    if ruleKey == "type":
        return ruleValue == item[0]
    if ruleKey == "color":
        return ruleValue == item[1]
    if ruleKey == "name":
        return ruleValue == item[2]
    return False

#
# items = [["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]]
# count = 0
# for i in items:
#     if math_rule(i, ruleKey, ruleValue):
#         count += 1
# print(count)
