import time
from dtmfdetector import MicDetector
md=MicDetector()
print("inited!")
with md, open("l.txt", "a", encoding="UTF-8") as f:
	print("contexted!")
	o='n'
	while True:
		try:
			time.sleep(0.01)
			a=md.get_key()
			f.write(a)
			print(f'--- {a}')

		except KeyboardInterrupt:
			break