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

time_audio = obj.getnframes() / obj.getframerate()
print(time_audio)

frames = obj.readframes(-1)
print(type(frames), type(frames[0]))
print(len(frames) / 2)

obj.close()

obj_new = wave.open("sample_new.wave", "wb")

obj_new.setnchannels(1)
obj_new.setsampwidth(2)
obj_new.setframerate(16000)

obj_new.writeframes(frames)

obj_new.close()
