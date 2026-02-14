import fullcontrol as fc

# Ejemplo de diferentes representaciones para de un par de puntos tanto en coordenadas polares, 
# como en coordenadas cartesianas.

origin = fc.Point(x=0, y=0, z=0)
from math import tau

point_cart = fc.Point(x=10,y=0,z=0)
print(point_cart)
point_polar1 = fc.polar_to_point(origin, 10, 0)
print(point_polar1)
point_polar2 = fc.polar_to_point(origin, 10, tau/8)
print(point_polar2)
point_polar3 = fc.polar_to_point(origin, 10, tau/4)
print(point_polar3)
point_polar4 = fc.polar_to_point(origin, 10, -tau/4)
print(point_polar4)