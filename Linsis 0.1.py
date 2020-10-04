from astropy.io import fits
import matplotlib.pyplot as plt
from specutils import Spectrum1D


#tiene que heredar de Spectrum1D en algún momento

class spectro(Spectrum1D):
    def __init__(self,spectrum,datastorage,flux=None,spectral_axis=None):
        self.spectrum = fits.open(spectrum)
        self.datos = self.spectrum[datastorage].data
        self.header = fits.getheader(spectrum)
        #self.plot = plt.plot(self.datos)

spec1 = spectro('/Users/RULO/Desktop/cfgal01.0001.fits',0)

spec1.header
