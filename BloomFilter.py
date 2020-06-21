import mmh3 as mmh3
import fibo as fibo
import fnv as fnv
import math
class Bitvector:
	def __init__(self, length, initval):
		self.arr = [initval for i in range(0,length)]

class BloomFilter:
	def __init__(self, n,fpr):
		self.curr = 0
		self.max = n
		self.fp_prob = fpr
		self.m = int(self.opt_size())
		self.k = int(self.opt_k())
		self.bit_vector = Bitvector(self.m,0) #Create a bit vector of optimal size

	def opt_size(self):      #Compute optimal size
		m = -(self.max * math.log(self.fp_prob))/((math.log(2))**2) 
		return round(m)

	def opt_k(self): #Compute optimal k value
		k = (self.m/self.max) * math.log(2) 
		return math.ceil(k)
		
	def insert(self,elem):
		for i in range(int(self.k)-2):
			hashv = mmh3.murmur(elem,i) % (self.m//self.k) + i*self.m//self.k
			self.bit_vector.arr[hashv] = self.bit_vector.arr[hashv] + 1
		hashv = (int(fibo.hash(elem))%self.m)
		self.bit_vector.arr[hashv] = self.bit_vector.arr[hashv] + 1
		hashv = (int(fnv.fnv(elem))%self.m)
		self.bit_vector.arr[hashv] = self.bit_vector.arr[hashv] + 1
		self.curr = self.curr + 1

	def query(self,elem):
		for i in range(int(self.k)-2):
			hashv = mmh3.murmur(elem,i) % (self.m//self.k) + i*self.m//self.k
			if self.bit_vector.arr[hashv] == 0:
					return False
		hashv = (int(fibo.hash(elem))%self.m)
		if(self.bit_vector.arr[hashv] == 0):
			return False
		hashv = (int(fnv.fnv(elem))%self.m)
		if(self.bit_vector.arr[hashv] == 0):
			return False
		return True

	def delelem(self,elem):
		if self.curr == 0:
			print("Error : Query unsuccessful, Bloom filter empty")
			return
		for i in range(int(self.k)-2):
			hashv = mmh3.murmur(elem,i) % self.m
			if self.bit_vector.arr[hashv] == 0:
				print(elem,"Not found")
				return
			else:
				self.bit_vector.arr[hashv] = self.bit_vector.arr[hashv] - 1
				self.curr = self.curr - 1
		hashv = (int(fnv.fnv(elem))%self.m)
		if(self.bit_vector.arr[hashv] == 0):
			print(elem,"Not found")
			return
		else:
			self.bit_vector.arr[hashv] = self.bit_vector.arr[hashv] - 1
			self.curr = self.curr - 1
		hashv = (int(fibo.hash(elem))%self.m)
		if(self.bit_vector.arr[hashv] == 0):
			print(elem,"Not found")
			return
		else:
			self.bit_vector.arr[hashv] = self.bit_vector.arr[hashv] - 1
			self.curr = self.curr - 1


def main():

	b = Bitvector(5,0)
	print(b.arr)
	BF = BloomFilter(5000,0.2)
	for i in range(2):
		BF.insert(str(i))
	print("Number of elements inserted is ",BF.curr)
	print(BF.query("1"))
	BF.delelem("1")
	print(BF.query("1"))
	c = 0

if __name__ == "__main__":
	main()
