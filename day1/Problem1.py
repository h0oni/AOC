from math import floor

with open('input.txt') as my_input:
    li = my_input.readlines()

ans = 0

for i in li:
    num = int(i)
    # print(ans)
    ans = ans + (floor(num / 3) - 2)
print('ans:', end=' ')
print(ans)
