import math

n = int(input("Enter the number of points: "))

points = []

for i in range(n):
    x = float(input(f"Enter x coordinate of point {i + 1}: "))
    y = float(input(f"Enter y coordinate of point {i + 1}: "))
    points.append((x, y))

print("\nPoints:", points)

x1 = float(input("\nEnter x1 of first point: "))
y1 = float(input("Enter y1 of first point: "))
x2 = float(input("Enter x2 of second point: "))
y2 = float(input("Enter y2 of second point: "))

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print("Distance between the two points:", distance)

farthest_point = points[0]
max_distance = math.sqrt(
    farthest_point[0] ** 2 + farthest_point[1] ** 2
)

for point in points:
    distance_from_origin = math.sqrt(point[0] ** 2 + point[1] ** 2)

    if distance_from_origin > max_distance:
        max_distance = distance_from_origin
        farthest_point = point

print("Point farthest from origin:", farthest_point)
print("Distance from origin:", max_distance)

        
        