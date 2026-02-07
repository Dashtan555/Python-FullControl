import fullcontrol as fc

print('e.g. "fc.linspace(0,1,5)": ' + str(fc.linspace(0,1,5)))

from math import tau
centre = fc.Point(x=0, y=0, z=0)
point_count = 600
radii = fc.linspace(10,20,point_count)
angles = fc.linspace(0,tau*7,point_count)
steps = [fc.polar_to_point(centre, radii[i], angles[i]) for i in range(point_count)]
fc.transform(steps, 'plot', fc.PlotControls(color_type='print_sequence'))