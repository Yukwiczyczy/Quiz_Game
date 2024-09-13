import os

def the_logo():
    print ("""

  _______                              __      _          
 |__   __|                            / _|    | |         
    | |_ __ _   _  ___    ___  _ __  | |_ __ _| |___  ___ 
    | | '__| | | |/ _ \  / _ \| '__| |  _/ _` | / __|/ _ \\
    | | |  | |_| |  __/ | (_) | |    | || (_| | \__ \  __/
    |_|_|   \__,_|\___|  \___/|_|    |_| \__,_|_|___/\___|
                                                          
                                                          
    """)

class Quiz:

    def __init__(self, question_bank) -> None:
        self.question_roll_number = 0
        self.list = question_bank


    def next_question(self):
        score = 0

        for index in range(len(self.list)):
            os.system("cls")
            the_logo()
            print(f"\nScore: {score}")

            current_question = self.list[index]
            self.question_roll_number = index + 1
            answer = input(f"[Question no. {self.question_roll_number}] {current_question.question} (True/False): ")

            # Check the correct answer
            if answer.lower() == current_question.answer.lower():
                score += 1
            else:
                print(f'Correct answer: {current_question.answer.lower()}')