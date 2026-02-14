import fullcontrol as fc

# create an empty list called steps
steps=[]
# add points to the list
steps.append(fc.Point(x=40,y=40,z=0.2))
steps.append(fc.Point(x=50,y=50))
steps.append(fc.Point(x=60,y=40))
# turn the extruder on or off
steps.append(fc.Extruder(on=False))
steps.append(fc.Point(x=40,y=40,z=0.4))
steps.append(fc.Extruder(on=True))
steps.append(fc.Point(x=50,y=50))
steps.append(fc.Point(x=60,y=40))
# transform the design into a plot
fc.transform(steps, 'plot')

filename = 'my_design'
printer = 'ender_3' 
# printer options: generic, ultimaker2plus, prusa_i3, ender_3, cr_10, bambulab_x1, toolchanger_T0, toolchanger_T1, toolchanger_T2, toolchanger_T3
print_settings = {'extrusion_width': 0.5,'extrusion_height': 0.2, 'nozzle_temp': 210, 'bed_temp': 40, 'fan_percent': 100}
# 'extrusion_width' and 'extrusion_height' are the width and height of the printed line)

fc.transform(steps, 'gcode', fc.GcodeControls(printer_name=printer, save_as=filename, initialization_data=print_settings))

steps = [fc.polar_to_point(centre=fc.Point(x=0, y=0, z=i*0.005), radius=10, angle=i*4.321) for i in range(1000)]
fc.transform(steps, 'plot', fc.PlotControls(neat_for_publishing=True, zoom=0.7))

from math import tau
from random import random
steps=[fc.polar_to_point(centre=fc.Point(x=0, y=0, z=i*0.001), radius=10+5*random(), angle=i*tau/13.8) for i in range(4000)]
fc.transform(steps, 'plot', fc.PlotControls(neat_for_publishing=True, zoom=0.7))