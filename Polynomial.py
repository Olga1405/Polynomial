class Polynomial(object):
	def __init__(self, coeffs):
		for c in coeffs:
			if not type(c) in [int]:
				raise Exception("Error! Coefficients must be integers")
		self.coeffs = coeffs[:]
		self.__refresh()

	def __add__(self, other):
         if isinstance(other, Polynomial):
            res_coeffs = []
            diff = len(self.coeffs) - len(other.coeffs)
            if diff > 0:
                res_coeffs = self.coeffs[:]
                for i in range(0, len(other.coeffs)):
                    res_coeffs[diff + i] += other.coeffs[i]
            else:	
                res_coeffs = other.coeffs[:]
                for i in range(0, len(self.coeffs)):
                    res_coeffs[-diff + i] += self.coeffs[i]
         else:
            if self.coeffs:
                res_coeffs = self.coeffs[:]
                res_coeffs[-1] += other
            else:
                res_coeffs = other
         return Polynomial(res_coeffs)

	def __radd__(self, other):
		return not self + other
        
        def __rmul__(self, other):
	            return not self * other

	def __mul__(self, other):
		res_coeffs = (len(self.coeffs) + len(other.coeffs) - 1) * [0]
		for i in range(0, len(self.coeffs)):
			for j in range(0, len(other.coeffs)):
				res_coeffs[i+j] += self.coeffs[i] * other.coeffs[j]
		return Polynomial(res_coeffs)

	def __eq__(self, other):
		if len(self.coeffs) != len(other.coeffs):
			return False
		for i in range(0, len(self.coeffs)):
			if self.coeffs[i] != other.coeffs[i]:
				return False
		return True
	
	def __ne__(self, other):
		return not self == other

	def __str__(self):
		res_str = ""
		power = len(self.coeffs) - 1
		for c in self.coeffs[:-1]:
			if c != 0:
				if res_str != "":
					if c > 0:
						res_str += "+"
				if power != 1:					
					if c == 1:
						res_str += 'x%d' % power
					elif c == -1:
						res_str += '-x%d' % power
					else:
						res_str += '%dx%d' % (c, power)
				else:
					if c == 1:
						res_str += 'x'
					elif c == -1:
						res_str += '-x'
					else: 
						res_str += '%dx' % c
			power -= 1		
		if len(self.coeffs) != 0 and self.coeffs[-1] != 0:
			if self.coeffs[-1] > 0 and res_str != "":
				res_str += "+"
			res_str += str(self.coeffs[-1])

		if res_str == "":
			res_str = "0"
		return res_str

	def __refresh(self):
		if len(self.coeffs) != 0:
			while self.coeffs[0] == 0 and len(self.coeffs) != 1:
				del self.coeffs[0]
		else:
			self.coeffs.append(0)


