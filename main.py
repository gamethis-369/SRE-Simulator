from lattice import Lattice
from rotors import rotor_lifts
from hamiltonian import hamiltonian_spectrum
from vacuum import vacuum_twist
from fibonacci import fibonacci_convergence
from database import query_results
from utils import plot_data

def main_menu():
    lattice = Lattice()
    while True:
        print("\nSRE Simulator Menu")
        print("1. Display Lattice Nodes")
        print("2. Compute Rotor Lifts")
        print("3. Compute Hamiltonian Spectrum")
        print("4. Compute Vacuum Twist")
        print("5. Fibonacci Convergence")
        print("6. Query Database")
        print("7. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            lattice.display()
        elif choice == '2':
            m0 = float(input("Base mass m0 (MeV): ") or 0.511)
            gens = int(input("Generations: ") or 3)
            rotor_lifts(m0, gens)
        elif choice == '3':
            nodes = int(input("Nodes: ") or 26)
            coupling = float(input("Coupling: ") or 0.05)
            spectrum = hamiltonian_spectrum(nodes, coupling)
            plot_data(range(len(spectrum)), spectrum, 'Spectrum', 'Index', 'Energy')
        elif choice == '4':
            t_factor = float(input("T factor: ") or 0.0001)
            vacuum_twist(t_factor)
        elif choice == '5':
            terms = int(input("Terms: ") or 50)
            ratios = fibonacci_convergence(terms)
            plot_data(range(2, terms+1), ratios, 'Fib Convergence', 'n', 'Ratio')
        elif choice == '6':
            results = query_results()
            for row in results:
                print(row)
        elif choice == '7':
            break

if __name__ == "__main__":
    main_menu()
