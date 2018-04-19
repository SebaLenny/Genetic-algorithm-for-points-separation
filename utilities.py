import matplotlib.pyplot as plt
import numpy as np


def generate_points_set_donut(n, x=.0, y=.0, r=1., center_r=.0):
    return_points = np.zeros((n, 2))
    radius = np.random.rand(n)
    angle = np.random.rand(n)
    return_points[:, 0] = r * ((radius + center_r) / (center_r + 1)) * np.cos(2 * np.pi * angle) + x
    return_points[:, 1] = r * ((radius + center_r) / (center_r + 1)) * np.sin(2 * np.pi * angle) + y
    return return_points


def generate_points_set(n, x=.0, y=.0, r=1.):
    return_points = np.zeros((n, 2))
    radius = np.random.rand(n)
    angle = np.random.rand(n)
    return_points[:, 0] = r * radius * np.cos(2 * np.pi * angle) + x
    return_points[:, 1] = r * radius * np.sin(2 * np.pi * angle) + y
    return return_points


def count_polynomial(arguments, parameters):
    return_values = np.zeros(np.shape(arguments))
    for i in range(np.shape(parameters)[0]):
        return_values += parameters[-i - 1] * (arguments ** i)
    return return_values


def fitness_basic(x):
    return np.copy(np.where(x > 0, x, 0))


def fitness_close_to_zero(x):
    return np.where(x > 0, x, 5 - x)


def crossover(parents):
    new_gene = np.zeros(np.shape(parents)[1:])
    for column in range(np.shape(parents)[1]):
        new_gene[column] = np.copy(parents[np.random.randint(np.shape(parents)[0]), column])
    return new_gene


def mutation(gene, sigma):
    return gene + np.random.randn(*np.shape(gene)) * sigma


def select_from_population(population, n):
    p = np.arange(0, np.shape(population)[0]) + 1
    p = 1 / (p + 1)
    p = p / np.sum(p)
    choices = np.random.choice(np.arange(0, np.shape(population)[0]) + 1, n, replace=False, p=p)
    choices = np.sort(choices)
    return population[choices - 1]


def show_fitness_function():
    plot = plt.figure("Fitness function")
    points = np.arange(-3, 3, 0.05)
    plt.plot(points, fitness_basic(points), "--")
    plot.show()


def showcase_cross_and_mut():
    parents = np.round(np.random.rand(3, 5) * 10)
    print("Parents:\n", parents)
    new_gene = crossover(parents)
    print("New gene:\n", new_gene)
    mutated_new_gene = mutation(new_gene, 1)
    print("Mutated gene:\n", mutated_new_gene)


def showcase_selection():
    p = np.arange(0, 100) + 1
    print("Sample points\n", p)
    propabilities = 1 / (p + 1)
    propabilities = propabilities / sum(propabilities)
    print("Propabilities\n", propabilities)
    selection = np.random.choice(p, 50, replace=False, p=propabilities)
    print("Choosen population\n", selection)
    print("Choosen population (Sorted)\n", np.sort(selection))
    print("Average number\n", np.average(selection))
