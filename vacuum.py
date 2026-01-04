from database import save_result

def vacuum_twist(t_factor=0.0001, terms=5):
    suppression = 1 - np.exp(-1 / t_factor)  # Simplified
    params = {'t_factor': t_factor, 'terms': terms}
    results = suppression
    save_result('vacuum_twist', params, results)
    return suppression
