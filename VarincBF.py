import mmh3
class varincBF:
	def __init__(self, n):
		self.BH = [1,4,8,13] #BH sequence
		self.m = 10000 #Size of bloom filter
		self.k = 10 #Number of murmur functions
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
		print(sum)
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
		arr = [0 for i in range(0,27)] #since max sum two at a time can be 13*2=26
		for i in range(4):
			for j in range(4):
				if arr[BH[i]+BH[j]]:
					arr[BH[i]+BH[j]]=1
					self.distelem2.append((BH[i],BH[j]))
		return arr

	def getsums3(self,BH):
		arr = [0 for i in range(0,40)] #since max sum three at a time can be 13*3=39
		for i in range(4):
			for j in range(4):
				for k in range(4):
					if arr[(BH[i]+BH[j]+BH[k])]:
						arr[BH[i]+BH[j]+BH[k]]=1
						self.distelem3.append((BH[i],BH[j],BH[k]))
		return arr

	def insert(self,elem):
		for i in range(self.k):
			digest = mmh3.murmur(elem,i) % self.m//self.k + (self.m//self.k)*i
			print(digest)
			self.c1[digest] = self.c1[digest] + 1
			digest1 = mmh3.murmur(elem,i) % 4
			self.c2[digest] = self.c2[digest] + self.BH[digest1]

	def query(self,elem):
		for i in range(self.k):
			digest = mmh3.murmur(elem,i) % self.m//self.k + (self.m//self.k)*i
			digest1 = mmh3.murmur(elem,i) % 4
			if self.c1[digest] == 0:
				return False
			if self.c1[digest] >= 4:
				return True
			if self.c1[digest] == 3:
				t = self.distinct_sum3.index(self.c2[digest])
				for j in self.dis_elem3[t]:
					if j == self.BH[digest1]:
						return True
				return False
			if self.c1[digest] == 1:
				if self.c2[digest] == self.BH[digest1]:
					return True
				return False
			if self.c1[digest] == 2:
				t = self.distinct_sum2.index(self.c2[digest])
				for j in self.dis_elem2[t]:
					if j == self.BH[digest1]:
						return True
				return False

	def delelem(self,elem):
		if not self.query(elem):
			return
		for i in range(self.k):
			digest = mmh3.murmur(elem,i) % self.m//self.k + (self.m//self.k)*i
			self.c1[digest] = self.c1[digest] - 1
			digest1 = mmh3.murmur(elem,i) % 4
			self.c2[digest] = self.c2[digest] - self.BH[digest1]

v=varincBF(100)
print(v.false_positive_rate(0))
v.nCr(6,2)
v.insert("Vivin")
print(v.query("Vivin"))