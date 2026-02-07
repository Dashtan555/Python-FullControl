import fullcontrol as fc
from math import tau

# Tau representa 2*pi el cual representa el circulo completo, en este ejemplo
# se puede observar que 0.75*tau es 3/4 partes del circulo y 0.5*tau es el medio circulo

centre = fc.Point(x=0, y=0, z=0.2)
steps = fc.arcXY(centre, 10, 0, 0.75*tau)
fc.transform(steps, 'plot', fc.PlotControls(color_type='print_sequence'))