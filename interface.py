from  keyboard import *

class Interface:
	'''
	Interface class
	'''
	def __init__(self, size: tuple=(30, 30), alignment: str='center'):
		# Init size
		self._size = size
		self._width, self._height = size[0], size[1]

		# Init alignment
		self._alignment = alignment

		# Init view of interface
		self._skeleton = [f'+{self._width * "--"}+']
		self._skeleton += self._height * [f'|{self._width * "  "}|'] + self._skeleton
		self._view = '\n'.join(self._skeleton)

