class QuizBrain:


    def __init__(self, ques_list):
        self.question_number = 0
        self.question_list = ques_list
        self.score = 0


    def next_question(self):
        current_question = self.question_list[self.question_number]
        answer = input(f"Q.{self.question_number + 1}: {current_question.Text} (true/false): ")
        self.answer_analysis(answer, current_question.Answer)
        self.question_number += 1

    def is_empty(self):
        if(self.question_number >= len(self.question_list)):
            return True
        else:
            return False


    def answer_analysis(self, answer,correct_answer):
        if answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"well played, your score is {self.score}/{len(self.question_list)}")

        else:
            print(f"stupid, the answer is {correct_answer} your score is {self.score}/{len(self.question_list)}")
