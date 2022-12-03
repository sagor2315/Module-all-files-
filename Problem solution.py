# Given the 3 sides of a triangle - x, y and z - determine whether the
# triangle is equilateral, isosceles or obtuse.

x = int(input("The First Side is: "))
y = int(input("The Second Side is: "))
z = int(input("The Third Side is: "))
if x == y == z:
    print("The Triangle is Equilateral")
elif x == y != z:
    print("The Triangle is Isosceles")
else:
    print("The Triangle is Obtuse")