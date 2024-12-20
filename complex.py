from rational import RationalNum
from math import sqrt, atan

class ComplexNum:
    """Класс для представления комплексных чисел"""
    def __init__(self, real=RationalNum(), imaginary=RationalNum()):
        self._real = real
        self._imaginary = imaginary

    @property
    def real(self):
        """Геттер для действительной части"""
        return self._real

    @real.setter
    def real(self, value):
        """Сеттер для действительной части"""
        self._real = RationalNum(value) if isinstance(value, (int, float)) else value

    @property
    def imaginary(self):
        """Геттер для мнимой части"""
        return self._imaginary

    @imaginary.setter
    def imaginary(self, value):
        """Сеттер для мнимой части"""
        self._imaginary = RationalNum(value) if isinstance(value, (int, float)) else value

    def __add__(self, other):
        """Перегрузка оператора сложения"""
        if isinstance(other, (int, float)):
            other = ComplexNum(RationalNum(other))
        new_real = self.real + other.real
        new_imaginary = self.imaginary + other.imaginary
        return ComplexNum(new_real, new_imaginary)

    def __radd__(self, other):
        """Перегрузка оператора сложения с целым или вещественным числом"""
        if isinstance(other, (int, float)):
            return ComplexNum(self.real + RationalNum(other), self.imaginary)
        return NotImplemented

    def __sub__(self, other):
        """Перегрузка оператора вычитания"""
        if isinstance(other, (int, float)):
            other = ComplexNum(RationalNum(other))
        new_real = self.real - other.real
        new_imaginary = self.imaginary - other.imaginary
        return ComplexNum(new_real, new_imaginary)

    def __rsub__(self, other):
        """Перегрузка оператора вычитания с целым или вещественным числом"""
        if isinstance(other, (int, float)):
            return ComplexNum(RationalNum(other) - self.real, -self.imaginary)
        return NotImplemented

    def __mul__(self, other):
        """Перегрузка оператора умножения"""
        if isinstance(other, (int, float)):
            other = ComplexNum(RationalNum(other))
        new_real = self.real * other.real - self.imaginary * other.imaginary
        new_imaginary = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNum(new_real, new_imaginary)

    def __rmul__(self, other):
        """Перегрузка оператора умножения с целым или вещественным числом"""
        if isinstance(other, (int, float)):
            return ComplexNum(self.real * RationalNum(other), self.imaginary * RationalNum(other))
        return NotImplemented

    def __truediv__(self, other):
        """Перегрузка оператора деления"""
        if isinstance(other, (int, float)):
            other = ComplexNum(RationalNum(other))
        denominator = other.real ** 2 + other.imaginary ** 2
        new_real = (self.real * other.real + self.imaginary * other.imaginary) / denominator
        new_imaginary = (other.real * self.imaginary - self.real * other.imaginary) / denominator
        return ComplexNum(new_real, new_imaginary)

    def __rtruediv__(self, other):
        """Перегрузка оператора деления с целым или вещественным числом"""
        if isinstance(other, (int, float)):
            return ComplexNum(self.real / RationalNum(other), self.imaginary / RationalNum(other))
        return NotImplemented

    def __eq__(self, other):
        """Перегрузка оператора равенства"""
        return self.real == other.real and self.imaginary == other.imaginary

    def __ne__(self, other):
        """Перегрузка оператора неравенства"""
        return not self.__eq__(other)

    def __neg__(self):
        """Перегрузка унарного минуса."""
        return ComplexNum(-self.real, -self.imaginary)

    def __pow__(self, n):
        """Перегрузка оператора возведения в степень"""
        if not isinstance(n, int):
            raise ValueError("Степень должна быть целым числом")
        if n < 0:
            raise ValueError("Степень должна быть неотрицательным целым числом")
        if n == 0:
            return ComplexNum(RationalNum(1), RationalNum(0))
        result = ComplexNum(self.real, self.imaginary)
        for _ in range(n - 1):
            result *= self
        return result

    def __str__(self):
        """Строковое представление комплексного числа"""
        return f"{self.real} + {self.imaginary}i"

    def abs(self):
        """Модуль комплексного числа"""
        return sqrt((self.real.to_float()) ** 2 + (self.imaginary.to_float()) ** 2)

    def arg(self):
      """Аргумент комплексного числа"""
      real = self.real.to_float()
      imag = self.imaginary.to_float()
      if real == 0 and imag == 0:
            raise ValueError("Аргумент не определен для нулевого комплексного числа")
      return atan(imag / real)