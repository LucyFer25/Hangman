import pygame

pygame.font.init()

class Letter:
	def __init__(self, value):
		self.value = value
		self.img = pygame.image.load("imgs/border.png")
		self.img = pygame.transform.scale(self.img, (50, 50))
		self.font = pygame.font.Font('freesansbold.ttf', 45)
		self.letter = self.font.render(self.value, True, (0,0,0))

		self.guessed = False


		# coretctions 
		self.crox = (50 - self.letter.get_width())/2
		self.croy = (50 - self.letter.get_height())/2


		

	def check(self,password, word, mistakes):
		
		if self.value.upper() in word:
			letters = []
			for letter in password:
				letters.append(letter)

			for i in range(len(word)):
				if self.value.upper() == word[i]:
					print("this letter is in password")
					letters[i] = self.value

			new_password = ""
			for letter in letters:
				new_password += letter

			
			return new_password,mistakes

		else:
			mistakes += 1
			return password, mistakes


		
		



		



				





	def draw(self, win, x, y):
		self.rect = self.img.get_rect(topleft=(x,y))
		win.blit(self.img, (x, y))
		win.blit(self.letter, (x+self.crox, y+self.croy+5))