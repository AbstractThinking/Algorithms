import math;
import random;

def complement(prob_a):
    return 1 - prob_a;


def condition(prob_b_given_a, prob_a, prob_b):
    return prob_b_given_a * prob_a / prob_b;


def exclusive(prob_a, prob_b):
    return prob_a + prob_b;


def intersect(prob_a_given_b, prob_b):
    return prob_a_given_b * prob_b;


def join(prob_a, prob_b, prob_a_given_b):
    return prob_a + prob_b - intersect(prob_a_given_b, prob_b);


def total(prob_a, prob_b_given_a, prob_b_given_not_a):
    return prob_a * prob_b_given_a + complement(prob_a) * prob_b_given_not_a;


def probability(event_size, universe_size):
    return event_size / universe_size;


def expect(dist):
    return sum(x * y for x, y in dist);


def uniform_pdf(x):
    return 1 if x >= 0 and x < 1 else 0; 


def uniform_cdf(x):
    if x < 0:
        return 0;
    elif x > 1:
        return 1;
    else:
        return x;  


def normal_pdf(x, mu=0, sigma=1):
    return math.exp(-((x-mu)**2) / (2*sigma**2))  /  (math.sqrt(2*math.pi) * sigma);


def normal_cdf(x,  mu=0, sigma=1):
    return (1 + math.erf((x-mu)/(sigma*2**0.5))) / 2;


def inverse_normal_cdf(prob, mu, sigma, precision=0.001):
    is_not_std = mu != 0 and sigma != 1; 
    std_search = lambda prob: inverse_normal_cdf(prob, 0, 1);
    transform_z_to_x = lambda z, mu, sigma:  mu + sigma * z; 

    if is_not_std:
        return transform_z_to_x(std_search(prob));

    return _binary_search_z(prob);


def _binary_search_z(prob_to_search, precision=0.001):
    z_low = -10;
    z_high = 10;

    while z_high - z_low > precision:
        z_mid = (z_low + z_high) / 2;
        z_prob = normal_cdf(z_mid);

        if z_prob < prob_to_search:
            z_low = z_mid;
        elif z_prob > prob_to_search:
            z_high = z_mid;
        else:
            break;

    return z_mid;


def bernoulli_trial(prob):
    return 1 if random.random() < prob else 0;


def binomial_trial(n, prob):
    return sum([bernoulli_trial(prob) for i in range(n)]);


def normal_bounds(prob, mu=0, sigma=1):
    tail_prob = complement(prob) / 2;
    lower_bound = inverse_normal_cdf(tail_prob, mu, sigma);
    upper_bound = inverse_normal_cdf(complement(tail_prob), mu, sigma);

    return lower_bound, upper_bound;


def normal_probability(a, b, mu=0, sigma=1):
    return abs(normal_cdf(a, mu, sigma) - normal_cdf(b, mu, sigma))