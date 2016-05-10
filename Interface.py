
from Display import Display
from Artist import Artist
import pygame



DEFAULTMENUPANELCOLOR = (100,100,100)
DEFAULTMENUPANELBORDERCOLOR = (50,50,50)

DEFAULTBUTTONCOLOR = (100,100,100)
DEFAULTBUTTONBORDERCOLOR = (50,50,50)


class MenuPanel(pygame.sprite.Sprite):


	def __init__(self,pos,size):

		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface(size)
		self.image.fill(MENUPANELCOLOR)
		self.rect = pygame.Rect(pos,size)
		borderrect = pygame.Rect((0,0),size)
		pygame.draw.rect(self.image,MENUPANELBORDERCOLOR,borderrect,1)
		self.interactibles = pygame.sprite.Group()


	def click(self,cursor):

		cursor.rect.top -= self.rect.top
		interactible = pygame.sprite.spritecollideany(cursor,self.interactibles)
		if interactible is not None:
			return interactible.click()




class Cursor(pygame.sprite.Sprite):


	def __init__(self):

		pygame.sprite.Sprite.__init__(self)
		self.rect = pygame.Rect(0,0,1,1)


	def move(self,mousex,mousey):

		self.rect.topleft = (mousex,mousey)




class Button(pygame.sprite.Sprite):


	def __init__(self,rect,message):

		pygame.sprite.Sprite.__init__(self)
		self.rect = rect.copy()
		self.image = pygame.Surface(rect.size)
		self.image.fill(DEFAULTBUTTONBORDERCOLOR)
		innerrect = rect.copy()
		innerrect.left = 1
		innerrect.top = 1
		innerrect.height -= 2
		innerrect.width -= 2
		self.image.fill(DEFAULTBUTTONCOLOR,innerrect)
		self.message = message


	def click(self):

		return self.message




class Screen(MenuPanel):


	def __init__(self,pos,size):

		super(Screen,self).__init__(pos,size)
		self.artist = Artist()


	def update(self):

		self.artist.draw(self.image)






class Interface:
	"""
	class for handling all interface elements
	"""


	def __init__(self):
		"""
		init function for components (display,panels,cursor)
		"""

		self.display = Display(None)
		self.canvas = self.display.get_canvas()
		self.menuPanels = pygame.sprite.Group()
		self.populate()
		self.cursor = Cursor()


	def click(self,mousex,mousey):
		"""
		function for chosing what panel is clicked
		"""

		self.cursor.move(mousex,mousey)
		menuPanel = pygame.sprite.spritecollideany(self.cursor,self.menuPanels)
		
		if menuPanel is not None:
			return menuPanel.click(self.cursor)


	def populate(self):
		"""
		init function for adding predefined panels
		"""

		pass



	def update(self,*args,**kwargs):
		"""
		update function for updating panels and drawing
		"""
		pArgs = [] # input args mapped to output args

		self.menuPanels.update(pArgs)
		self.menuPanels.draw(self.canvas)
		self.display.update()


