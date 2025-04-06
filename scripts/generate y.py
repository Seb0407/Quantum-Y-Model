import numpy as np
import matplotlib.pyplot as plt

def draw_y_particle():
    # Dessine un Y en 2D (simplifié)
    x = [0, 0, -1, 0, 1]
    y = [0, 2, 1, 1, 1]
    plt.plot(x, y, 'b-', linewidth=2)
    plt.title("Quasi-Particule en Y")
    plt.savefig("y_particle.png")

draw_y_particle()
