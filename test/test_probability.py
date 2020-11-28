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

    def test_normal_probability(self):
        # empirical rule (68-95-99.7 rule)
        self.assertAlmostEqual(normal_probability(-1,1), 0.6827, places=4);
        self.assertAlmostEqual(normal_probability(-2,2), 0.9545, places=4);
        self.assertAlmostEqual(normal_probability(-3,3), 0.9973, places=4);

    def test_trials(self):
        pass;
        # sample_size = 1000;
        # trials = [bernoulli_trial(0.5) for i in range(sample_size)];
        # trial_mu, trial_sigma = measure(trials);
        # model_prob = 0.5;
        # model_mu, model_sigma = binomial_to_normal(sample_size, model_prob);
        # lower_bound, upper_bound = inverse_normal_cdf(model_prob);
        # alpha_risk = 0.05; # accept as true the false alternative hypothesis (type 1 error / false positive)
        # beta_risk = normal_probability(); # accept as true the false null hypothesis (type 2 error / false negative)
        # power = 1 - beta_risk;

    def test_bernoulli_trial(self):
        # z-score / confidence level | 1.65 / 90% | 1.96 / 95% | 2.58 / 99%
        mu, sem = self.simulate(1000, bernoulli_trial, 0.5);
        z_score = (mu - 0.5) / sem; # number of standard errors from the mean
        # probability of the estimator be this close of the mean
        p_value = normal_probability(0.5 - z_score * sem, 0.5 + z_score * sem, mu=0.5, sigma=0.5);
        # eventual closeness of this level almost impossible
        self.assertLessEqual(p_value, self.alpha);

    def test_binomial_trial(self):
        # z-score / confidence level | 1.65 / 90% | 1.96 / 95% | 2.58 / 99%
        mu, sem = self.simulate(1000, binomial_trial, 2, 0.5);
        z_score = (mu - 1) / sem; # number of standard errors from the mean
        # probability of the estimator be this close of the mean
        p_value = normal_probability(1 - z_score * sem, 1 + z_score * sem, mu=1, sigma=0.70710678118);
        # eventual closeness of this level almost impossible
        self.assertLessEqual(p_value, self.alpha);

    def test_normal_bounds(self):
        self.assertAlmostEqual(normal_bounds(0.90)[0], -1.65, places=1);
        self.assertAlmostEqual(normal_bounds(0.90)[1], 1.65, places=1);
        self.assertAlmostEqual(normal_bounds(0.95)[0], -1.96, places=1);
        self.assertAlmostEqual(normal_bounds(0.95)[1], 1.96, places=1);
        self.assertAlmostEqual(normal_bounds(0.99)[0], -2.58, places=1);
        self.assertAlmostEqual(normal_bounds(0.99)[1], 2.58, places=1);

    def simulate(self, num_trials,func, *args):
        results = [func(*args) for i in range(num_trials)];        
        mean_estimator = sum(results) / num_trials;
        std_estimator = sum((result -mean_estimator) ** 2 for result in results) / num_trials;
        sem = std_estimator / num_trials ** 0.5;

        return mean_estimator, sem;

    def multiple_test(self, test_cases, func):
         x_vals, y_vals = zip(*test_cases);
         self.assertSequenceEqual(list(map(func, x_vals)), y_vals);


if __name__ == '__main__':
    unittest.main();
