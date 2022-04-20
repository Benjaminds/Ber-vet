import roadster as rd
import matplotlib.pyplot as plt

route = 'speed_elsa.npz'
target = 0.5
time = []

for i in range(66):
    time.append(rd.time_to_destination(i, route, 10000))

plt.plot(time)
#plt.axis([25, 32, 0.45, 0.55])
plt.plot([0, 65], [target, target])

dis, n = rd.distance(target, route)
print(dis, n)

plt.scatter(dis, target)
plt.grid()