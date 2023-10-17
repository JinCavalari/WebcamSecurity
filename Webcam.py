import cv2
from pynput import keyboard
from datetime import datetime
from threading import Thread
import time
import numpy as np

class Webcam:
	def __init__(self):
		self.cam = cv2.VideoCapture(0)
		if not self.cam.isOpened():
			raise IOError("Cannot open webcam")
		self.size = (640, 480)
		self.end = False
		self.openCam = True
		self.camera = None
		self.listener = None
		self.keys = []
		self.recThread = None
		self.frame = None
		self.prev_frame = None
		self.prev_frame_dilated = None
		self.motionDetected = False
		self.recSecOrgin = 3
		self.recSec = self.recSecOrgin

	def motionDetect(self):
		if self.prev_frame is None:
			self.prev_frame = self.frame

		diff = cv2.absdiff(self.prev_frame, self.frame)
		gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
		blur = cv2.GaussianBlur(gray, (21, 21), 0)

		thresh = cv2.threshold(blur, 25, 255, cv2.THRESH_BINARY)[1]
		dilated = cv2.dilate(thresh, None, iterations=3)
 
		if self.prev_frame_dilated is None:
			self.prev_frame_dilated = dilated

		result = np.abs(np.mean(dilated) - np.mean(self.prev_frame_dilated))
		self.prev_frame = self.frame
		self.prev_frame_dilated = dilated

		if result != 0:
			self.recSec = self.recSecOrgin
			# print("Motion Detected: ", result)

			if self.motionDetected is False:
				self.motionDetected = True
				if self.rcdCam:
					# print(self.camera)
					if self.camera != None: self.camera.release()
					self.camera = cv2.VideoWriter(
						filename = "recs/"+str(datetime.now()).replace(":", ";")+".mp4",
						fourcc = cv2.VideoWriter_fourcc(*'IYUV'),# IYUV / DIVX
						fps = 30,
						frameSize = self.size)
				self.recThread = Thread(target=self.pauseRec, args=[])
				self.recThread.start()

	def on_press(self, key):
		if key not in self.keys:
			self.keys.append(key)
			if keyboard.Key.alt_l in self.keys and keyboard.Key.ctrl_l in self.keys and keyboard.Key.shift in self.keys:
				self.end = True
				self.camera.release()
				return False

	def on_release(self, key):
		if key in self.keys:
			self.keys.remove(key)

	def pauseRec(self):
		while True:
			time.sleep(1)
			self.recSec -= 1
			if self.recSec <= 0 or self.end:
				self.motionDetected = False
				self.camera.release()
				break

	def start(self, rcdCam = True):
		self.rcdCam = rcdCam

		self.listener = keyboard.Listener( on_press=self.on_press, on_release=self.on_release)
		self.listener.start()

		fc = 0
		while not self.end:
			ret, self.frame = self.cam.read()
			if ret:
				frame = np.copy(self.frame)
				if fc >= 5 and self.rcdCam:
					fc = 0
					self.motionDetect()

				date = datetime.now()
				text = date.strftime("%d")+"/"+date.strftime("%m")+"/"+date.strftime("%Y")+" "+date.strftime("%H")+":"+date.strftime("%M")+":"+date.strftime("%S")
				# size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1.5, 5)[0]
				cv2.putText(frame, text, (10, self.size[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 5)
				cv2.putText(frame, text, (10, self.size[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
				if self.openCam:
					cv2.imshow('Input', frame)
					c = cv2.waitKey(1)
					if c == 27: break

				if self.rcdCam and self.motionDetected:
					try:
						self.camera.write(frame)
					except Exception as e:
						print(e)
			fc += 1

		cv2.destroyAllWindows()

# webcam = Webcam()
# webcam.start()