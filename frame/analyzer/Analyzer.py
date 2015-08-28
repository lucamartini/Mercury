import sys
# from scipy.io import wavfile  # get the api

import matplotlib
import matplotlib.pyplot as plt
import timeit
import csv


class Analyzer():
    def __init__(self, fulladdress):
        self.data = []
        self.fs = 10000
        with open(fulladdress) as datafile:  # load the data
            datareader = csv.reader(datafile, delimiter=';')
            fileline = 0
            acquisitions = -1
            for row in datareader:
                fileline = fileline+1
                if fileline > 29:
                    if row[1] is '0':
                        print row
                        acquisitions = acquisitions + 1
                        self.data.append([])
                    ch1 = float(row[2].replace(',', '.'))
                    self.data[acquisitions].append(ch1)

        print 'there are', len(self.data), 'acquisitions of lenght:'
        for acq in self.data:
            print(len(acq)),

        self.fftdata = self.data[0]
        print '\nfor now take the first:', len(self.fftdata)

        start_time = timeit.default_timer()
        self.ms_tuple = plt.magnitude_spectrum(
            self.fftdata,
            Fs=self.fs,
            window=matplotlib.mlab.window_none,
            # pad_to=10000,
        )
        elapsed = timeit.default_timer() - start_time
        print 'magnitude spectrum in', elapsed, 'seconds'


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print 'add csv file as argument'
        exit(-1)

    Analyzer(sys.argv[1])
