from geometry_lib import Circle, Triangle, area

print("Circle r=5 area:", area(Circle(5)))
print("Triangle 3-4-5 area:", area(Triangle(3, 4, 5)))
print("Is 3-4-5 right-angled?", Triangle(3, 4, 5).is_right())