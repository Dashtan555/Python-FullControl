import fullcontrol as fc
# Primero Creo una lista vacia llamada steps[]
steps = []
# Es este primer paso con la funcion append añado elementos a mi lista vacia steps
# y hago que la boquilla se dirija al primer punto x=0, y=0, y con un z=0.2
steps.append(fc.Point(x=0, y=0, z=0.2))
# Luego con la misma función append agrego el punto x=5, y=5 y en este caso ya voy extruyendo material 
steps.append(fc.Point(x=5, y=5))
# Con esta linea de codigo y la función (extend) agrego una serie de parametros como apagar el extrusor con fc.Extruder(on=False)
# Me muevo al punto x=10, y=10 y al final vuelvo a activar la extrusión de materia con fc.Extruder(on=True)
steps.extend([fc.Extruder(on=False), fc.Point(x=10, y=10), fc.Extruder(on=True)])
# Desde aqui me muevo al siguiente punto extruyendo material 
steps.append(fc.Point(x=15, y=15))
# Con la función travel_to me dirijo al punto fc.Point(x=20 y=20),
# pero en esta función ya se apaga el extrusor automaticamente 
# y al llegar al punto vuelve a encender el extrusor nuevamente
steps.extend(fc.travel_to(fc.Point(x=20, y=20)))
# tomas en cuenta que cuando se desplaza de un punto a otro y no se a expresado la función travel_to 
# el programa considera que es un desplazamiento de diseño por ende debe extruir el material
# y esto la hace automaticamente, FullControl calcula el volumen del filamento necesario
# basandose en la distancia euclidiana entre los puntos 
# a traves de la formula interna distancia=sqrt((x2-x1)^2+*(y2-y1)^2)
steps.append(fc.Point(x=25, y=25))
#Pra finalizar este programa sencillo, se envia a la función fc.transform(steps, 'plot') para visualizar la trayectoria
fc.transform(steps, 'plot')