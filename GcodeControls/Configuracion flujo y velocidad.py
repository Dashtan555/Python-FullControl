import fullcontrol as fc

steps = [fc.Point(x=30, y=30, z=0.2), fc.Point(x=60)]
initial_settings = {
    "print_speed_percent": 100,
    "material_flow_percent": 100,
}
gcode_controls = fc.GcodeControls(initialization_data=initial_settings)
print(fc.transform(steps, 'gcode', gcode_controls))