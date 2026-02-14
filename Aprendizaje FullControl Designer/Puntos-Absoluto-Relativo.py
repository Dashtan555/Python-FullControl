import lab.fullcontrol as fclab

# Ejemplo en el cual se muestra los puntos absolutos y relativos
# se usa la funcion fclab.setup_p() para puntos absolutos
# y fclab.setup_r() para puntos relativos
# los puntos relativos siempre son definidos respecto al ultimo punto de esta lista

steps = []
P = fclab.setup_p()
R = fclab.setup_r(steps)

steps.append(P(40, 40, 0))
steps.append(R(0, 1, 0))
steps.append(R(1, 0, 0))
steps.append(R(-7, -12, 0))

for step in steps: print(step)