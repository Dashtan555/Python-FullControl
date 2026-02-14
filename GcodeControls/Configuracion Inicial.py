import fullcontrol as fc
 # Aqui se usa la funcion initial_settings para configurar las configuraciones iniciales de la impresion
 # como velocidad de impresion, velocidad de traslado, temperatura del nozzle entre otras.
 

steps = [fc.Point(x=30, y=30, z=0.2), fc.Point(x=60)]
initial_settings = {
    "print_speed": 2000,
    "travel_speed": 4000,
    "nozzle_temp": 280,
    "bed_temp": 80,
    "fan_percent": 40,
}
gcode_controls = fc.GcodeControls(initialization_data=initial_settings)
print(fc.transform(steps, 'gcode', gcode_controls))