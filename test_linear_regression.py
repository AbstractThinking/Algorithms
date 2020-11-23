import unittest;

from algorithms.linear_regression import RegressionLine;

class RegressionLineCase(unittest.TestCase):

    def setUp(self):
        self.dataset = [(i,i) for i in range(1000)]
        self.regression_line = RegressionLine(self.dataset);

    def test_predict(self):
        self.assertLessEqual(abs(self.regression_line.predict(1001) - 1001), 1)

if __name__ == '__main__':
    unittest.main();