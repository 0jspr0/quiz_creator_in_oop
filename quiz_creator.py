class QuizCreator():

    def create_quiz(self):
        while True:
            question = input("Enter a question:\n")

            answers = {}
            for option in ['a', 'b', 'c', 'd']:
                answer = input(f"Enter answer option {option}:\n")
                answers[option] = answer

            correct_answer = input("Enter the correct answer (a, b, c, or d):\n")

            with open("quiz.txt", "a") as file:
                file.write(f"Question: {question}\n")
                for option, answer in answers.items():
                    file.write(f"{option}. {answer}\n")

            add_another_question_choice = input("Do you want to add another question? (yes/no):\n").strip().lower()
            if add_another_question_choice != "yes":
                break

quiz_creator1 = QuizCreator()
quiz_creator1.create_quiz()