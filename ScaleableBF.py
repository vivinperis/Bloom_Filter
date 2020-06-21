import mmh3 as mmh3
import math,time
from Bloomfilter import Bitarray,BloomFilter
class ScalableBF:
	def __init__(self,p):
		self.fp = p
		self.n0 = 1000
		self.SBF = [BloomFilter(self.n0,self.fp/2)]
		self.count = 0

	def insert(self,ele):
		t = int(math.floor(math.log((self.count/self.n0) + 1,2)))
		if t == len(self.SBF):
			self.SBF.append(BloomFilter((2**t)*self.n0,self.fp/(2**(t+1))))
		self.SBF[t].insert(str(ele))
		self.count = self.count + 1

	def query(self,ele):
		for i in range(len(self.SBF)-1 , -1 , -1):
			if self.SBF[i].query(ele):
				print("Present in BF#",i)
			else:
				print("Absent in BF#",i)
			

scaleBF = ScalableBF(0.1)
for i in range(12000):
	scaleBF.insert(str(i))
scaleBF.query("0")