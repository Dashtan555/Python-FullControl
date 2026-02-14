import fullcontrol as fc 

# se usa para purgar y garantizar una correcta impresion desde el inicio.
# 'front_lines_then_x' - this involves printing some lines on the front of the bed before moving in the x direction to the start point of the design
# 'front_lines_then_y' - similar to above except move in y direction
# 'front_lines_then_xy' - similar to above except move in diagonal xy direction
# 'x' - move from the position at the end of start_gcode to the start point of the design along the x direction (after a y-direction move)
# 'y' - similar to above except move in x first, then y to the start point
# 'xy' - print directly from the end of the start gcode to the start point
# 'travel' - travel from the end of the start gcode to the start point


steps = [fc.Point(x=30, y=30, z=0.2), fc.Point(x=60)]
gcode_controls = fc.GcodeControls(initialization_data={"primer": "front_lines_then_xy"})
print(fc.transform(steps, 'gcode', gcode_controls))