import math

class RationalNum:
    def __init__(self, u=0, d=1):
        if d == 0:
            raise ValueError("Знаменатель не может быть равен нулю.")
        if isinstance(u, float) or isinstance(d, float):
            u, d = self._float_to_fraction(u, d)
        self.up = u
        self.down = d
        self.reduction()

    def to_float(self):
        """Преобразует дробь в вещественное число."""
        return self.up / self.down

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
        gcd_value = math.gcd(self.up, self.down)
        self.up //= gcd_value
        self.down //= gcd_value
        if self.down < 0:
            self.up = -self.up
            self.down = -self.down
        return self

    def __str__(self):
        return f"{self.up}/{self.down}"

    def __eq__(self, other):
        if not isinstance(other, RationalNum):
            return NotImplemented
        self.reduction()
        other.reduction()
        return self.up == other.up and self.down == other.down

    def __ne__(self, other):
        return not self.__eq__(other)

    def __neg__(self):
        return RationalNum(-self.up, self.down)

    def __add__(self, other):
        if isinstance(other, (int, float)):
            other = RationalNum(other)
        res_down = self.down * other.down
        res_up = self.up * other.down + self.down * other.up
        return RationalNum(res_up, res_down).reduction()

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            other = RationalNum(other)
        res_down = self.down * other.down
        res_up = self.up * other.down - self.down * other.up
        return RationalNum(res_up, res_down).reduction()

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            other = RationalNum(other)
        res_down = self.down * other.down
        res_up = self.up * other.up
        return RationalNum(res_up, res_down).reduction()

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            other = RationalNum(other)
        res_down = self.down * other.up
        res_up = self.up * other.down
        return RationalNum(res_up, res_down).reduction()

    def __pow__(self, n):
        result = RationalNum(self.up, self.down)
        for _ in range(n - 1):
            result *= self
        return result.reduction()

    def __iadd__(self, other):
        return self.__add__(other)

    def __isub__(self, other):
        return self.__sub__(other)

    def __imul__(self, other):
        return self.__mul__(other)

    def __itruediv__(self, other):
        return self.__truediv__(other)