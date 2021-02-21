"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""


def avg_score_by_class(school_score):
    for clas in school_score:
        n_scores = 0
        sum_scores = 0
        for score in clas['scores']:
            sum_scores += score
            n_scores += 1
        if n_scores > 0:
            print(clas['school_class'], sum_scores/n_scores)
        else:
            print("No scores in ", clas['school_class'])


def avg_school_score(school_scores):
    n_scores = 0
    sum_scores = 0
    for clas in school_scores:
        for score in clas['scores']:
            sum_scores += score
            n_scores += 1
    if n_scores > 0:
        print(sum_scores/n_scores)
    else:
        print('No scores in school')


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    school_scores = [
        {'school_class': '1a',
         'scores': [4, 4, 5, 3, 5, 2]
         },
        {'school_class': '1b',
         'scores': [5, 5, 5, 4, 5, 4]
         },
        {'school_class': '2a',
         'scores': [5, 5, 5, 5, 5, 5]
         },
        {'school_class': '2b',
         'scores': [5, 5, 3, 3, 4, 3]
         },
        {'school_class': '7a',
         'scores': [5, 4, 5, 4, 5, 4]},
        {'school_class': '7b',
         'scores': [4, 3, 4, 3, 4, 3]}
    ]

#    avg_score_by_class(school_scores)
    avg_school_score(school_scores)


if __name__ == "__main__":
    main()
