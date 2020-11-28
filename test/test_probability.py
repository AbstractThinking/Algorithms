import unittest;

from algorithms.probability import *;


class ProbabilityCase(unittest.TestCase):

    def test_complement(self):
        # not occur the given event in the trial
        # select between any digit a different one
        self.assertAlmostEqual(complement(0.1), 0.9);

    def test_total(self):
        # occur indirect event as union of exclusive dependencies
        # Monty Hall opens the door with goat behind it 
        self.assertEqual(total(1/3, 1, 1), 1);
        
        # dice roll for Fibonacci, knowing chances for parities
        self.assertEqual(total(1/2, 1/3, 1), 4/6);

    def test_condition(self):
        # occur (in)dependent event given the prior occurrence
        # Monty Hall problem, consideration of new information
        self.assertEqual(condition(1, 1/3, 1), 1/3);
        self.assertEqual(condition(1, 2/3, 1), 2/3);

    def test_join(self):
        self.assertAlmostEqual(join(1/6,3/6,0), 4/6);
        self.assertAlmostEqual(join(1/6,3/6,1/3), 3/6);

    def test_exclusive(self):
        # any of the two exclusive events in the trial
        # coin flip for head or tail
        self.assertEqual(exclusive(0.5, 0.5), 1);

    def test_intersect(self):
        # both of the independent events in two different trials
        # two coin flips for two sequential faces 
        self.assertEqual(intersect(0.5, 0.5), 0.25);

    def test_uniform(self):
        self.multiple_test([(-2, 0), (0, 1), (0.5, 1), (1, 0), (2, 0)], uniform_pdf);
            
    def test_uniform_cdf(self):
        self.multiple_test([(-2, 0), (0, 0), (1/2, 0.5), (3/4-1/4, 0.5), (1, 1), (2, 1)], uniform_cdf);

    def test_normal_cdf(self):
        self.assertEqual(normal_cdf(0), 0.5);

        # compare against phi table
        self.assertAlmostEqual(normal_cdf(-1), 0.1587, places=4);
        self.assertAlmostEqual(normal_cdf(1), 0.8413, places=4);

        # empirical rule (68-95-99.7 rule)
        self.assertAlmostEqual(normal_cdf(1) - normal_cdf(-1), 0.6827, places=4);
        self.assertAlmostEqual(normal_cdf(2) - normal_cdf(-2), 0.9545, places=4);
        self.assertAlmostEqual(normal_cdf(3) - normal_cdf(-3), 0.9973, places=4);

    def test_bernoulli(self):
        # coin flip simulation for the given coin side with 100 sample of size 100
        population_mean, population_std, sem = self.simulate(bernoulli_trial, 0.5);

        self.assertAlmostEqual(population_mean, 0.5, places=1);
        self.assertAlmostEqual(population_std, 0.5, places=1);

    def test_binomial_trial(self):
        # coin flip simulation for two sequential coin sides with 100 sample of size 100
        population_mean, population_std, sem = self.simulate(binomial_trial, 0.5, 2);

        self.assertAlmostEqual(population_mean, 1, places=1);
        self.assertAlmostEqual(population_std, 0.7, places=1);


    def simulate(self, func, *args):
        # central limit theorem for computing population mean and variance
        num_trials = 100;
        trial_size = 100;
        
        sample_means = [];
        squared_errors= [];

        for i in range(num_trials):
            trial_results = [];

            for j in range(trial_size):
                trial_results.append(func(*args));

            sample_means.append(sum(trial_results) / trial_size);
            squared_errors += [(trial_result - sample_means[-1]) ** 2 for trial_result in trial_results];

        population_mean = sum(sample_means) / num_trials;
        population_std = sum(squared_errors) / (num_trials * sample_size);
        sem = population_std / num_trials ** 0.5;

        return population_mean, population_std, sem;

    def multiple_test(self, test_cases, func):
         x_vals, y_vals = zip(*test_cases);
         self.assertSequenceEqual(list(map(func, x_vals)), y_vals);


if __name__ == '__main__':
    unittest.main();
