import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from scipy.linalg import eigh

class SRESimulator:
    def __init__(self, num_nodes=26):
        self.num_nodes = num_nodes
        self.nodes = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')[:num_nodes]
        self.frequencies = np.linspace(0.040, 0.780, num_nodes)

    def display_lattice_nodes(self):
        print("Node | Frequency (Hz)")
        for node, freq in zip(self.nodes, self.frequencies):
            print(f"{node}    | {freq:.4f}")

    def plot_frequencies(self):
        plt.figure(figsize=(10, 6))
        plt.bar(self.nodes, self.frequencies, color='#3498db')
        plt.title('SRE Lattice Node Resonant Frequencies')
        plt.xlabel('Node')
        plt.ylabel('Frequency (Hz)')
        plt.show()

    def rotor_lifts(self, m0=0.511, generations=3, rotor_type='lepton', delta_v=0.0):
        masses = [m0]
        for g in range(1, generations + 1):
            k = 2 * g + 2 if rotor_type == 'lepton' else 4 * g
            base = np.sqrt(2 ** k)
            variable = base * (1 + delta_v * np.sin(g * np.pi / 5))
            mass = m0 * variable
            masses.append(mass)
        print("Generation | Mass (MeV)")
        for g, mass in enumerate(masses):
            print(f"{g}          | {mass:.3f}")
        return masses

    def hamiltonian_spectrum(self, coupling=0.05):
        omega_sq = self.frequencies ** 2 / 2
        H = np.diag(omega_sq)
        for i in range(self.num_nodes):
            for j in range(self.num_nodes):
                if i != j and (abs(i - j) <= 2 or abs(i - j) == self.num_nodes - 1):
                    H[i, j] = coupling
                    H[j, i] = coupling
        eigenvalues = eigh(H, eigvals_only=True)
        print("Eigenvalues (sorted, first 10):")
        print(eigenvalues[:10])
        plt.figure(figsize=(10, 6))
        plt.scatter(range(1, len(eigenvalues) + 1), eigenvalues, color='#e74c3c')
        plt.title('SRE Hamiltonian Eigenvalue Spectrum')
        plt.xlabel('Mode Index')
        plt.ylabel('Energy')
        plt.show()
        return eigenvalues

    def vacuum_twist_suppression(self, t_factor=0.0001):
        suppression = 1 - np.exp(-1 / t_factor)
        print(f"Suppression Factor: {suppression:.10f}")
        print("Effective Λ ~ 10^{-120} (normalized)")

    def fibonacci_convergence(self, terms=50):
        fib = [0, 1]
        for i in range(2, terms + 1):
            fib.append(fib[i-1] + fib[i-2])
        ratios = [fib[i+1] / fib[i] for i in range(1, terms)]
        plt.figure(figsize=(10, 6))
        plt.plot(range(2, terms + 1), ratios, label='F_{n+1}/F_n', color='#2ecc71')
        plt.axhline((1 + np.sqrt(5))/2, color='#f39c12', linestyle='--', label='φ ≈ 1.618')
        plt.title('Fibonacci Ratio Convergence to Golden Ratio')
        plt.xlabel('n')
        plt.ylabel('Ratio')
        plt.legend()
        plt.show()

# Example Usage
if __name__ == "__main__":
    sre = SRESimulator(num_nodes=26)
    print("=== SRE Lattice Nodes ===")
    sre.display_lattice_nodes()
    sre.plot_frequencies()

    print("\n=== Rotor Lifts ===")
    sre.rotor_lifts(m0=0.511, generations=3, rotor_type='lepton', delta_v=0.0)

    print("\n=== Hamiltonian Spectrum ===")
    sre.hamiltonian_spectrum(coupling=0.05)

    print("\n=== Vacuum Twist ===")
    sre.vacuum_twist_suppression(t_factor=0.0001)

    print("\n=== Fibonacci Convergence ===")
    sre.fibonacci_convergence(terms=50)
