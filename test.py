from pylab import *
import cufft

i = arange(2**16)
Signal = sin(i) + sin(i/3.) + sin(i/17.)/8.

from numpy.fft import rfft
plot(abs(rfft(Signal)),'ob', mew=0, ms=8)
plot(abs(cufft.rfft(Signal)), 'or', mew=0, ms=3)

show()