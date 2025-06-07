# Geometry Lib

расширяемая библиотека для вычисления площади фигур  
(круг, треугольник, + простое добавление своих через наследование).

## Установка

Библиотека — один файл, так что достаточно скачать `geometry_lib.py`  
или установить репозиторий:

```bash
git clone https://github.com/<логин>/geometry-lib-task.git
cd geometry-lib-task
```


## Пример использования
```
from geometry_lib import Circle, Triangle, area

print(area(Circle(5)))          # 78.53981633974483
print(area(Triangle(3, 4, 5)))  # 6.0
print(Triangle(3, 4, 5).is_right())  # True
```

Быстрый запуск примера:
```
python demo.py
```

## Запуск тестов
python geometry_lib.py -v

## Как добавить новую фигуру
Наследуйтесь от Shape, далее реализуйте метод _area() — в нем формула площади.
