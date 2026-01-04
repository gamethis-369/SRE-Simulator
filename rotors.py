import numpy as np
from database import save_result

def rotor_lifts(m0=0.511, generations=3, rotor_type='lepton', delta_v=0.0):
    masses = [m0]
    params = {'m0': m0, 'generations': generations, 'type': rotor_type, 'delta_v': delta_v}
    for g in range(1, generations + 1):
        k = 2 * g + 2 if rotor_type == 'lepton' else 4 * g
        base = np.sqrt(2 ** k)
        variable = base * (1 + delta_v * np.sin(g * np.pi / 5))
        mass = m0 * variable
        masses.append(mass)
    results = masses
    save_result('rotor_lifts', params, results)
    return masses
