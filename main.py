import numpy as np
import argparse
from draw import Draw  # type: ignore
from fft_step_by_step import FFT_step_by_step  # type: ignore
from scipy_fft import FFT_with_fft_and_fftfreq, FFT_with_rfft_and_rfftfreq, FFT_with_fft_and_fftfreq_shift  # type: ignore

parser = argparse.ArgumentParser(description='Fast Fourier Transform experiments with different scipy functions')
parser.add_argument('--fs', default=100, type=int, help='sampling frequency')
parser.add_argument('--fw', default=10, type=int, help='frequency of the wave (Hz)')
parser.add_argument('--t', default=5, type=int, help='time period')

def main():
    args = parser.parse_args()
    samplingFrequency = args.fs
    samplingInterval = 1 / samplingFrequency
    signalFrequency = args.fw

    time = np.arange(0, args.t, samplingInterval)  # Time points
    amplitude = np.sin(2 * np.pi * signalFrequency * time)  # create wave

    number_of_points = len(time)
    Draw(time, amplitude, 'time', 'amplitude', '1Hz + 2Hz + 3Hz sine wave')
    
    FFT_step_by_step(samplingFrequency, amplitude, number_of_points)
    FFT_with_fft_and_fftfreq(amplitude, number_of_points, samplingInterval)
    FFT_with_rfft_and_rfftfreq(amplitude, number_of_points, samplingInterval)
    FFT_with_fft_and_fftfreq_shift(amplitude, number_of_points, samplingInterval)
    
if __name__ == '__main__':
    main()



