import fullcontrol as fc

# En este ejmplo se puede ver secuaenciacion para subir el porcentaje de operacion del ventilador
# se hacen anotaciones dinamicas a traves del bucle el cual 
# denota el porcentaje que va aumentando conforme avanza en el bucle y tanto las anotaciones como
# el rendimiento del ventilador

steps = []
for i in range(13):
    steps.append(fc.Point(x=i+1, y=i+1, z=0))
    if i%2 == 0 and i<12:
        steps.append(fc.Fan(speed_percent=i*10))
        steps.append(fc.PlotAnnotation(label=f'fan speed {i*10}%'))
fc.transform(steps, 'plot', fc.PlotControls(style='line', color_type='print_sequence'))