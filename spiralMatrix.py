matrix = [[1,2,3],[4,5,6],[7,8,9]]

def spiralOrder(matrix):
    m = len(matrix[0])
    n = len(matrix)

    max_x = m
    min_x = 0

    max_y = n
    min_y = 0

    total = m * n

    x = 0
    y = 0

    count = 0
    output = []

    while count < total:

        while min_x <= x < max_x and min_y <= y <max_y:
            output.append(matrix[y][x])
            x += 1
            count += 1
        min_y += 1
        y += 1
        x -= 1

        while min_x <= x < max_x and min_y <= y <max_y:
            output.append(matrix[y][x])
            y += 1
            count += 1
        max_x -= 1
        y -= 1
        x -= 1

        while min_x <= x < max_x and min_y <= y <max_y:
            output.append(matrix[y][x])
            x -= 1
            count += 1
        max_y -= 1
        y -= 1
        x += 1

        while min_x <= x < max_x and min_y <= y <max_y:
            output.append(matrix[y][x])
            y -= 1
            count += 1
        min_x += 1
        y += 1
        x += 1
        
    return output

print(spiralOrder(matrix))