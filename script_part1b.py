import roadster as rd
import matplotlib.pyplot as plt
import numpy as np

#Anna
dis, spe = rd.load_route('speed_anna.npz')
x = np.linspace(min(dis), max(dis), 60)
v = rd.velocity(x,'speed_anna')

#Elsa
dis2, spe2 = rd.load_route('speed_elsa.npz')
x2 = np.linspace(min(dis2), max(dis2), 60)
v2 = rd.velocity(x2,'speed_elsa')

###Plot###
fig = plt.figure(dpi = 300)

#Anna plot
plt.scatter(dis, spe, marker = '.', label = 'Anna - values')
plt.plot(x, v, label = 'Anna - approx')

#Elsa plot
plt.scatter(dis2, spe2, marker = '.', label = 'Elsa - values')
plt.plot(x2, v2, label = 'Elsa - approx')

#Axis and legend
plt.title('Speed over distance')
plt.ylabel('Speed [km/h]')
plt.xlabel('Distance [km]')
# plt.axis([10, 20, 70, 120])
plt.grid()
plt.legend(loc = (0.13, 0.05))
plt.show()