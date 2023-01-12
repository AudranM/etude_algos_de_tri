import matplotlib.pyplot as plt

def print_time (tab : [int]) -> None:
    plt.title("Rapport de Vitesse")
    plt.plot(tab)
    plt.xlabel('Nombre')
    plt.ylabel('Temps')
    plt.show()