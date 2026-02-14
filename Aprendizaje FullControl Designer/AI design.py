import fullcontrol as fc
from math import cos, sin, pi

def generate_spiral_points(start_radius: float, end_radius: float, turns: int, num_points: int, center: fc.Point) -> list:
    points = []
    radius_diff = end_radius - start_radius
    angle_step = 2 * pi * turns / num_points
    for i in range(num_points):
        radius = start_radius + radius_diff * i / (num_points - 1)
        angle = i * angle_step
        x = center.x + radius * cos(angle)
        y = center.y + radius * sin(angle)
        points.append(fc.Point(x=x, y=y, z=center.z)) # added 'fc.' and a z value is required for FullControl to create a plot in 3D space
    return points

steps = generate_spiral_points(10, 20, 4, 128, fc.Point(x=50, y=50, z=0))
fc.transform(steps, 'plot', fc.PlotControls(color_type='print_sequence'))