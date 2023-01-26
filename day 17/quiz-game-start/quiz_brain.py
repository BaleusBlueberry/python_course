class Quiz:
    def __init__(self, question_list):
        self.question_number = 0
        self.currect_answers = 0
        self.question_list = question_list

    def still_have_question(self):
        if self.question_number == len(self.question_list):
            return False
        else:
            return True

    def next_question(self):
        current_qestion = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} {current_qestion.text} (True/False):")
        self.check_answer(user_answer, current_qestion.answer)


    def check_answer(self, user_answer, correct_answer):

        if user_answer.lower() == correct_answer.lower():
            print("Tou got it right")
            self.currect_answers += 1
        else:
            print("Tjat's wrong.")
        print(f"The correct answer is: {correct_answer}")
        print(f"Your current score is: {self.currect_answers}/{self.question_number}")
        print("\n")
