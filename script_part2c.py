import roadster as rd
import matplotlib.pyplot as plt
import numpy as np


def get_error(route, m):
    x = rd.load_route(route)[0][-1]
    
    t_old = rd.time_to_destination(x, route, 1)
    E_t = []
    n = []
    
    for i in range(m):
        t_new = rd.time_to_destination(x, route, 2 ** (i + 1))
        n.append((2 ** (i + 1)))
        
        #Tredjedelsregeln
        E_t.append(abs((t_new - t_old) / 3))
        t_old = t_new
    
    return E_t, n


#Elsa
E_e, n = get_error('speed_elsa.npz', 10)

#Anna
E_a = get_error('speed_anna.npz', 10)[0]

y = [(E_e[0] + E_a[0]) / 2 ** (i + 1) for i in range(len(n))]


plt.loglog(n, E_e, label = 'Elsa')
plt.loglog(n, E_a, label = 'Anna')
plt.loglog(n, y, label = 'Teoretiskt värde')
plt.title('Fel över antalet staplar')
plt.ylabel('Fel')
plt.xlabel('Antalet staplar')
plt.legend()
plt.grid()
plt.show()