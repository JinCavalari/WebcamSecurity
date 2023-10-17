from Webcam import Webcam
from Microphone import Microphone
from threading import Thread

print("Iniciando Gravação")
microphone = Microphone()
# microphone.start()
recThread = Thread(target=microphone.start, args=[])
recThread.start()

webcam = Webcam()
webcam.start()