from math import floor

with open('input.txt') as my_input:
    li = my_input.readlines()

ans = 0

for i in li:
    num = int(i)
    while num > 5:
        new_mass = (floor(num / 3) - 2)
        ans = ans + new_mass
        num = new_mass

print('ans:', end=' ')
print(ans)