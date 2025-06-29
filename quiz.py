import random

class Quiz():

	def __init__(self, quiz_file):
		with open(quiz_file, "r") as file:
			self.lines = file.readlines()
		self.number_of_entries = int(len(self.lines) / 6)
		self.random_number = random.randrange(1, self.number_of_entries + 1)
		for line in range(len(self.lines)):
			self.lines[line] = self.lines[line][:-1]
		self.your_answer = ""
		self.correct_answer = ""

	def load_question(self):
		question_number = ((self.random_number - 1) * 6) + 1
		question = self.lines[question_number - 1].replace("Question: ", "")
		print(question)

	def load_answers(self):
		answers = []
		answer_number = ((self.random_number - 1) * 6) + 1
		for i in range(4):
			answer_number += 1
			answer = self.lines[answer_number - 1]
			answers.append(answer)
		for answer in answers:
			print(answer)

	def load_correct_answer(self):
		correct_answer_number = ((self.random_number - 1) * 6) + 6
		self.correct_answer = self.lines[correct_answer_number - 1].replace("Correct answer: ", "")[:1]

	def input_your_answer(self):
		self.your_answer = input("\nWhat is your answer? (a, b, c, or d)\n")

	def check_if_your_answer_is_correct(self, your_answer, correct_answer):
		if self.your_answer == self.correct_answer:
			print("Your answer is correct!")
		else:
			print("Your answer is incorrect!")
			print(f"Correct answer: {self.correct_answer}")

def load_quiz(quiz_file):
	quiz1 = Quiz(quiz_file)