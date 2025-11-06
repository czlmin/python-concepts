def average_coordinates(points):
    avg_x = 0
    avg_y = 0
    avg_z = 0
    for x, y, z in points:
        avg_x += x
        avg_y += y
        avg_z += z

    return float(avg_x)/len(points), float(avg_y)/len(points), float(avg_z)/len(points)

points = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(average_coordinates(points))


