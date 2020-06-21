#from itertools import permutations

#def main():

def getPermU(fn, ln):
	fperm = []
	lperm = []
	perms = []
	for i in range(len(fn)):
		fperm.append((fn[:(i+1)]).casefold())
	for j in range(len(ln)):
		lperm.append((ln[:(j+1)]).casefold())
	perms = fperm + lperm
	for i in fperm:
		for j in lperm:
			for k in range(11):
				perms.append(i+j)
				perms.append(j+i)
				perms.append(i+j+str(k))
				perms.append(j+i+str(k))
				perms.append(i+str(k))
				perms.append(str(k)+i)
				perms.append(j+str(k))
				perms.append(str(k)+j)
				perms.append(i+str(k)+j)
				perms.append(j+str(k)+i)

	#chars = [char for char in ip]
	#for j in range(10):
		#chars.append(str(j))

	#for i in range(1, len(chars)+1):
	#	for c in permutations(chars, i):
	#		perms.append("".join(c))
	return perms
	#print (len(perms))


def getPermP(fn, ln, dob, ite):
	fperm = []
	lperm = []
	pwperm = []
	perms = []
	for i in range(len(fn)):
		fperm.append((fn[:(i+1)]).casefold())
	for j in range(len(ln)):
		lperm.append((ln[:(j+1)]).casefold())
	perms = fperm + lperm
	pwperm.append(dob[:2])
	pwperm.append(dob[:4])
	pwperm.append(dob[2:4])
	pwperm.append(dob[1:2])
	pwperm.append(dob[3:4])
	pwperm.append(dob[6:])
	pwperm.append(dob[4:])
	pwperm.append(dob)

	for i in fperm:
		for j in lperm:
			for k in pwperm:
				perms.append(i+j)
				perms.append(j+i)
				perms.append(i+j+k)
				perms.append(j+i+k)
				perms.append(i+k+j)
				perms.append(j+k+i)

	if ite==0 :
		with open("common_passwords.txt") as dict:
			dict1 = dict.read().split('\n')

		for i in range(len(dict1)):
			a = []
			a = dict1[i]
			if len(a)!=0 :
				perms.append(a)

	return perms


#main()

#nodupe = set(perms)

#print(nodupe[1])
#print(perms)