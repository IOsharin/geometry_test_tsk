"""geometry_lib.py
Небольшая расширяемая библиотека геометрии

Публичное API
-------------
>> from geometry_lib import Circle, Triangle, area
>> area(Circle(5))
78.53981633974483
>> tri = Triangle(3, 4, 5)
>> area(tri)
6.0
>> tri.is_right()
True

Чтобы добавить собственную фигуру, наследоваться от `Shape` и реализовать свойметод `_area`.
"""
from __future__ import annotations

import math
from abc import ABC, abstractmethod
from functools import singledispatch
from typing import Any

__all__ = [
    "Shape",
    "Circle",
    "Triangle",
    "area",
]


class Shape(ABC):
    """Абстрактный базовый класс для геометрических фигур"""

    @abstractmethod
    def _area(self) -> float:
        """Возвращает площадь фигуры (переопределяется в наследниках)"""

    def area(self) -> float:
        """Return the area of *self* (preferred: use :pyfunc:`area`)."""
        return self._area()


class Circle(Shape):
    """Окружность, определяемая ее radius"""

    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        self.radius = radius

    def _area(self) -> float:
        return math.pi * self.radius ** 2

    def __repr__(self) -> str:
        return f"Окружность(radius={self.radius})"


class Triangle(Shape):
    """Треугольник, определяемый его сторонами, a,b,c"""

    def __init__(self, a: float, b: float, c: float):
        sides = sorted((a, b, c))
        if any(s <= 0 for s in sides):
            raise ValueError("Длины сторон должны быть положительными")
        if sides[0] + sides[1] <= sides[2]:
            raise ValueError("Нарушено неравенство треугольника")
        self.a, self.b, self.c = sides

    def _area(self) -> float:
        s = (self.a + self.b + self.c) / 2.0 # герон
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    # Дополнительно
    def is_right(self, *, rel_tol: float = 1e-9) -> bool:
        """Возвращает *True*, если треугольник прямоугольный"""
        a2, b2, c2 = (x ** 2 for x in (self.a, self.b, self.c))
        return math.isclose(a2 + b2, c2, rel_tol=rel_tol)

    def __repr__(self) -> str:
        return f"Треугольник(a={self.a}, b={self.b}, c={self.c})"


# ---- public functional interface -----------------------------------------

@singledispatch
def area(obj: Any) -> float:
    """Вернуть площадь объекта obj.

    Если obj является экземпляром `Shape`, вызывается его приватный метод
    `_area`. Для неподдерживаемых типов `TypeError`.
    """
    if isinstance(obj, Shape):
        return obj._area()
    raise TypeError(f"Unsupported type: {type(obj).__name__}")


@area.register
def _(obj: Shape) -> float:  # обработка любых наследников `Shape`
    return obj._area()

# -----------------------------------------------------------------------
# Добавляйте новые фигуры ниже
# ----------------------------------------------------------------------
# Пример:
# class Square(Shape):
#     ... реализуйте _area() ...
#
# ---------------------------------------------------------------------------
# Юнит‑тесты (запускаются командой: `python geometry_lib.py -v`)
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    import unittest

    class TestGeometryLib(unittest.TestCase):
        def test_circle_area(self):
            self.assertAlmostEqual(area(Circle(1)), math.pi)
            self.assertAlmostEqual(area(Circle(2.5)), math.pi * 2.5 ** 2)

        def test_triangle_area(self):
            self.assertAlmostEqual(area(Triangle(3, 4, 5)), 6)
            self.assertAlmostEqual(area(Triangle(7, 8, 9)), 26.8328157, places=6)

        def test_triangle_right(self):
            self.assertTrue(Triangle(3, 4, 5).is_right())
            self.assertFalse(Triangle(5, 5, 5).is_right())

        def test_invalid_inputs(self):
            with self.assertRaises(ValueError):
                Circle(0)
            with self.assertRaises(ValueError):
                Triangle(1, 2, 3)  # нарушает неравенство треугольника

    unittest.main()
