import time

"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""


def get_time(str):
    return time.ctime()


questions_and_answers = {
    "что делаешь?": computing,
    "давно?": always,
    "сколько времени": get_time
}


def always():
    return 'always'


def computing():
    return 'вычисляю'


def ask_user(answers_dict):
    """
    Замените pass на ваш код
    """
    while True:
        question = input()
        answer = questions_and_answers.get(question)
        if answer is None:
            print("Странный вопрос...")
        else:
            print(answer(question))


if __name__ == "__main__":
    ask_user(questions_and_answers)
