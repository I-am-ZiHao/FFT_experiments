from scipy.fftpack import fft
import numpy as np
from draw import Draw  # type: ignore

def FFT_step_by_step(samplingFrequency, amplitude, number_of_points):

    # step1
    fourier_transform_results = fft(amplitude)

    # step2: 換成 Magnitude
    fourier_transform_results = abs(fourier_transform_results)
    frequencies = np.arange(number_of_points) * samplingFrequency / number_of_points
    Draw(frequencies, fourier_transform_results, 'Frequency', 'Amplitude', 'step2: Magnitude')

    # step3: 取前半
    fourier_transform_results = fourier_transform_results[range(int(number_of_points / 2))]
    frequencies = np.arange(int(number_of_points / 2)) * samplingFrequency / number_of_points
    Draw(frequencies, fourier_transform_results, 'Frequency', 'Amplitude', 'step3: Take the first half')

    # step4: double magnitude
    fourier_transform_results = fourier_transform_results * 2
    Draw(frequencies, fourier_transform_results, 'Frequency', 'Amplitude', 'step4: Double Magnitude')

    # step5: normalize
    fourier_transform_results = fourier_transform_results / number_of_points
    Draw(frequencies, fourier_transform_results, 'Frequency', 'Amplitude', 'step5: Normalize')