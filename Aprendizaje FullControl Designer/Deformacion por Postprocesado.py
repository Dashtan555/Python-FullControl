import fullcontrol as fc
from math import tau

rad, rad_fluc, segs_per_period = 20, 5, 12
periods = 25
period_length = 3  # calculated to make sure the wave is the length of the circle circumference
steps = fc.sinewaveXYpolar(fc.Point(x=rad, y=0, z=0.2), 0.75*tau, rad_fluc, period_length, periods, segs_per_period)
steps.append(fc.PlotAnnotation(point=fc.Point(x=1.5*rad, y=-60, z=10), label='original geometry'))
fc.transform(steps, 'plot', fc.PlotControls(color_type='print_sequence'))

def linear_to_arc(steps: list, centre: fc.Point, radius: float) -> list:
    '''this function assumes the linear geometry (list of points: 'steps') is oriented in 
    the y direction and positioned in the positive x-direction from the centre point. it 
    is 'wrapped' around an arc/circle dictated by radius. it is possible to wrap multiple 
    times. return list of translated points
    '''
    steps_wrapped = []
    for step in steps:
        rad_step = step.x - centre.x
        angle_step = (step.y - centre.y) / radius
        steps_wrapped.append(fc.polar_to_point(centre, rad_step, angle_step))
    return steps_wrapped

del steps[-1] # remove the PlotAnnotation
steps_wrapped = linear_to_arc(steps, fc.Point(x=0, y=0, z=0.2), 15)
steps_wrapped.append(fc.PlotAnnotation(point=fc.Point(x=0, y=0, z=10), label="'post-processed' geometry"))

fc.transform(steps_wrapped, 'plot', fc.PlotControls(color_type='print_sequence'))