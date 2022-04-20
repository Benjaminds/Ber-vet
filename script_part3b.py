import roadster as rd
import matplotlib.pyplot as plt

route = 'speed_elsa.npz'
target = 10000
consume = []

for i in range(66):
    consume.append(rd.total_consumption(i, route, 10000))

plt.plot(consume)
#plt.axis([25, 32, 0.33, 0.4])
plt.plot([0, 65], [target, target])

dis = rd.reach(target, route)
print('reach:', dis, 'km')

plt.scatter(dis, target)
plt.grid()