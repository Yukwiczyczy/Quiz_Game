from data import question_data
from question_model import Question
from quiz_brain import Quiz
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

def program_execution():
    question_bank = []
    
    for question_row in question_data:
        question_text = question_row['text']
        question_answer = question_row['answer']

        question_to_import = [
            Question(question_text=question_text, 
            question_answer=question_answer)
        ]

        question_bank += question_to_import
    
    new_question = Quiz(question_bank=question_bank)

    while new_question.has_question():
        os.system('cls')
        the_logo()
        print(new_question.show_score())
        print(new_question.show_correct_answer())
        new_question.next_question()

    os.system('cls')
    print(f"Final Score: {new_question.show_score()}")
    

program_execution()