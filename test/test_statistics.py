import unittest;

from algorithms.statistics import Statistics;

class StatisticsCase(unittest.TestCase):

    def setUp(self):
        self.dataset = [1, 2, 3, 4, 5];
        self.empty_list = [];
        self.not_list = (1, 2, 3);
        self.nan_items = [1, 'a', 3];
        self.statistics = Statistics();

    def test_mean(self):
        self.assertEqual(self.statistics.mean(self.dataset), 3);
        self.assertEqual(self.statistics.mean(self.empty_list), 0);

    def test_variance(self):
        self.assertEqual(self.statistics.variance(self.dataset), 2.5);
        self.assertEqual(self.statistics.variance(self.dataset, sample = True), 2.5);
        self.assertEqual(self.statistics.variance(self.dataset, sample = False), 2);
        self.assertEqual(self.statistics.variance(self.empty_list), 0);

    def test_std_dev(self):
        self.assertEqual(round(self.statistics.std_dev(self.dataset), 2), 1.58);
        self.assertEqual(round(self.statistics.std_dev(self.dataset, sample = True), 2), 1.58);
        self.assertEqual(round(self.statistics.std_dev(self.dataset, sample = False), 2), 1.41);

    def test_check_instance(self):
        with self.assertRaises(TypeError):
            self.statistics._check_instance(self.not_list);
        with self.assertRaises(TypeError):
            self.statistics._check_instance(self.nan_items);
[]
if __name__ == '__main__':
    unittest.main();
