from scipy.fftpack import fft, fftfreq, rfft, rfftfreq, fftshift
from draw import Draw  # type: ignore

def FFT_with_fft_and_fftfreq(amplitude, number_of_points, samplingInterval):
    fourier_transform_results = abs(fft(amplitude))
    frequencies = fftfreq(number_of_points, samplingInterval)
    Draw(frequencies, fourier_transform_results, 'Frequency', 'Amplitude', 'with fftfreq')

def FFT_with_rfft_and_rfftfreq(amplitude, number_of_points, samplingInterval):
    fourier_transform_results = abs(rfft(amplitude))
    frequencies = rfftfreq(number_of_points, samplingInterval)
    Draw(frequencies, fourier_transform_results, 'Frequency', 'Amplitude', 'with rfftfreq')

def FFT_with_fft_and_fftfreq_shift(amplitude, number_of_points, samplingInterval):
    fourier_transform_results = abs(fftshift(fft(amplitude)))
    frequencies = fftshift(fftfreq(number_of_points, samplingInterval))
    Draw(frequencies, fourier_transform_results, 'Frequency', 'Amplitude', 'with fftshift')