from levantar_espectro_rafa import spectro
import pytest

class Test_Load_spectrum():

#def not_empty(spec):
#	if spec is empty rise error
#import pytest

    @pytest.fixture
    def spectrum(self):
        spect = spectro('/home/fenix/Documents/WorkWorkWork/NGC4945/esp_finales/cfgal01.0001.fits',0)
        return spect
   
    def test_match(self, spectrum):
        assert spectrum.spectral_axis.shape == spectrum.flux.shape
	
	
    #def test_unities(self):
    #	assert u.spec.spectral_axis = 'AA'
    #	assert u.spec.flux = 'erg cm-2 s-1 AA-1'	
	
	
    def test_header(self, spectrum):
        assert type(spectrum.header['EXPTIME']) == float
        assert spectrum.header['EXPTIME'] >= 0.
        
        
    def test_wav_axis(self, spectrum):
        assert spectrum.header['CD1_1'] >=0.
        assert spectrum.header['CTYPE1'] == 'LINEAR'
