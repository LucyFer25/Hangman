import pygame
from gallows import Gallows
from letter import Letter
import string


pygame.init()
pygame.font.init()

alphabet = list(string.ascii_uppercase)


class Game:

	def __init__(self):
		self.win_size = (800,500)
		self.fps = 60
		self.window = pygame.display.set_mode(self.win_size)
		self.bg_img = pygame.image.load("imgs/grassland.jpg")
		self.bg_img = pygame.transform.scale(self.bg_img, self.win_size)
		self.mistakes = 0

		# other classes
		self.gallows = Gallows()
		self.letters = [Letter(value) for value in alphabet]

		# words to guess 
		self.word = "WHAT A CHEESE"
		self.password=""
		for letter in self.word:
			if letter.isalpha():
				self.password += "-"
			elif letter.isspace():
				self.password += " "

		self.font = pygame.font.Font('freesansbold.ttf', 40)
		self.font_word = self.font.render(self.password, True, (0,0,0))
		


	def draw(self):
		# drawing background 
		self.window.blit(self.bg_img,(0,0))
		self.gallows.draw(self.window,self.mistakes)

		# if player lost
		if self.mistakes == 7:
			self.letters = []
			font = pygame.font.Font('freesansbold.ttf', 35)
			ending = font.render("YOUR LITTLE FRIEND IS DEAD  :C", True, (0, 0, 0))
			self.window.blit(ending, (20,30))

		# if password isn't complete yet
		elif not self.ifwin():
			#drawing letters to click
			x,y = 20,30
			i = 0
			for letter in self.letters:

				letter.draw(self.window, x, y)
				x += 60
				i += 1
				if i == 13:
					y += 60
					x = 20
			
			# drawing word to guess
			self.font_word = self.font.render(self.password, True, (0,0,0))
			self.window.blit(self.font_word, (400,250))


		# player won
		else:
			self.letters = []
			font = pygame.font.Font('freesansbold.ttf', 35)
			ending = font.render("CONGRATULATION, YOU HAVE SAVED YOUR FRIEND!", True, (0, 0, 0))
			self.window.blit(ending, (20,30))

	def ifwin(self):

		if self.password == self.word:
			return True
		else:
			return False

	def run(self):
		clock = pygame.time.Clock()


		running = True
		while running:
			clock.tick(self.fps)


			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
				if event.type == pygame.MOUSEBUTTONDOWN:
					m_x, m_y = pygame.mouse.get_pos()
					for letter in self.letters:
						if pygame.Rect.collidepoint(letter.rect,m_x,m_y):
							self.password, self.mistakes = letter.check(self.password,self.word,self.mistakes)
							self.letters.remove(letter)

			self.draw()
			pygame.display.update()
			print(self.mistakes)

game = Game()
game.run()
