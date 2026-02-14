import fullcontrol as fc

result_type = 'plot'  # set as 'gcode' or 'plot'
steps = []
for i in range(6):
    if result_type != 'plot':
        # fan speed does not affect the 'plot' result so doesn't need to be added to the design result_type == 'plot'
        steps.append(fc.Fan(speed_percent=100*i/5))
    steps.append(fc.Point(x=5*(i+1), y=5*((i+1)%2), z=0.2))
print(f"the design specifically for the '{result_type}' result contains {len(steps)} steps:")
for step in steps: print(type(step).__name__)
fc.transform(steps, result_type, fc.PlotControls(color_type='print_sequence'))