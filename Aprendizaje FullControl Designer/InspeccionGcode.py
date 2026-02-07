import fullcontrol as fc

# En este ejemplo se demuestra como se puede realizar una inspeccion del codigo G
# para evaluar posibles errores o alguna duda respecto a la trayectoria o 
# cambio que se pueda programar.

output_type = 1 # change this to be 1, 2, or 3

steps = [fc.Point(x=0,y=i,z=0) for i in range(11)]
gcode = fc.transform(steps, 'gcode')
gcode_list = (gcode.split('\n'))
if output_type == 1:
    print(gcode)
elif output_type == 2:
    print('\n'.join(gcode_list[5:8]))
elif output_type == 3:
    for gcode_line in (gcode_list):
        if 'G1 F' in gcode_line or 'G0 F' in gcode_line:
            print(gcode_line)