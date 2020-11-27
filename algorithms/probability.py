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

def bernoulli_trial(p):
    return 1 if random.random() < p else 0;

def binomial_trial(p, n):
    return sum([bernoulli_trial(p) for i in range(n)]);