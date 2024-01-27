n = int(input())
maze = [['.' for _ in range(n)]]
maze[0][0] = '*'
x, y = 0, 0

while True:
    command = input()
    if command == 'END':
        break
    elif command == 'R':
        if y+1 <= (n-1):
            y += 1
            maze[x][y] = '*'
    elif command == 'L':
        if y-1 >= 0:
            y -= 1
            maze[x][y] = '*'
    elif command == 'B':
        maze.append(['.' for _ in range(n)])
        x += 1
        maze[x][y] = '*'

for row in maze:
    print(' '.join(row))

if y != (n-1):
    print("There's no way out!")
