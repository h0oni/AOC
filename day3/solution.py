with open('Line2.txt') as Line1:
    li1 = Line1.readlines()

visited = {}
coords = {}

for wire_no, line in enumerate(li1):
    moves = line.split(',')
    x = y = 0
    start = 1

    for mov in moves:
        direct = mov[0]
        distance = int(mov[1:])

        for _ in range(distance):
            if direct == 'U':
                y -= 1
            elif direct == 'L':
                x -= 1
            elif direct == 'R':
                x += 1
            else:
                y += 1

            if (x, y) in visited and wire_no == 1 and (x, y) not in coords:
                coords[(x, y)] = start + visited[(x, y)]

            if wire_no == 0 and (x, y) not in visited:
                visited[x, y] = start
            start += 1
min_dist = min(abs(i) + abs(j) for i, j in coords.keys())
few_steps = min(stp for stp in coords.values())
print("Manhattan distance:", min_dist)
print("fewest combined steps:", few_steps)