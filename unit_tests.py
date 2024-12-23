import unittest
from rational import RationalNum
from complex import ComplexNum
import math

class TestRationalNum(unittest.TestCase):

    def test_init(self):
        r = RationalNum(1, 2)
        self.assertEqual(r.up, 1)
        self.assertEqual(r.down, 2)

    def test_init_float(self):
        r = RationalNum(0.5)
        self.assertEqual(r.up, 1)
        self.assertEqual(r.down, 2)

    def test_to_float(self):
        r = RationalNum(1, 2)
        self.assertEqual(r.to_float(), 0.5)

    def test_reduction(self):
        r = RationalNum(2, 4)
        r.reduction()
        self.assertEqual(r.up, 1)
        self.assertEqual(r.down, 2)

    def test_add(self):
        r1 = RationalNum(1, 2)
        r2 = RationalNum(1, 3)
        result = r1 + r2
        self.assertEqual(result.up, 5)
        self.assertEqual(result.down, 6)

    def test_sub(self):
        r1 = RationalNum(1, 2)
        r2 = RationalNum(1, 3)
        result = r1 - r2
        self.assertEqual(result.up, 1)
        self.assertEqual(result.down, 6)
				
    def test_truediv(self):
        r1 = RationalNum(1, 2)
        r2 = RationalNum(1, 3)
        result = r1 / r2
        self.assertEqual(result.up, 3)
        self.assertEqual(result.down, 2)

    def test_eq(self):
        r1 = RationalNum(1, 2)
        r2 = RationalNum(1, 2)
        self.assertEqual(r1, r2)

    def test_ne(self):
        r1 = RationalNum(1, 2)
        r2 = RationalNum(1, 3)
        self.assertNotEqual(r1, r2)

    def test_neg(self):
        r = RationalNum(1, 2)
        result = -r
        self.assertEqual(result.up, -1)
        self.assertEqual(result.down, 2)

    def test_exception_zero_denominator(self):
        with self.assertRaises(ValueError):
            RationalNum(1, 0)
    
    def test_assignment_up(self):
        """Тест присваивания числителя"""
        r = RationalNum(2, 2)
        r.up = 3
        self.assertEqual(r.up, 3)
        self.assertEqual(r.down, 1)

    def test_assignment_down(self):
        """Тест присваивания знаменателя"""
        r = RationalNum(2, 4)
        r.down = 6
        self.assertEqual(r.up, 1)
        self.assertEqual(r.down, 6)

    def test_assignment_zero_denominator(self):
        """Тест присваивания нулевого знаменателя"""
        r = RationalNum(2, 4)
        with self.assertRaises(ValueError):
            r.down = 0 

    # Тесты с большими значениями
    def test_large_values(self):
        r1 = RationalNum(123456789, 987654321)
        r2 = RationalNum(987654321, 123456789)
        result = r1 * r2
        self.assertEqual(result.up, 1)
        self.assertEqual(result.down, 1)

    def test_reduction_large_values(self):
        r = RationalNum(123456789 * 2, 123456789 * 3)
        r.reduction()
        self.assertEqual(r.up, 2)
        self.assertEqual(r.down, 3)

