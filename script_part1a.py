#!/usr/bin/env python3
#Wed Mar 16 15:04:11 2022 +0100, 601cd27
import numpy as np
import roadster  as rd
import matplotlib.pyplot as plt
import test_roadster as tst

speed_kmph = np.linspace(1., 200., 1000)
consumption_Whpkm = rd.consumption(speed_kmph)

fig = plt.figure(dpi = 300)
plt.plot(speed_kmph, consumption_Whpkm)
plt.title('Consumption over speed')
plt.xlabel('Speed [km/h]')
plt.ylabel('Consumption [Wh/km]')
plt.grid()
plt.show()

print(tst.test_part1a_A())
print(tst.test_part1a_B())
print(tst.test_part1a_C())