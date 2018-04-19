from utilities import *


class Points:
    positive = np.zeros((1, 2))
    negative = np.zeros((1, 2))

    def __init__(self):
        #np.random.seed(3536344299)
        # A normal set
        self.add_positives(generate_points_set(30, x=-1.25, y=1))
        self.add_negatives(generate_points_set(30, x=1, y=2))
        self.add_positives(generate_points_set(30, x=3.5, y=1))
        self.add_negatives(generate_points_set(30, x=6, y=2.75))
        # B overlapping set
        # self.add_positives(generate_points_set(30, x=-0.5, y=1))
        # self.add_negatives(generate_points_set(30, x=1, y=1.5))
        # self.add_positives(generate_points_set(30, x=2.25, y=0.75))
        # self.add_negatives(generate_points_set(30, x=6, y=2.75))

    def get_min_x(self):
        return np.min(np.concatenate((self.positive, self.negative)))

    def get_max_x(self):
        return np.max(np.concatenate((self.positive, self.negative)))

    def arrange_points_to_plt(self):
        plt.plot(self.positive[:, 0], self.positive[:, 1], "r.")
        plt.plot(self.negative[:, 0], self.negative[:, 1], "b.")

    def add_positives(self, points):
        if np.shape(self.positive) == (1, 2):
            self.positive = points
        else:
            self.positive = np.concatenate((self.positive, points))

    def add_negatives(self, points):
        if np.shape(self.negative) == (1, 2):
            self.negative = points
        else:
            self.negative = np.concatenate((self.negative, points))
