# Audio file formats
# .mp3 - lossy
# .flac - lossless
# .wav - uncompressed

import wave

# Audio signal parameters
# - number of channels - mono = 1 / stereo = 2
# - sample width = number of bytes for each for sample
# - framerate/sample_rate = number of samples per second(44,100 Hz)
# - number of frames
# - values of a frames

obj = wave.open("sample01.wav", "rb")
print("Number of channels", obj.getnchannels())
print("Sample width", obj.getsampwidth())
print("Frame rate", obj.getframerate())
print("Number of frames", obj.getnframes())
print("Parameters", obj.getparams())
