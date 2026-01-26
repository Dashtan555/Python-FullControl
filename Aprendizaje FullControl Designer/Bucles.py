import fullcontrol as fc

# definimos una variable como numero de capas
layers = 30

# usamos la variable layer_steps para crear en el un cuadrado a traves de la funcion fc.rectangleXY
# como parametros colocamos el punto inicial (0,0) y el tamno x=10 y y=10
layer_steps=fc.rectangleXY(start_point=fc.Point(x=0, y=0, z=0.2), x_size=10, y_size=10)
# Con la funcion fc.move copiamos el lapyer_steps las veces que indique el numero de capas layers = 30
# tomar en cuenta que fc.Vector se usa para moverse en este caso en el eje z=0.2 es un movimiento relativo
# desde donde esta sube 0.2 a diferencia que con fc.Point son movimiento absolutos
steps=fc.move(layer_steps, fc.Vector(z=0.2), copy=True, copy_quantity=layers)
# El siguiente codigo lo que hace es que en el plot del grafico identificar el caso #1 con letras
steps.insert(-2, fc.PlotAnnotation(label='Case 1'))

# Usamos la funcion travel_to para dirigirnos al punto de inicio del caso #2
steps.extend(fc.travel_to(fc.Point(x=20, y=20, z=0.2)))
# En este caso a traves del bucle for se logra hacer los mismo que en el caso anterior
# valiendonos de la variable i que va aumentando segun vaya pasando por el bucle hasta 
# llegar a layers que es el numero de capas
for i in range(layers):
    steps.extend(fc.rectangleXY(start_point=fc.Point(x=20,y=20,z=i*0.2), x_size=10, y_size=10))
steps.insert(-2, fc.PlotAnnotation(label='case 2'))

steps.extend(fc.travel_to(fc.Point(x=40,y=40,z=0.2)))

for i in range(layers):
    steps.extend(fc.rectangleXY(start_point=fc.Point(x=40,y=40,z=i*0.2), x_size=10+i*0.2, y_size=10))
steps.insert(-2, fc.PlotAnnotation(label='case 3'))

fc.transform(steps, 'plot')