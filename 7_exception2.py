"""

Домашнее задание №1

Исключения: приведение типов

* Перепишите функцию discounted(price, discount, max_discount=20)
  из урока про функции так, чтобы она перехватывала исключения,
  когда переданы некорректные аргументы.
* Первые два нужно приводить к вещественному числу при помощи float(),
  а третий - к целому при помощи int() и перехватывать исключения
  ValueError и TypeError, если приведение типов не сработало.
    
"""

def discounted(price, discount, max_discount=20):
    """
    Замените pass на ваш код
    """
    try:
      price_ = abs(float(price))
    except (TypeError, ValueError):
      print(price, "Неправильное значение price")
      return
    try:  
      discount_ = abs(float(discount))
    except (TypeError, ValueError):
      print(discount, "Неправильное значение discount")
      return
    try:
      max_discount_ = abs(int(max_discount))
    except (TypeError, ValueError):
      print(max_discount, "Неправильное значение max_discount")
      return
    if max_discount_ > 99:
      raise ValueError('Слишком большая максимальная скидка')
    if discount_ >= max_discount_:
      return price_
    else:
      return price_ - (price_ * discount_ / 100)

      
    
if __name__ == "__main__":
    print(discounted(100, 2))
    print(discounted(100, "3"))
    print(discounted("100", "4.5"))
    print(discounted("five", 5))
    print(discounted("сто", "десять"))
    print(discounted(100.0, 5, "10"))
