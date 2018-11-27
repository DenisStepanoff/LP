QUESTION_ANSWER = {'Как дела':'Хорошо',
                   'Что делаешь':'Программирую',
                   'Знаешь python':'Ктож его не знает',
                   'Python или bash':'Конечно python'}
class Dialog:
    
    def __init__(self):
        pass

    def ask_user(self):
        while 1:
            answer = input('Как дела?  ')
            if answer.lower() == 'хорошо':
                break

    def question(self):
        self.a = 1

    def question_answer(self, answer_dict):
        #print(Dialog.QUESTION_ANSWER)
        while 1:
            try:
                question = input('Ваш вопрос: ')
                #print(question.capitalize())
                if question.capitalize() in answer_dict:
                    print(answer_dict[question.capitalize()])
            except KeyboardInterrupt:
                print('\nПока!')
                break
            

dialog = Dialog()
#dialog.ask_user()
print(dialog)
dialog.question_answer(QUESTION_ANSWER)
dialog.question()
