import fullcontrol as fc
# Primero Creo una lista vacia llamada steps[]
steps = []
# Es ets primer paso con la funcion append añado elementos a mi lista vacia steps
# y hago que la boquilla se dirija al primer punto x=0, y=0, y con un z=0.2
steps.append(fc.Point(x=0, y=0, z=0.2))
# Luego con la misma función append agrego el punto x=5, y=5 y en este caso ya voy extruyendo material 
steps.append(fc.Point(x=5, y=5))
steps.extend([fc.Extruder(on=False), fc.Point(x=10, y=10), fc.Extruder(on=True)])
steps.append(fc.Point(x=15, y=15))
steps.extend(fc.travel_to(fc.Point(x=20, y=20)))
steps.append(fc.Point(x=25, y=25))
fc.transform(steps, 'plot')