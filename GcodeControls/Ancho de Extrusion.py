import fullcontrol as fc

steps = [fc.Point(x=30, y=30, z=0.2), fc.Point(x=60)]
initial_settings = {
    "extrusion_width": 0.8,
    "extrusion_height": 0.3,
    "e_units": "mm3",
    "relative_e": False,
    "dia_feed": 2.85,
}
gcode_controls = fc.GcodeControls(initialization_data=initial_settings)
print(fc.transform(steps, 'gcode', gcode_controls))