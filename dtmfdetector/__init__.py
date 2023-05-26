import sys
from time import time as now, sleep
from .dtmfdetector import Detector
import sounddevice as sd
import queue
import numpy  # Make sure NumPy is loaded before it is used in the callback
assert numpy  # avoid "imported but unused" message (W0611)
bs=0

class MicDetector:
	def __init__(self):
		self.tone='n'
		self.q=queue.Queue()
		self.device_info = sd.query_devices(None, 'input')
		#self.samplerate = int(self.device_info['default_samplerate'])
		self.samplerate=44100
		self.detector=Detector(int(self.samplerate))
		self.time=now()

	def __enter__(self):
		self.stream=sd.InputStream(samplerate=self.samplerate, device=None, channels=1, dtype='float32', blocksize=bs, callback=self.callback)
		self.stream.start()
	def __exit__(self, type, value, traceback):
		self.stream.close()


	def callback(self, indata, frames, time, status):
		if status:
			print(status, file=sys.stderr)
		self.q.put(indata.copy())
		#print(self.q.unfinished_tasks)
		self.time=now()

	def update(self, slp=False):
		if slp: sleep(0.005)
		if self.q.empty(): return self.detector.last_tone
		self.detector.decode(self.q.get() )
		self.q.task_done()
		return self.detector.last_tone

	def get_key(self):
		changed=False
		self.tone=self.update(True)
		while not changed:
			k=self.tone
			self.tone=self.update()
			changed=(self.tone!='n' and k!=self.tone)
		return self.tone
