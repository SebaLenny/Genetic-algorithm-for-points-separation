from generation import *


class MasterController:
    points = None
    generations = []
    population_size = 0
    averages = []
    bests = []
    mutation_sigma = 0
    population_part = 2

    def __init__(self, points, population_size=100, genes=3, mutation_sigma=.5, population_part=2, value_range=5):
        self.points = points
        self.generations.append(Generation(points, population_size, genes, value_range=value_range))
        self.update_stats_from_last_gen()
        self.population_size = population_size
        self.mutation_sigma = mutation_sigma
        self.population_part = population_part

    def update_stats_from_last_gen(self):
        self.averages.append(self.get_last_generation().get_avg_fitness())
        self.bests.append(self.get_last_generation().get_best_fitness())

    def generate_till_best_fitness_less_equals_than(self, fitness, max_generations=np.inf, mutation_saturation=1):
        while self.get_last_generation().get_best_fitness() > fitness and len(self.generations) < max_generations:
            self.generate_next_generation(sigma=self.mutation_sigma, population_part=self.population_part)
            self.update_stats_from_last_gen()
            self.mutation_sigma *= mutation_saturation

    def arange_last_best_to_plot(self):
        plt.figure("Last best chromosome")
        self.generations[-1].arange_best_chromosome_to_plot()

    def arange_best_of_all(self):
        best_fitness = np.inf
        best_gen = None
        for gen in range(len(self.generations)):
            if best_fitness > self.generations[gen].get_best_fitness():
                best_fitness = self.generations[gen].get_best_fitness()
                best_gen = self.generations[gen]
        plt.figure("Best chromosome ever")
        best_gen.arange_best_chromosome_to_plot()

    def arange_all_bests_to_plot(self):
        plt.figure("Best chromosomes from all gens")
        for gen in self.generations:
            gen.arange_best_chromosome_to_plot()

    def arange_stats_to_plot(self):
        plt.figure("Max and average for each generation")
        averages = np.zeros(len(self.generations))
        maxes = np.zeros(len(self.generations))
        stds = np.zeros(len(self.generations))
        for gen in range(len(self.generations)):
            averages[gen] = self.generations[gen].get_avg_fitness()
            maxes[gen] = self.generations[gen].get_best_fitness()
            stds[gen] = self.generations[gen].get_standard_deviation()
        plt.subplot(311)
        plt.ylabel("Average chrom.")
        plt.plot(averages)
        plt.subplot(312)
        plt.ylabel("Best chrom.")
        plt.plot(maxes)
        plt.subplot(313)
        plt.ylabel("Standard deviation")
        plt.plot(stds)

    def get_last_generation(self):
        return self.generations[-1]

    def generate_next_generation(self, sigma=.5, population_part=2):
        old_gen = self.get_last_generation()
        selected_population = select_from_population(old_gen.population,
                                                     np.shape(old_gen.population)[0] // population_part)
        holder = np.zeros((self.population_size - np.shape(selected_population)[0],
                           np.shape(selected_population)[1]))
        for i in range(np.shape(holder)[0]):
            holder[i] = crossover(select_from_population(selected_population, 3))
        new_gen = np.copy(mutation(np.append(selected_population, holder, axis=0), sigma=sigma))
        self.generations.append(Generation(self.points, population=new_gen))
