
class Mic:
	def __init__(self):
		pass

import speech_recognition as sr

import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

freq = 44100
duration = 3
recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)

print("Gravando")
sd.wait()
# write("rec.wav", freq, recording)
for i in recording:
	print(i)
print(recording)
# wv.write("rec.wav", recording, freq, sampwidth=2)

print("Fim")