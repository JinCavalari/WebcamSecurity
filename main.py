from Webcam import Webcam
from Microphone import Microphone
from threading import Thread

print("Iniciando Gravação")
microphone = Microphone()

webcam = Webcam()

# microphone.start()
Thread(target=microphone.start, args=[]).start()
webcam.start()