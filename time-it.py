import timeit
from math import sqrt

def time_it():
    listing = []
    for x in range(50):
        listing.append(sqrt(x))

    print(listing)

time_it()