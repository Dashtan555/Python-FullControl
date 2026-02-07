import fullcontrol as fc

from math import cos, tau
x_size = 20
y_offset, y_amplitude, waves = 5, 5, 10
t_steps = fc.linspace(0, 1, 101) # [0, 0.01, 0.02, ... , 0.99, 1]
steps = []
for t_now in t_steps:
    x_now = x_size*t_now
    y_now = y_offset+y_amplitude*cos(t_now*tau*waves)
    z_now = 0.2
    steps.append(fc.Point(x=x_now, y=y_now, z=z_now))
    #print(x_now, y_now)
    #steps = fc.move(steps,fc.Vector(z=0.1),copy=True, copy_quantity=10)
fc.transform(steps, 'plot', fc.PlotControls(color_type='print_sequence'))