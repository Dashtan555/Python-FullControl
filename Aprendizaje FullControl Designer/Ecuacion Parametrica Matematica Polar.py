import fullcontrol as fc
from math import cos, tau

centre = fc.Point(x=0, y=0, z=0)
inner_rad, rad_fluctuation, waves = 4, 1, 12
t_steps = fc.linspace(0, 1, 1001)  # [0, 0.001, 0.002, ... , 0.999, 1]
steps = []
for t_now in t_steps:
    a_now = t_now*tau
    r_now = inner_rad+rad_fluctuation*cos(t_now*tau*waves)
    z_now = 0
    steps.append(fc.polar_to_point(centre, r_now, a_now))
steps = fc.move(steps,fc.Vector(z=0.1),copy=True, copy_quantity=10)
fc.transform(steps, 'plot')