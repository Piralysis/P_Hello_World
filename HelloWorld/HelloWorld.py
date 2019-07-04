import sys
import time
import random

class Application:
	def __init__(self):
		self.output = list()
		self.now = None
		self.check = False

	def print(self, *args, **kwargs):
		nl = False
		if not kwargs:
			sys.stdout.write(f"\r{''.join(self.output)}")
		else:
			for key, value in kwargs.items():
				if key == 'msg':
					sys.stdout.write(f"{kwargs.get('msg')}")
				elif key == 'newline' and value == True:
					nl = True
		if nl:
			sys.stdout.write("\n")
		sys.stdout.flush()

	'''
	Loops through every character in the input, randomly
	generating a character based on printable ascii characters
	and if the character generated matches the input or the
	time exceeds one minutes, the program moves on to the next
	character.
	'''
	def run(self, input):
		for i in input:
			self.check = False
			self.time = time.time()
			while time.time() - self.time <= 59:
				char = random.randrange(32, 126, 1)
				self.output.append(chr(char))
				self.print()
				if chr(char) == i:
					self.check = True
					break
				self.output.pop()
				time.sleep(0.05)
			if not self.check:
				self.output.append(i)
			self.print()
		self.print(newline=True)

if __name__ == "__main__":
	try:
		app = Application()
		app.run("Hello World!")
	except KeyboardInterrupt:
		print("\nExitting program...")