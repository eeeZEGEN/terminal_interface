import sys 
sys.path.insert(0, '/home/roman/worx/python_worx/interface/env/lib64/python3.11/site-packages')
import keyboard as kb
import time as tm
import threading
import os

class Interface:
	'''
	Interface class
	'''
	def __init__(self, size: tuple = (30, 30), alignment: str = 'center', cursor_coordinates: tuple = (0, 0)):
		# Init size
		self._size = size
		self._width, self._height = size[0], size[1]

		# Init alignment
		self._alignment = alignment

		# Init cursor
		self.initCursor(cursor_coordinates)

		# Init view of interface
		self._skeleton = [f'+{self._width * "--"}+']
		battle_field = []
		for i in range(self._height):
			if i != self._cursor_y:
				battle_field.append(f'|{self._width * "  "}|')
			elif i == 0:
				battle_field.append(f'|{(self._cursor_x) * "  "}{self._cursor}{(self._width - self._cursor_x - 1) * "  "}|')
			else:
				battle_field.append(f'|{(self._cursor_x - 1) * "  "}{self._cursor}{(self._width - self._cursor_x) * "  "}|')

		self._skeleton += battle_field + self._skeleton
		self._view = '\n'.join(self._skeleton)

	
	def initCursor(self, cursor_coordinates: tuple = (0, 0)) -> None:
		# Init cursor
		self._cursor = '□□'
		self._cursor_x = cursor_coordinates[0]
		self._cursor_y = cursor_coordinates[1]
		self._cursor_coordinates = (self._cursor_x, self._cursor_y)


	def setCursorCoordinates(self, coordinates: tuple) -> None:
		# Update cursor coordinates
		self.__init__(size=self._size, alignment=self._alignment, cursor_coordinates=coordinates)


	def setSize(self, size: tuple) -> None:
		# Update size
		self.__init__(size=size, alignment=self._alignment, cursor_coordinates=self._cursor_coordinates)


	def setAlignment(self, alignment) -> None:
		# Update alignment
		self.__init__(size=self._size, alignment=alignment, cursor_coordinates=self._cursor_coordinates)


	def updateInterface(self):
		# Clear terminal
		self.__init__(size=self._size, alignment=self._alignment, cursor_coordinates=self._cursor_coordinates)
		os.system('clear')
		print(self._view)


	def loop(self):

		os.system('clear')
		print(self._view)

		while True:

			#Triggers for bindings W,A,S,D
			if kb.is_pressed('s'):
				print('YOU')
				self.initCursor((self._cursor_x, self._cursor_y + 1))
				self.updateInterface()
				tm.sleep(0.1)

			if kb.is_pressed('w'):
				print('YOU')
				self.initCursor((self._cursor_x, self._cursor_y - 1))
				self.updateInterface()
				tm.sleep(0.1)

			if kb.is_pressed('a'):
				print('YOU')
				self.initCursor((self._cursor_x - 1, self._cursor_y))
				self.updateInterface()
				tm.sleep(0.1)

			if kb.is_pressed('d'):
				print('YOU')
				self.initCursor((self._cursor_x + 1, self._cursor_y))
				self.updateInterface()
				tm.sleep(0.1)

