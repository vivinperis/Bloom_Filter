import mmh3

class BHCBF:
	def __init__(self, n):
		self.BH = [1,4,8,13] #BH sequence
		self.m = 10000 #Size of bloom filter
		self.k = 8 #Number of murmur functions
		self.h = 3 #BH is a valid B3 sequence
		self.l = len(self.BH)
		self.c1 = [0 for i in range(self.m)]  #Fixed increment BF
		self.c2 = [0 for i in range(self.m)] #Variable increment BF
		self.distelem2 = []
		self.distelem3 = []
		self.fpr = self.false_positive_rate(n) 
		self.distinct_sum2 = self.getsums3(self.BH)
		self.distinct_sum3= self.getsums2(self.BH)

	def false_positive_rate(self,n):
		sum=0
		for i in range(self.h+1):
			sum = sum + (self.nCr(n*self.k,i) * (((self.l-1)/(self.l*self.m))**i) * ((1 - 1/self.m)**(n*self.k - i))) 
		#print(sum)
		return pow((1 - sum),self.k)

	def nCr(self,n,r):
		factn=1
		factr=1
		factnr=1  #Factorial of n-r
		for i in range(2,n+1):
			factn=factn*i
			if(i<=r):
				factr=factr*i
			if(i<=(n-r)):
				factnr=factnr*i
		#print(factn)
		#print(factr)
		#print(factnr)
		return (factn//(factr*factnr))

	def getsums2(self,BH):
		arr = [] 
		for i in range(4):
			for j in range(4):
				if (BH[i]+BH[j]) not in arr:
					arr.append(BH[i]+BH[j])
					self.distelem2.append((BH[i],BH[j]))
		return arr

	def getsums3(self,BH):
		arr = [] 
		for i in range(4):
			for j in range(4):
				for k in range(4):
					if (BH[i]+BH[j]+BH[k]) not in arr:
						arr.append(BH[i]+BH[j]+BH[k])
						self.distelem3.append((BH[i],BH[j],BH[k]))
		return arr

	def insert(self,elem):
		for i in range(self.k):
			hashv = (mmh3.murmur(elem,i) % self.m)//self.k + (self.m//self.k)*i
			#print(hashv)
			self.c1[hashv] = self.c1[hashv] + 1
			hashv1 = mmh3.murmur(elem,i) % 4
			self.c2[hashv] = self.c2[hashv] + self.BH[hashv1]

	def query(self,elem):
		for i in range(self.k):
			hashv = (mmh3.murmur(elem,i) % self.m)//self.k + (self.m//self.k)*i
			hashv1 = mmh3.murmur(elem,i) % 4
			if self.c1[hashv] == 0:
				return False
			if self.c1[hashv] >= 4:
				return True
			if self.c1[hashv] == 3:
				t = self.distinct_sum3.index(self.c2[hashv])
				for j in self.dis_elem3[t]:
					if j == self.BH[hashv1]:
						return True
				return False
			if self.c1[hashv] == 1:
				if self.c2[hashv] == self.BH[hashv1]:
					return True
				return False
			if self.c1[hashv] == 2:
				t = self.distinct_sum2.index(self.c2[hashv])
				for j in self.dis_elem2[t]:
					if j == self.BH[hashv1]:
						return True
				return False

	def delelem(self,elem):
		if not self.query(elem):
			return
		for i in range(self.k):
			hashv = mmh3.murmur(elem,i) % self.m//self.k + (self.m//self.k)*i
			self.c1[hashv] = self.c1[hashv] - 1
			hashv1 = mmh3.murmur(elem,i) % 4
			self.c2[hashv] = self.c2[hashv] - self.BH[hashv1]

def main():

	v=BHCBF(100)
	v.insert("Vivin")
	print(v.query("Vivin"))
	for i in range(0,100):
		v.insert(str(i))
		


if __name__ == "__main__":
	main()