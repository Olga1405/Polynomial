import unittest
from Polynomial import Polynomial

class PolynomialTest(unittest.TestCase):
	def test_str_null(self):
		self.assertEqual(str(Polynomial([0, 0, 0, 0])), '0')

	def test_str_first_(self):
		self.assertEqual(str(Polynomial([0, 2])), '2')

	def test_str_any_positive_numbers_poly(self):
		self.assertEqual(str(Polynomial([4,3,2,1])), '4x3+3x2+2x+1')
        
	def test_add_zero(self): 
		self.assertEqual(Polynomial([-4,3,-2,1]), Polynomial([-4,3,-2,1]) + Polynomial([0]))

        def test_add_const(self): 
	    self.assertEqual(Polynomial([-4,3,-2,3]), Polynomial([-4,3,-2,1]) + 2)

        def test_mult_const(self): 
	    self.assertEqual(Polynomial([-4,3,-2,1]), Polynomial([-4,3,-2,1]) * 1)

	def test_add_number(self):
		self.assertEqual(Polynomial([4,3,2,2]), Polynomial([4,3,2,1]) + Polynomial([1]))

	def test_add_negative_number(self):
		self.assertEqual(Polynomial([-4,3,-2,0]), Polynomial([-4,3,-2,1]) + Polynomial([-1]))

	def test_add_polynom_same_size(self):
		self.assertEqual(Polynomial([-8,6,-4,0]), Polynomial([-4,3,-2,0]) + Polynomial([-4,3,-2,0]))

	def test_add_polynom_less_size(self):
		self.assertEqual(Polynomial([-1,2,-2,-5]), Polynomial([-1,3,-5,0]) + Polynomial([-1,3,-5]))

	def test_add_polynom_bigger_size(self):
		self.assertEqual(Polynomial([-1,2,-2,-5]), Polynomial([-1,3,-5]) + Polynomial([-1,3,-5,0]))

	def test_mul_zero(self):
		self.assertEqual(Polynomial([0]), Polynomial([-1,3,-5,0]) * Polynomial([0]))

	def test_mul_positive_number(self):
		self.assertEqual(Polynomial([-2,6,-10,2]), Polynomial([-1,3,-5,1]) * Polynomial([2]))

	def test_mul_negative_number(self):
		self.assertEqual(Polynomial([2,-6,10,-2]), Polynomial([-1,3,-5,1]) * Polynomial([-2]))
	
	def test_mul_polynoms(self):
		self.assertEqual(Polynomial([-2,3,-1,-13,3]), Polynomial([-1,3,-5,1]) * Polynomial([2,3]))

if __name__ == '__main__':
    unittest.main()