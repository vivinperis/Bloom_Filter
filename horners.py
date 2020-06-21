def getKey(word):
	x = 37
	n = len(word)
	#print(n)
	key = ord(word[n-1])
	for i in range(n-1):
		key*=x
		key+=ord(word[n-2-i])	
	
	return key