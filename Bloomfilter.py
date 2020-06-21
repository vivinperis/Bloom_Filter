import mmh3 as mmh3
import math
class Bitarray:
	def __init__(self, length, initval):
		self.arr = [initval for i in range(0,length)]

class BloomFilter:
	def __init__(self, n,fpr):
		self.curr = 0
		self.max = n
		self.fp_prob = fpr
		self.m = int(self.opt_size())
		self.k = int(self.opt_k())
		self.bit_array = Bitarray(self.m,0) #Create a bit array of optimal size

	def opt_size(self):      #Compute optimal size
		m = -(self.max * math.log(self.fp_prob))/((math.log(2))**2) 
		return round(m)

	def opt_k(self): #Compute optimal k value
		k = (self.m/self.max) * math.log(2) 
		return math.ceil(k)
		
	def insert(self,elem):
		for i in range(int(self.k)):
			digest = mmh3.murmur(elem,i) % (self.m//self.k) + i*self.m//self.k
			self.bit_array.arr[digest] = self.bit_array.arr[digest] + 1
		self.curr = self.curr + 1

	def query(self,elem):
		for i in range(self.k):
			digest = mmh3.murmur(elem,i) % (self.m//self.k) + i*self.m//self.k
			if self.bit_array.arr[digest] == 0:
					return False
		return True

	def delete(self,elem):
		if self.curr == 0:
			print("Error : Query unsuccessful, Bloom filter empty")
			return
		for i in range(self.k):
			digest = mmh3.murmur(elem,i) % self.m
			if self.bit_array.arr[digest] == 0:
				print(elem,"Not found")
				return
			else:
				self.bit_array.arr[digest] = self.bit_array.arr[digest] - 1
				self.curr = self.curr - 1

b = Bitarray(5,0)
print(b.arr)
BF = BloomFilter(5000,0.2)
for i in range(5000):
	BF.insert(str(i))
print("Number of elements inserted is ",BF.curr)
c = 0
