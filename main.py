from masterController import *
from points import *

if __name__ == "__main__":
    points = Points()
    show_fitness_function()
    plt.show()
    master_controller = MasterController(points,
                                         genes=6,
                                         population_part=2,
                                         mutation_sigma=.5)
    master_controller.generate_till_best_fitness_less_equals_than(fitness=1,
                                                                  max_generations=125,
                                                                  mutation_saturation=0.95)
    master_controller.arange_last_best_to_plot()
    points.arrange_points_to_plt()
    plt.grid()
    plt.show()
    master_controller.arange_best_of_all()
    points.arrange_points_to_plt()
    plt.grid()
    plt.show()
    master_controller.arange_all_bests_to_plot()
    points.arrange_points_to_plt()
    plt.show()
    master_controller.arange_stats_to_plot()
    plt.show()
