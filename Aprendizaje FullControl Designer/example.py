import fullcontrol as fc

steps = [fc.Point(x=i, y=i, z=0.2) for i in range(10)]
steps.insert(3, fc.Extruder(on=False))
steps.insert(6, fc.Extruder(on=True))
fc.transform(steps,'plot')
