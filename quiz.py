import random

class Quiz():

	def __init__(self, quiz_file):
		with open(quiz_file, "r") as file:
			self.lines = file.readlines()
		self.number_of_entries = int(len(self.lines) / 6)
		self.random_number = random.randrange(1, self.number_of_entries + 1)