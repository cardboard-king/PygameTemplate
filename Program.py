
from Interface import Interface
from Engine import Engine
import pygame
import sys




class Program:
	"""
	General program template
	 - init function for program component initialization
	 - main loop
	 	* check events -> handle (event)
	 	* update
	"""

	def __init__(self):
		"""
		init function
		"""

		self.interface = Interface()
		self.engine = Engine()
		self.run()


	def run(self):
		"""
		main loop
		"""

		while True:
			self.check_events()
			self.update()


	def check_events(self):
		"""
		pygame event handling (edit this for more events)
		"""

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				mousex, mousey = event.pos
				response = self.interface.click(mousex,mousey)
				self.handle(response)


	def handle(self,response):
		"""
		handle responses to events
		"""

		self.engine.send(response)
		

	def update(self):
		"""
		update state of program components
		"""

		self.engine.update()
		self.interface.update(self.engine.get_updates())









