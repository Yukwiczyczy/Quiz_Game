from data import question_data
from question_model import Question
from quiz_brain import Quiz

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
    new_question.next_question()



program_execution()