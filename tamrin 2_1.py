n = int(input())
def pascals_triangle(n):
    triangle = []
    for i in range(n):
        row = []
        if i > 1:
            for j in range(i+1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(triangle[i-1][j-1] + triangle[i-1][j])
        else:
            row = [1] * (i+1)
        triangle.append(row)
    return triangle

for row in pascals_triangle(n):
    print(" ".join(str(num) for num in row))