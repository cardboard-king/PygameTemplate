
import pygame



class Display:


	def __init__(self,size):

		if size is not None:
			self.canvas = pygame.display.set_mode(size)
		else:
			self.canvas = pygame.display.set_mode()


	def update(self):

		pygame.display.update()


	def get_canvas(self):

		return self.canvas






