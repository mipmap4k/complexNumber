import math

class RationalNum:
    def __init__(self, u=0, d=1):
        if d == 0:
            raise ValueError("Знаменатель не может быть равен нулю")
        if isinstance(u, float) or isinstance(d, float):
            u, d = self._float_to_fraction(u, d)
        self._up = u
        self._down = d
        self.reduction()

    @property
    def up(self):
        return self._up

    @up.setter
    def up(self, value):
        if isinstance(value, float):
            value, self._down = self._float_to_fraction(value, self._down)
        self._up = value
        self.reduction()

    @property
    def down(self):
        return self._down

    @down.setter
    def down(self, value):
        if value == 0:
            raise ValueError("Знаменатель не может быть равен нулю")
        if isinstance(value, float):
            self._up, value = self._float_to_fraction(self._up, value)
        self._down = value
        self.reduction()

    def to_float(self):
        return self._up / self._down

    def _float_to_fraction(self, num, denom=1):
        if isinstance(num, float):
            decimal_places = len(str(num).split('.')[-1])
            denom = 10 ** decimal_places
            num = int(round(num * denom))
        if isinstance(denom, float):
            decimal_places = len(str(denom).split('.')[-1])
            num = int(round(num * (10 ** decimal_places)))
            denom = int(round(denom * (10 ** decimal_places)))
        gcd_val = math.gcd(num, denom)
        return num // gcd_val, denom // gcd_val

    def reduction(self):
        gcd_value = math.gcd(self._up, self._down)
        self._up //= gcd_value
        self._down //= gcd_value
        if self._down < 0:
            self._up = -self._up
            self._down = -self._down
        return self

    def __str__(self):
        return f"{self._up}/{self._down}"

    def __eq__(self, other):
        if isinstance(other, int):
            return self._up == other and self._down == 1
        if not isinstance(other, RationalNum):
            return NotImplemented
        self.reduction()
        other.reduction()
        return self._up == other._up and self._down == other._down

    def __ne__(self, other):
        return not self.__eq__(other)

    def __neg__(self):
        return RationalNum(-self._up, self._down)

    def __add__(self, other):
        if isinstance(other, (int, float)):
            other = RationalNum(other)
        res_down = self._down * other._down
        res_up = self._up * other._down + self._down * other._up
        return RationalNum(res_up, res_down).reduction()

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            other = RationalNum(other)
        res_down = self._down * other._down
        res_up = self._up * other._down - self._down * other._up
        return RationalNum(res_up, res_down).reduction()

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            other = RationalNum(other)
        res_down = self._down * other._down
        res_up = self._up * other._up
        return RationalNum(res_up, res_down).reduction()

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            other = RationalNum(other)
        if other._up == 0:
            raise ZeroDivisionError("Деление на ноль.")
        res_down = self._down * other._up
        res_up = self._up * other._down
        return RationalNum(res_up, res_down).reduction()

    def __pow__(self, n):
        result = RationalNum(self._up, self._down)
        for _ in range(n - 1):
            result *= self
            result.reduction()
        return result

    def __iadd__(self, other):
        return self.__add__(other)

    def __isub__(self, other):
        return self.__sub__(other)

    def __imul__(self, other):
        return self.__mul__(other)

    def __itruediv__(self, other):
        return self.__truediv__(other)