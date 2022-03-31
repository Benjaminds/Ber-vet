import numpy as np
import roadster  as rd
import matplotlib.pyplot as plt

speed_kmph = np.linspace(1., 200., 1000)
consumption_Whpkm = rd.consumption(speed_kmph)

fig = plt.figure(dpi = 300)
plt.plot(speed_kmph, consumption_Whpkm)
plt.title('Consumption over speed')
plt.xlabel('Speed [km/h]')
plt.ylabel('Consumption [Wh/km]')
plt.grid()
plt.show()
