import unittest
import sea_level_predictor
import matplotlib.pyplot as plt

class SeaLevelTestCase(unittest.TestCase):
    def setUp(self):
        self.ax = sea_level_predictor.draw_plot()

    def test_plot_lines(self):
        self.assertEqual(len(self.ax.lines), 2, "Expected two lines of best fit to be plotted.")

    def test_plot_labels(self):
        self.assertEqual(self.ax.get_xlabel(), 'Year', "Expected xlabel to be 'Year'.")
        self.assertEqual(self.ax.get_ylabel(), 'Sea Level (inches)', "Expected ylabel to be 'Sea Level (inches)'.")
        self.assertEqual(self.ax.get_title(), 'Rise in Sea Level', "Expected title to be 'Rise in Sea Level'.")

if __name__ == "__main__":
    unittest.main()