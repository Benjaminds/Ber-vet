import route_nyc as nyc
import matplotlib.pyplot as plt

h = 0.01
time1, distance1, speed1 = nyc.nyc_route_traveler_euler(4, h)
time1 -= 4
time2, distance2, speed2 = nyc.nyc_route_traveler_euler(9.5, h)
time2 -= 9.5

plt.plot(time1, distance1)
plt.plot(time1, speed1)
plt.plot(time2, distance2)
plt.plot(time2, speed2)
plt.grid()