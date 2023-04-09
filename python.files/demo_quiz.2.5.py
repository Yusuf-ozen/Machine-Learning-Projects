# Question

class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer


    def check_answer(self, answer):
        return self.answer == answer            # Burada self'te belirlediğimiz answer diğer answere eşit ise döndürür.






# Quiz

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.question_index = 0             # Buradaki index değerini bir yazarsak 2.soru karşımıza çıkar.



    def get_question(self):
        return self.questions[self.question_index] 



    def display_question(self):
        question = self.get_question()
        print(f"Soru {self.question_index + 1} : {question.text}")



        for q in question.choices:
            print('-'+ q)

        answer = input('Enter your answer : ')
        self.guess(answer)
        self.load_question

        print(question.check_answer(answer))



    def guess(self, answer):
        question = self.get_question()

        if question.check_answer(answer):
            self.score += 1
        self.question_index += 1

        # self.display_question()


    def load_question(self):
        if len(self.questions) == (self.question_index):
            self.show_score


        else:
            self.display_question()


    def show_score(self):
        pass






q1 = Question('En iyi programlama dili hangisidir? ', ['C#', 'python', 'javascript', 'Matlab'], 'python')        # Burada 2.kısımda şıkları belirledik. 3.kısımda cevabı belirledik.
q2 = Question('En popüler programlama dili hangisidir? ', ['C#', 'python', 'javascript', 'Matlab'], 'C#')
q3 = Question('En hızlı programlama dili hangisidir? ', ['C#', 'python', 'javascript', 'Matlab'], 'Matlab')

questions = [q1, q2, q3]


quiz = Quiz(questions)              # questionları quiz'e atadık.
# question = quiz.questions[quiz.question_index]           # Burada köşeli parantez kullanılmalıdır.

quiz.display_question()

# question = quiz.get_question()
# print(question.text)






# print(q1.check_answer('python'))        # Burada answer için 'python' cevabını verdiğimiz için 'true' cevabını aldık.
# print(q2.check_answer('C#'))
# print(q3.check_answer('Matlab'))





