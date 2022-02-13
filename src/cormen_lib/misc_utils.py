import sys
import math

INF = sys.maxsize
'''Integer constant representing infinity.'''

NEG_INF = -sys.maxsize
'''Integer constant representing negative infinity.'''

def ceil(x):
    '''Returns x rounded up to the nearest integer.'''
    return math.ceil(x)

def floor(x):
    '''Returns x truncated.'''
    return math.floor(x)