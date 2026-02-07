import fullcontrol as fc

# Se puede unir bloques para formar geometrias complejas 
# usando el ensablaje de bloques de diseno 
# como el ejemplo acontinuacion

centre = fc.Point(x=0, y=0, z=0.2)
block1 = fc.spiralXY(centre, 0.5, 20, 0, 40, 2000)
block2 = fc.helixZ(centre, 20, 0, 0, 60, 0.3, 2200)
steps = block1 + block2
fc.transform(steps, 'plot', fc.PlotControls(color_type='print_sequence'))