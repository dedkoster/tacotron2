from scipy.io.wavfile import read

list = [r'Ruslan\000000_RUSLAN.wav', r'..\..\tacotron2\DUMMY\LJ001-0001.wav']

for path in list:
    sampling_rate, data = read(path)
    print()
