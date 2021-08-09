"""
##### NFMATH ######
Last update: 261120

Small library for basic math and statistics operations.
"""

from scipy import special as sp
import numpy as np

## Help
def tools():
    functions = {
        'Cartesian plane': [
            'get_slope',
            'point_slope',
            ],
        'Probability': [
            'binomial_probability',
            'p_draw_norepl'
            ],
    }
    return functions

## Cartesian plane
def get_slope(point_A, point_B):
    """
    Calculates slope M of the line segment formed by two points in Cartesian space.
    :point_a: :point_b: array of int/float
    :return: int
    """
    M = (point_B[1]-point_A[1]) / (point_B[0]-point_A[0])
    return M

def point_slope(point_A, point_B):
    """
    Applies point slope formula & checks if given points are on the line
    :point_a: :point_b: array of int/float
    :return: bool
    """
    M = get_slope(point_A, point_B)
    
    return point_b[1] - point_a[1] == M * (point_b[0] - point_a[0])

## Probability
def binomial_probability(successes, n_trials, p_trial):
    """
    :successes: int number of successes
    :n_trials: int number of trials
    :p_trial: float probability of 1 success
    :return: float probability of s successes in n trials
    """
    # calculate number of possible combinations
    n_choose_s = sp.comb(n_trials,successes)

    # calculate the probability of s successes
    p_power_s =  p_trial ** successes

    # calculate failure probability
    fails_base = (1 - p_trial)
    fails_power = n_trials - successes
    fails = fails_base ** fails_power

    # return probability of s successes in n trials
    return n_choose_s * p_power_s * fails

def p_draw_norepl(totals, elements):
    """
    Calculate probability with no replacement
    :totals: int number of possible items in the universe
    :elements: int number of items we want to draw
    :return: the probability of drawing n elements from n totals in n draws
    """
    p_distr = []

    while elements != 0:
        # print('elements:', elements, ' / totals ', totals)
        p_draw = elements/totals
        p_distr.append(p_draw)
        elements -= 1
        totals -= 1
    
    probability = np.prod(p_distr)

    return probability
