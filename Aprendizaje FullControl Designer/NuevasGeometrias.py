import fullcontrol as fc

# Se puede crear nuevas funciones como este ejemplo, no estoy seguro como funciona voy a continuar 
# para aprender el resto de funciones

def saw_wave_x(start_point: fc.Point, length: float, amplitude: float, periods: int) -> list:
    period_length = length/periods
    steps_wave = []
    for i in range(periods):
        steps_wave.append(fc.Point(x=start_point.x+period_length*i, y=start_point.y, z=start_point.z))
        steps_wave.append(fc.Point(x=start_point.x+period_length*i, y=start_point.y+amplitude, z=start_point.z))
    steps_wave.append(fc.Point(x=start_point.x+length, y=start_point.y, z=start_point.z))   
    return steps_wave
                 
steps = []
steps.extend(saw_wave_x(fc.Point(x=20, y=20, z=0), 50, 10, 20))
steps.extend(saw_wave_x(steps[-1], 50, 20, 10))
steps.extend(saw_wave_x(steps[-1], 50, 10, 20))
fc.transform(steps, 'plot', fc.PlotControls(color_type='print_sequence', style='tube'))