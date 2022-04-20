#Wed Mar 16 15:04:11 2022 +0100, 601cd27
import numpy as np
from scipy import interpolate

def load_route(route):
    """ 
    Get speed data from route .npz-file. Example usage:

      distance_km, speed_kmph = load_route('speed_anna.npz')
    
    The route file should contain two arrays, distance_km and 
    speed_kmph, of equal length with position (in km) and speed 
    (in km/h) along route. Those two arrays are returned by this 
    convenience function.
    """
    # Read data from npz file
    if not route.endswith('.npz'):
        route = f'{route}.npz' 
    data = np.load(route)
    distance_km = data['distance_km']
    speed_kmph = data['speed_kmph']    
    return distance_km, speed_kmph

def save_route(route, distance_km, speed_kmph):
    """ 
    Write speed data to route file. Example usage:

      save_route('speed_olof.npz', distance_km, speed_kmph)
    
    Parameters have same meaning as for load_route
    """ 
    np.savez(route, distance_km=distance_km, speed_kmph=speed_kmph)

### PART 1A ###
def consumption(v):
    """
    Gets consumption[Wh/km] as a function of speed[km/h].

    Parameters
    ----------
    v : Float or ndarray
        The speed of v at a point or series of points.

    Returns
    -------
    c : Float or ndarray
       c(v) = a1 / v + a2 + a3 * v + a4 * v ** 2

    """
    a1 = 546.8
    a2 = 50.31
    a3 = 0.2584
    a4 = 0.008210
    return a1 / v + a2 + a3 * v + a4 * v ** 2

### PART 1B ###
def velocity(x, route):
    # ALREADY IMPLEMENTED!
    """
    Interpolates data in given route file, and evaluates the function
    in x
    """
    # Load data
    distance_km, speed_kmph = load_route(route)
    # Check input ok?
    assert np.all(x>=0), 'x must be non-negative'
    assert np.all(x<=distance_km[-1]), 'x must be smaller than route length'
    # Interpolate
    v = interpolate.pchip_interpolate(distance_km, speed_kmph,x)
    return v

### PART 2A ###
def time_to_destination(x, route, n):
    """
    Gets time[h] to destination as a function of distance[km].

    Parameters
    ----------
    x : Float or integer
        Distance to destination in kilometers.
    route : String
        The route taken.
    n : Integer
        Number of steps used when integrating.

    Returns
    -------
    T : Float
        The approximated time to destination.

    """
    assert type(n) == int, 'n should be an integer'
    
    x_line = np.linspace(0, x, n + 1)
    time = 1 / velocity(x_line, route)
    h = x / n
    return h * (time.sum() - (time[0] + time[-1]) / 2)

### PART 2B ###
def total_consumption(x, route, n):
    """
    Gets consumption[Wh/km] as a function of distance[km].

    Parameters
    ----------
    x : Float or integer
        Distance to destination in kilometers.
    route : String
        The route taken.
    n : Integer
        Number of steps used when integrating.

    Returns
    -------
    T : Float
        The approximated time to destination.

    """
    x_line = np.linspace(0, x, n + 1)
    con = consumption(velocity(x_line, route))
    h = x / n
    return h * (con.sum() - (con[0] + con[-1]) / 2)

### PART 3A ###
def distance(T, route):
    """
    Gets the distance[km] traveled in T hours.

    Parameters
    ----------
    T : Float or integer
        Target time.
    route : String
        The route taken.

    Returns
    -------
    dis : Float
        Distance traveled[km].

    """
    tol = 0.0001
    dis = 30
    error = tol + 1
    n = 0
    
    while error >= tol:
        assert 100 > n, 'Runtime error'
        n += 1
        
        time_2h = time_to_destination(dis, route, 250000)
        time_h = time_to_destination(dis, route, 500000) 
        dt = (time_h - time_2h) / 3
        
        ddis = - (time_h - T) * velocity(dis, route)
        dis += ddis
        error = abs(ddis) + abs(dt)
    
    return dis

### PART 3B ###
def reach(C, route):
    """
    Gets the distance[km] traveled with a start charge of C[Wh].

    Parameters
    ----------
    C : Float or integer
        Start charge.
    route : String
        The route taken.

    Returns
    -------
    dis : Float
        Distance traveled.

    """
    max_dis = load_route(route)[0][-1]
    tol = 0.0001
    dis = 30
    error = tol + 1
    n = 0
    
    while error >= tol:
        assert 100 > n, 'Runtime error'
        n += 1
        
        totcon_2h = total_consumption(dis, route, 250000)
        totcon_h = total_consumption(dis, route, 500000) 
        dtotcon = (totcon_h - totcon_2h) / 3
         
        ddis = - (totcon_h - C) / consumption(velocity(dis, route))
        dis += ddis
        error = abs(ddis) + abs(dtotcon)
        
        if dis > max_dis:
            dis = max_dis
            break
    
    return dis
