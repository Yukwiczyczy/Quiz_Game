class Quiz:

    def __init__(self, question_bank) -> None:
        self.question_roll_number = 0
        self.list = question_bank
        self.score = 0
        self.current_question = ""
        self.correct_answer = ""

    def has_question(self):
        return self.question_roll_number < len(self.list)


    def next_question(self):
        current_question = self.list[self.question_roll_number]
        self.question_roll_number += 1
        answer = input(f"[Question no. {self.question_roll_number}] {current_question.question}: (True/False): ")
        self.current_question = f"[Question no. {self.question_roll_number}] {current_question.question}:"
        self.check_answer(answer, current_question.answer)


    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            self.score += 1
            self.correct_answer = ""
        else:
            self.correct_answer = correct_answer


    def show_score(self):
        return f"Score: {self.score}"
    

    def show_correct_answer(self):
        if not self.correct_answer == "":
            return f"{self.current_question} {self.correct_answer}"
        else:
            return ""