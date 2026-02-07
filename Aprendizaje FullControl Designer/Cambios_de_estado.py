import fullcontrol as fc


# Es este ejemplo lo que se busca es hacer cambios de estado por ejemplo
# encender o apagar el extrusor.

steps = [fc.Point(x=i, y=i, z=0.2) for i in range(10)]
steps.insert(4, fc.Extruder(on=False))
steps.insert(8, fc.Extruder(on=True))
fc.transform(steps,'plot')

