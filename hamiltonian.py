import numpy as np
from scipy.linalg import eigh
from database import save_result

def hamiltonian_spectrum(num_nodes=26, coupling=0.05):
    omega = np.linspace(0.04, 0.78, num_nodes)
    H_diag = omega**2 / 2
    H = np.diag(H_diag)
    for i in range(num_nodes):
        for j in range(num_nodes):
            if i != j and (abs(i - j) <= 2 or abs(i - j) == num_nodes - 1):
                H[i, j] = coupling
                H[j, i] = coupling
    eigenvalues = eigh(H, eigvals_only=True)
    params = {'nodes': num_nodes, 'coupling': coupling}
    save_result('hamiltonian', params, eigenvalues.tolist())
    return eigenvalues
