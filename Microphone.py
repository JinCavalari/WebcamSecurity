from datetime import datetime
from pynput import keyboard
from threading import Thread
import pyaudio
import wave
from time import sleep

class Microphone:
    def __init__(self):
        self.freq = 44100
        self.end = False
        self.filename = None

        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(format=pyaudio.paInt16, channels=1, rate=self.freq, input=True, frames_per_buffer=1024)
        self.frames = [[], []]

        self.init_time_rec = None
        self.time_rec = 10
        self.idxRec = 0
        self.listener = None
        self.keys = []

    def on_press(self, key):
        if key not in self.keys:
            self.keys.append(key)
            if keyboard.Key.alt_l in self.keys and keyboard.Key.ctrl_l in self.keys and keyboard.Key.shift in self.keys:
                self.end = True

                self.stream.stop_stream()
                self.stream.close()
                self.audio.terminate()

                self.saveAudio()

                return False

    def on_release(self, key):
        if key in self.keys:
            self.keys.remove(key)

    def timer(self):
        while not self.end:
            sleep(0.5)
            if int((datetime.now() - self.init_time_rec).total_seconds()) >= self.time_rec:
                self.init_time_rec = datetime.now()
                self.saveAudio()
                self.filename = "recs/"+str(datetime.now()).replace(":", ";")+".wav"

    def start(self):
        self.listener = keyboard.Listener( on_press=self.on_press, on_release=self.on_release)
        self.listener.start()
        
        Thread(target=self.timer, args=[]).start()
        
        while not self.end:
            self.init_time_rec = datetime.now()
            self.filename = "recs/"+str(datetime.now()).replace(":", ";")+".wav"
            while not self.end:
                data = self.stream.read(1024)
                self.frames[self.idxRec%2].append(data)
                # print(data)
                # print(data.decode(encoding="iso8859"))
                # break

    def saveAudio(self):
        self.idxRec += 1
        sound_file = wave.open(self.filename, "wb")
        sound_file.setnchannels(1)
        sound_file.setsampwidth(self.audio.get_sample_size(pyaudio.paInt16))
        sound_file.setframerate(self.freq)
        sound_file.writeframes(b''.join(self.frames[(self.idxRec+1)%2]))
        sound_file.close()
        self.frames[(self.idxRec+1)%2] = []
