import pygame


class Gallows:
	def __init__(self):
		self.imgs = [pygame.image.load("imgs/gallows"+str(i)+".png") for i in range(8)]
		


	


	def draw(self,win,mistakes):
		self.img = self.imgs[mistakes]
		self.img = pygame.transform.scale(self.img,(250,300))
		win.blit(self.img, (0,200))