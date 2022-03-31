import roadster as rd


def get_steps(route):
    x = rd.load_route(route)[0][-1]
    
    n = 2
    t_old = rd.time_to_destination(x, route, n)
    E_t = 1
    
    while 60 * abs(E_t) > 0.5:
        n *= 2
        t_new = rd.time_to_destination(x, route, n)
        
        #Tredjedelsregeln
        E_t = (t_new - t_old) / 3
        t_old = t_new
    
    #Richardsonextrapolation
    t = t_new + E_t
    return t, n


#Elsa
T_e, N_e = get_steps('speed_elsa.npz')
print(f'\nElsa:\nTime: {T_e} h\nNumber of steps: {N_e}')

#Anna
T_a, N_a = get_steps('speed_anna.npz')
print(f'\nAnna:\nTime: {T_a} h\nNumber of steps: {N_a}')