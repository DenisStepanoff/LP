QUESTION_ANSWER1 = {'Как дела':'Хорошо',
                   'Что делаешь':'Программирую',
                   'Знаешь python':'Ктож его не знает',
                   'Python или bash':'Конечно python'}

QUESTION_ANSWER2 = {'Эй чувак':'Что',
                   'Иди сюда':'Ну что такое',
                   'Семки есть':'Нет',
                   'А закурить':'Аааа... помогитеее...'}

class Dialog:
    
    def __init__(self, answers_dict):
        self.answers_dict = answers_dict

    def ask_user():
        while 1:
            answer = input('Как дела?  ')
            if answer.lower() == 'хорошо':
                break

    def question_answer(self):
        while 1:
            try:
                question = input('Ваш вопрос: ')
                if question.capitalize() in self.answers_dict:
                    print(self.answers_dict[question.capitalize()])
            except KeyboardInterrupt:
                print('\nПока!')
                break
            

dialog = Dialog(QUESTION_ANSWER1)
#dialog = Dialog(QUESTION_ANSWER2)
dialog.question_answer()

