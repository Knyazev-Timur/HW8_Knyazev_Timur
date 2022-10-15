import json
import random
import requests
import basic_questions


def load_questions():
    """ Получает словарь вопросов, преобразует из json и формирует для каждого вопроса класс """

    reponse = requests.get('https://api.jsonbin.it/bins/s6bylVXa')
    return [(basic_questions.Question(items.get('q'), items.get('d'), items.get('a'))) for items in
            json.loads(reponse.text)]


def get_change_question():
    """ получает случайный вопрос из списка полученного load_questions() """
    return random.choice(load_questions())


def get_question(question):
    """ Выводит вопрос при помощи метода build_question() класса Question """
    return question.build_question()


def verify_answer(answer, question):
    """ Передает введенный ответ в метод is_correct() для проверки
    получает bool и выводит результаты, в зависимости от bool """
    if question.is_correct(answer):
        print(question.build_positive_feedback())
        points = question.get_points()
    else:
        print(question.build_negative_feedback())
        points = 0
    return points


def main():
    """ Получает список экземпляров классов, распределяет их в случайном порядке.
    Запускает цикл вопросов. """
    questions = load_questions()
    random.shuffle(questions)
    score = 0
    for question in questions:
        print(get_question(question))
        answer = input()
        score += verify_answer(answer, question)
    get_end(score, questions)


def get_end(score, questions):
    """ Выводит финальный результат """
    correct_answer = [question.get_answer_bool() for question in questions if question.get_answer_bool() is True]
    print(f'Вот и все!\nОтвечено на {len(correct_answer)} вопроса из {len(questions)}\nНабрано баллов: {score}')


if __name__ == '__main__':
    main()
else:
    print('Sorry! This script is not designed for this kind of work!')
