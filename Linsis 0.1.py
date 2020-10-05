import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
from specutils import Spectrum1D
import specutils
from astropy import units as u

#tiene que heredar de Spectrum1D en algún momento

class spectro(Spectrum1D):
    def __init__(self,spectrum,datastorage, flux_unit=None, \
    wav_unit=None, wcs=None, velocity_convention=None, rest_value=None,\
    redshift=None, radial_velocity=None, bin_specification=None, \
    uncertainty=None, mask=None, meta=None):
        
        self.spectrum = fits.open(spectrum)
        self.datos = self.spectrum[datastorage].data
        self.header = fits.getheader(spectrum)
        
              
        
        #se construye el objeto tipo Spectrum1D
        spectral_axis = (self.header['CRVAL1'] +  self.header['CD1_1']*np.arange(0,len(self.datos)))*u.AA
        super().__init__(flux=self.datos*u.adu, \
        spectral_axis=spectral_axis, wcs=wcs, \
        velocity_convention=velocity_convention, rest_value=rest_value,\
        redshift=redshift, radial_velocity=radial_velocity, \
        bin_specification=bin_specification, uncertainty=uncertainty, \
        mask=mask, meta=meta)
	
    #Este metodo seria privado para asignar las unidades en caso de ser introducidas por el usuario pero no funciona	
    #def _set_units(self,flux_unit,wav_unit):
        #if flux_unit == None: pass
        #if wav_unit == None: pass
		
        #else: funit = flux_unit and wunit = wav_unit

        #atributo para plotear   
        self.plot = plt.plot(self.spectral_axis,self.flux)


spec1 = spectro('/home/fenix/Documents/WorkWorkWork/NGC4945/esp_finales/cfgal01.0001.fits',0)

spec1.datos
