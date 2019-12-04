upper_range = 657474
lower_range = 183564


def check_increase(num):
    string = str(num)
    # print(string[0])
    for i, c in enumerate(string):
        # print(c)
        try:
            if int(c) > int(string[i + 1]):
                return 0
            else:
                continue
        except IndexError:
            return 1
    return 1


def check_same(num, k):
    string = str(num)
    for i, c in enumerate(string):
        # print(string.count('5'))
        try:
            if int(c) == int(string[i + 1]):
                # print(string.count(c)>2 & k)
                if (string.count(c) > 2) & (int(k)):
                    # print(222)
                    continue
                return 1
            else:
                continue
        except IndexError:
            return 0
    return 0


count1 = 0
count2 = 0

for i in range(lower_range, upper_range):
    if check_increase(i) & check_same(i, 0):
        count1 += 1
    if check_increase(i) & check_same(i, 1):
        count2 += 1

# check_same(5555,0)

print(f'Ans(part-1): {count1}')
print(f'Ans(part-2): {count2}')