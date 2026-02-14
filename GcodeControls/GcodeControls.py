import fullcontrol as fc

steps = []
steps.append(fc.Point(x=30, y=30, z=0.2))
steps.append(fc.Point(x=60))
# option 1 (use built-in function):
gcode_controls = fc.GcodeControls(save_as='my_design') # filename includes date+time
fc.transform(steps, 'gcode', gcode_controls)
gcode_controls = fc.GcodeControls(save_as='my_design', include_date = False) # filename doesn't include date+time
fc.transform(steps, 'gcode', gcode_controls)
# option 2 (save gcode string to file manually):
gcode = fc.transform(steps, 'gcode')
open('my_file.gcode', 'w').write(gcode)


steps = []
steps.append(fc.Point(x=30, y=30, z=0.2))
steps.append(fc.Point(x=60))
gcode_controls = fc.GcodeControls(printer_name='toolchanger_T0', save_as='my_design')
fc.transform(steps, 'gcode', gcode_controls)