class TestComplexNum(unittest.TestCase):

    def test_init(self):
        c = ComplexNum(RationalNum(1, 2), RationalNum(3, 4))
        self.assertEqual(c.real, RationalNum(1, 2))
        self.assertEqual(c.imaginary, RationalNum(3, 4))

    def test_real_setter(self):
        c = ComplexNum()
        c.real = 5
        self.assertEqual(c.real, RationalNum(5))
        c.real = 5.8
        self.assertEqual(c.real, RationalNum(5.8))

    def test_imaginary_setter(self):
        c = ComplexNum()
        c.imaginary = 7
        self.assertEqual(c.imaginary, RationalNum(7))

    def test_add(self):
        c1 = ComplexNum(RationalNum(1, 2), RationalNum(3, 4))
        c2 = ComplexNum(RationalNum(2, 3), RationalNum(5, 6))
        result = c1 + c2
        self.assertEqual(result.real, RationalNum(7, 6))
        self.assertEqual(result.imaginary, RationalNum(19, 12))

    def test_radd(self):
        c = ComplexNum(RationalNum(1, 2), RationalNum(3, 4))
        result = 5 + c
        self.assertEqual(result.real, RationalNum(11, 2))
        self.assertEqual(result.imaginary, RationalNum(3, 4))

    def test_sub(self):
        c1 = ComplexNum(RationalNum(1, 2), RationalNum(3, 4))
        c2 = ComplexNum(RationalNum(2, 3), RationalNum(5, 6))
        result = c1 - c2
        self.assertEqual(result.real, RationalNum(-1, 6))
        self.assertEqual(result.imaginary, RationalNum(-1, 12))

    def test_rmul(self):
        c = ComplexNum(RationalNum(1, 2), RationalNum(3, 4))
        result = 5 * c
        self.assertEqual(result.real, RationalNum(5, 2))
        self.assertEqual(result.imaginary, RationalNum(15, 4))

    def test_truediv(self):
        c1 = ComplexNum(RationalNum(1, 2), RationalNum(3, 4))
        c2 = ComplexNum(RationalNum(2, 3), RationalNum(5, 6))
        result = c1 / c2
        denominator = RationalNum(4, 9) + RationalNum(25, 36)
        real_part = (RationalNum(1, 2) * RationalNum(2, 3) + RationalNum(3, 4) * RationalNum(5, 6)) / denominator
        imag_part = (RationalNum(2, 3) * RationalNum(3, 4) - RationalNum(1, 2) * RationalNum(5, 6)) / denominator
        self.assertEqual(result.real, real_part)
        self.assertEqual(result.imaginary, imag_part)

    def test_eq(self):
        c1 = ComplexNum(RationalNum(1, 2), RationalNum(3, 4))
        c2 = ComplexNum(RationalNum(1, 2), RationalNum(3, 4))
        self.assertEqual(c1, c2)

    def test_ne(self):
        c1 = ComplexNum(RationalNum(1, 2), RationalNum(3, 4))
        c2 = ComplexNum(RationalNum(2, 3), RationalNum(5, 6))
        self.assertNotEqual(c1, c2)

    def test_neg(self):
        c = ComplexNum(RationalNum(1, 2), RationalNum(3, 4))
        result = -c
        self.assertEqual(result.real, RationalNum(-1, 2))
        self.assertEqual(result.imaginary, RationalNum(-3, 4))

    def test_pow(self):
        c = ComplexNum(RationalNum(1, 2), RationalNum(3, 4))
        result = c ** 2
        self.assertEqual(result.real, RationalNum(-5, 16))
        self.assertEqual(result.imaginary, RationalNum(3, 4))

    def test_abs(self):
        c = ComplexNum(RationalNum(3), RationalNum(4))
        self.assertEqual(c.abs(), 5.0)

    def test_arg(self):
        c = ComplexNum(RationalNum(1), RationalNum(1))
        self.assertAlmostEqual(c.arg(), 0.7853981633974483, places=6)

    def test_add_int(self):
        c = ComplexNum(RationalNum(1), RationalNum(2))
        result = c + 3
        self.assertEqual(result.real, RationalNum(4))
        self.assertEqual(result.imaginary, RationalNum(2))

    def test_radd_float(self):
        c = ComplexNum(RationalNum(1), RationalNum(2))
        result = 3.5 + c
        self.assertEqual(result.real, RationalNum(4.5))
        self.assertEqual(result.imaginary, RationalNum(2))

    def test_sub_float(self):
        c = ComplexNum(RationalNum(1), RationalNum(2))
        result = c - 0.5
        self.assertEqual(result.real, RationalNum(0.5))
        self.assertEqual(result.imaginary, RationalNum(2))

    def test_mul_zero(self):
        c = ComplexNum(RationalNum(1), RationalNum(2))
        result = c * 0
        self.assertEqual(result.real, RationalNum(0))
        self.assertEqual(result.imaginary, RationalNum(0))

    def test_truediv_int(self):
        c = ComplexNum(RationalNum(2), RationalNum(4))
        result = c / 2
        self.assertEqual(result.real, RationalNum(1))
        self.assertEqual(result.imaginary, RationalNum(2))

    def test_pow_zero(self):
        c = ComplexNum(RationalNum(1), RationalNum(2))
        result = c ** 0
        self.assertEqual(result.real, RationalNum(1))
        self.assertEqual(result.imaginary, RationalNum(0))
    
    def test_assignment_real(self):
        c = ComplexNum(1, 2)
        c.real = 3
        self.assertEqual(c.real, 3)
        self.assertEqual(c.imaginary, 2)

    def test_assignment_imaginary(self):
        c = ComplexNum(1, 2)
        c.imaginary = 4
        self.assertEqual(c.real, 1)
        self.assertEqual(c.imaginary, 4)

    def test_assignment_invalid_real(self):
        c = ComplexNum(1, 2)
        with self.assertRaises(TypeError):
            c.real = "invalid"  

    def test_assignment_invalid_imaginary(self):
        c = ComplexNum(1, 2)
        with self.assertRaises(TypeError):
            c.imaginary = "invalid" 

    # Тесты с большими значениями
    def test_large_values(self):
        c1 = ComplexNum(RationalNum(123456, 654321), RationalNum(654321, 123456))
        c2 = 2 
        result = c1 * c2
        self.assertEqual(result.real.up, 82304)
        self.assertEqual(result.real.down, 218107)
        self.assertEqual(result.imaginary.up, 218107)
        self.assertEqual(result.imaginary.down, 20576)

    def test_reduction_large_values(self):
        c = ComplexNum(RationalNum(123456789 * 2, 123456789 * 3), RationalNum(123456789 * 4, 123456789 * 5))
        c.real.reduction()
        c.imaginary.reduction()
        self.assertEqual(c.real.up, 2)
        self.assertEqual(c.real.down, 3)
        self.assertEqual(c.imaginary.up, 4)
        self.assertEqual(c.imaginary.down, 5)

if __name__ == '__main__':
    unittest.main()