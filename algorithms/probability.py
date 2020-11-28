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
    transform_z_to_x = lambda z, mu, sigma:  mu + sigma * z; 
    
    if is_not_std:
        z = inverse_normal_cdf(prob, 0, 1);
        x = transform_z_to_x(z, 0, 1);

        return x;

    low_z = -10.0;
    high_z = 10.0;

    while high_z - low_z > precision:
        mid_z = (low_z + high_z) / 2;
        mid_p = normal_cdf(mid_z);

        if mid_p < prob:
            low_z = mid_z;
        elif mid_p > prob:
            high_z = mid_z;
        else:
            break;

    return mid_z;

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