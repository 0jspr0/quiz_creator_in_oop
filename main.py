from quiz import Quiz

def load_quiz(quiz_file):
	quiz1 = Quiz(quiz_file)
	quiz1.load_question()
	quiz1.load_answers()
	correct_answer = quiz1.load_correct_answer()
	your_answer = quiz1.input_your_answer()
	quiz1.check_if_your_answer_is_correct(your_answer, correct_answer)

load_quiz("quiz.txt")