import fullcontrol as fc
# create a basic simple geometry (a cylinder) that will be modified retrospectively
centre = fc.Point(x=50, y=50, z=0)
steps = fc.helixZ(centre, start_radius=10, end_radius=10, start_angle=0, n_turns=50, pitch_z=0.167, segments=50*64)
steps.append(fc.PlotAnnotation(point = fc.Point(x=50, y=50, z=10), label='original geometry'))
fc.transform(steps, 'plot', fc.PlotControls(color_type='print_sequence', zoom=0.7))

# 'post-process' the geometry to change it
z_max = 25
for step in steps:
    if isinstance(step, fc.Point):
        step.x -= 0.8*(step.x-centre.x)*(step.z/z_max)
        step.y -= 0.8*(step.y-centre.y)*(step.z/z_max)
        step.z -= (((step.y-centre.y)/2.5)**2)*(step.z/z_max)
steps[-1] = fc.PlotAnnotation(point = fc.Point(x=50, y=50, z=10), label="'postprocessed' geometry")
fc.transform(steps, 'plot', fc.PlotControls(color_type='print_sequence', zoom=0.7))