import sys
from scipy.io import wavfile  # get the api

import matplotlib.pyplot as plt
import timeit


class Analyzer():
    def __init__(self, fulladdress):
        self.fs, self.data = wavfile.read(fulladdress)  # load the data
        print 'sampling =', self.fs, 'Hz'
        start_time = timeit.default_timer()
        self.ms_tuple = plt.magnitude_spectrum(
            self.data,
            self.fs,
            pad_to=10000,
        )
        elapsed = timeit.default_timer() - start_time
        print 'magnitude spectrum in', elapsed, 'seconds'


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print 'add wav file as argument'
        exit(-1)

    Analyzer(sys.argv[1])
