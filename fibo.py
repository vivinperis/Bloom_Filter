import math
import horners

def hash(word):
	k = horners.getKey(word)
	BIG = math.pow(2,64)
	A = (math.sqrt(5)-1)/2
	h = math.floor(BIG*((k*A)%1))
	return h

def main():
	#print(str(math.pow(2,64)))
	num="100"
	hk = hash(num)
	print("H(k)=", int(hk)%10)

#if __name__ == "__main__":
#	main()