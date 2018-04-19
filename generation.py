from utilities import *


class Generation:
    points = None
    population = None
    fitness = None

    def __init__(self, points, population_size=100, genes=3, population=None, value_range=3):
        self.points = points
        if population is None:
            self.generate_start_population(population_size, genes, value_range)
        else:
            self.population = population
        self.fitness = np.zeros(self.population.shape[0])
        self.calculate_total_fitness()
        self.sort_by_fitness()

    def generate_start_population(self, n, genes, value_range):
        self.population = (2 * np.random.random((n, genes)) - 0.5) * value_range

    def arange_best_chromosome_to_plot(self):
        pt = np.arange(self.points.get_min_x(), self.points.get_max_x(), 0.1)
        v = count_polynomial(pt, self.population[0])
        plt.plot(pt, v, "--")

    def arange_all_chromosomes_to_plot(self):
        pt = np.arange(self.points.get_min_x(), self.points.get_max_x(), 0.1)
        for chromosome in self.population:
            v = count_polynomial(pt, chromosome)
            plt.plot(pt, v, "--")

    def calculate_total_fitness(self):
        for i in range(np.shape(self.population)[0]):
            self.fitness[i] = self.get_fitness_of_chromosome(self.population[i])

    def get_fitness_of_chromosome(self, chromosome):
        fitness = 0
        polynomial_values_positive = count_polynomial(self.points.positive[:, 0], chromosome)
        polynomial_values_negative = count_polynomial(self.points.negative[:, 0], chromosome)
        fitness += np.sum(fitness_basic(self.points.positive[:, 0] - polynomial_values_positive))
        fitness += np.sum(fitness_basic(polynomial_values_negative - self.points.negative[:, 0]))
        return fitness

    def sort_by_fitness(self):
        sortedd = self.fitness.argsort()
        self.population = self.population[sortedd]
        self.fitness = self.fitness[sortedd]

    def get_best_chromosome(self):
        return self.population.min()

    def get_worst_chromosome(self):
        return self.population.max()

    def get_best_fitness(self):
        return self.fitness.min()

    def get_standard_deviation(self):
        return np.std(self.fitness)

    def get_avg_fitness(self):
        return np.sum(self.fitness) / self.fitness.shape[0]
