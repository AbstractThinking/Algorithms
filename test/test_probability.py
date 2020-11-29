import unittest;

from algorithms.probability import *;


class ProbabilityCase(unittest.TestCase):

    def setUp(self):
        self.alpha = 0.05;

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
        self.assertAlmostEqual(join(1/6, 3/6, 0), 4/6);
        self.assertAlmostEqual(join(1/6, 3/6, 1/3), 3/6);

    def test_exclusive(self):
        # any of the two exclusive events in the trial
        # coin flip for head or tail
        self.assertEqual(exclusive(0.5, 0.5), 1);

    def test_intersect(self):
        # both of the independent events in two different trials
        # two coin flips for two sequential faces 
        self.assertEqual(intersect(0.5, 0.5), 0.25);

    def test_uniform(self):
        self._multiple_test([(-2, 0), (0, 1), (0.5, 1), (1, 0), (2, 0)], uniform_pdf);
            
    def test_uniform_cdf(self):
        self._multiple_test([(-2, 0), (0, 0), (1/2, 0.5), (3/4-1/4, 0.5), (1, 1), (2, 1)], uniform_cdf);

    def _multiple_test(self, test_cases, func):
         x_vals, y_vals = zip(*test_cases);
         self.assertSequenceEqual(list(map(func, x_vals)), y_vals);   
 
    def test_normal_cdf(self):
        # check if less than mu probability is 50% (0.5)
        self.assertEqual(normal_cdf(0), 0.5);

        # compare against phi table
        self.assertAlmostEqual(normal_cdf(-1), 0.1587, places=4);
        self.assertAlmostEqual(normal_cdf(1), 0.8413, places=4);

    def test_normal_probability(self):
        # empirical rule (68-95-99.7 rule)
        self.assertAlmostEqual(normal_probability(-1,1), 0.6827, places=4);
        self.assertAlmostEqual(normal_probability(-2,2), 0.9545, places=4);
        self.assertAlmostEqual(normal_probability(-3,3), 0.9973, places=4);

    def test_bernoulli_trial(self):
        self.assertLessEqual(self._get_p_value(0.5, 0.5, bernoulli_trial, 0.5), self.alpha);

    def test_binomial_trial(self):
        self.assertLessEqual(self._get_p_value(1, 0.70710678118, binomial_trial, 2, 0.5), self.alpha);

    def _get_p_value(self, mu, sigma, func, *args):
        mu_bar, sem = self._simulate(10000, func, *args);

        # number of standard errors from the mean
        z_score = (mu_bar - mu) / sem;

        # return probability of the estimator be this close of the mean
        return normal_probability(mu - z_score * sem, mu + z_score * sem, mu=mu, sigma=sigma);

    def test_normal_bounds(self):
        self.assertAlmostEqual(normal_bounds(0.95)[0], -1.96, places=1);
        self.assertAlmostEqual(normal_bounds(0.95)[1], 1.96, places=1);

    def _simulate(self, num_trials, func, *args):
        trial_results = [func(*args) for i in range(num_trials)];

        mean_estimator = self._get_mean(trial_results, num_trials);
        std_estimator = self._get_std(trial_results, num_trials, mean_estimator);
        sem = std_estimator / num_trials ** 0.5;
        
        return mean_estimator, sem;

    def _get_mean(self, vals, n):
        return sum(vals) / n;

    def _get_std(self, vals, n, mean):
        sse = [(val - mean) ** 2 for val in vals];
        return self._get_mean(sse, n);        

    
if __name__ == '__main__':
    unittest.main();
