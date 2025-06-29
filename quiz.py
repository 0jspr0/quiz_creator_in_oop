import random

class Quiz():

	def __init__(self, quiz_file):
		with open(quiz_file, "r") as file:
			self.lines = file.readlines()