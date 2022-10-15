class Question:
    """ Класс обрабатывает список вопросов и ответов пользователя"""

    def __init__(self, question, difficulty, correct_answer, use=False, user_answer=None):
        """ создает экземпляр с полями:
        self.question - вопрос
        self.difficulty - сложность
        self.correct_answer - верный ответ
        self.use - принимает True если вопрос задан
        self.user_answer - ответ пользователя
        self.points - кол-во очков за верный ответ
        self.answer_bool - принимает True при верном ответе
        """
        self.question = question
        self.difficulty = int(difficulty)
        self.correct_answer = correct_answer
        self.use = use
        self.user_answer = user_answer
        self.points = self.difficulty * 10
        self.answer_bool = False

    def __repr__(self):
        return f'Вопрос: {self.question},\nсложность: {self.difficulty},\nверный ответ: {self.correct_answer},\n' \
               f'использовался ли вопрос: {self.use},\nОтвет пользователя: {self.user_answer}\nОчки'


    def get_answer_bool(self):
        """ Возвращает bool верных ответов """
        return self.answer_bool

    def get_points(self):
        """ Возвращает кол-во очков за верный ответ """
        return self.points

    def is_correct(self, user_answer):
        """ Присваивает ответ пользователя, возвращает bool в зависимости от верности ответа"""
        self.user_answer = user_answer
        return self.user_answer == self.correct_answer

    def build_question(self):
        """ Возвращает строку с вопросом """
        return f'Вопрос: {self.question}\nСложность {self.difficulty}/5'

    def build_positive_feedback(self):
        """Присваивает значение self.use при верном ответе, возвращает строку с баллами за вопрос"""
        self.use = True
        self.answer_bool = True
        return f'Ответ верный, получено {self.points} баллов'

    def build_negative_feedback(self):
        """Возвращает строку с правильным ответом"""
        self.use = True
        return f'Ответ неверный, верный ответ {self.correct_answer}'
