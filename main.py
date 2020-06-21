from BloomFilter import Bitvector,BloomFilter
from ScalableBF import ScalableBF
import Perms
def usernames(a, b):
	ulist = Perms.getPermU(a,b)
	return ulist

def passwords(a, b, p,i):
	plist = Perms.getPermP(a,b,p,i)
	return plist

def main():
	print("\n\tWelcome! Check your username availibilty and password strength here!\n")
	for bftype in range(2):
		if bftype==0 :
			print ("\n\tUsing Counting Bloom Filter\n")
		else:
			print ("\n\tUsing Scalable Bloom Filter\n")
		adduser = True
		usersadded = 0
		while (adduser):
			while True:
				fname = input("Enter First Name : ")
				if len(fname) == 0:
					print("This field is mandatory")
				else:
					break
			while True:
				lname = input("Enter Last Name : ")
				if len(lname) == 0:
					print("This field is mandatory")
				else:
					break
			while True:
				dob = input("Enter DOB (ddmmyyyy) : ")
				if len(dob) != 8:
					print("Please enter DOB in format specified")
				else:
					eight = 8
					for d in dob:
						if not d.isdigit():
							print("Please enter DOB in format specified")
							eight-=1
					if (eight==8):
						break
			taken_users = usernames(fname, lname)
			utl = len(taken_users)
			if usersadded==0 :
				if bftype==0 :
					Bf_U = BloomFilter(utl, 0.25)
				else:
					Bf_U = ScalableBF(0.25)
			for i in taken_users:
				Bf_U.insert(i)

			while True:
				user = input("\nEnter username to check availibilty: ")
				if len(user) == 0:
					print("This field is mandatory")
					continue
				if(Bf_U.query(user.casefold())):
					print("This username is taken")
					continue
				else:
					print("Username available!")
					re_use = input("Would you like to retry username? : ")
					if (re_use.casefold()=="Y".casefold() or re_use.casefold()=="YES".casefold()):
						continue
					Bf_U.insert(i)
					break
			print("\n")
			common_pass = passwords(fname, lname, dob, usersadded)
			pwl = len(common_pass)
			if usersadded==0 :
				if bftype==0 :
					Bf_P = BloomFilter(pwl, 0.25)
				else:
					Bf_P = ScalableBF(0.25)
			for i in common_pass:
				Bf_P.insert(i)
			while True:
				pw = input("\nEnter password and check password strength: ")
				if len(pw) < 6:
					print("Password is too small! Enter at least 6 characters")
					continue
				if(Bf_P.query(pw.casefold())):
					print("Password too common and/or predictable. Retry with another password")
					continue
				low = cap = spcl = dig = 0
				for i in pw:
					if i.isdigit():
						dig = 1
					elif i.isupper():
						cap = 1
					elif i.islower():
						low = 1
					else:
						spcl = 1
				if not (low==1 and cap==1 and spcl==1 and dig==1):
					print("Password is weak! Enter at least 1 digit, uppercase, lowercase and special character")
					continue
				print("\tPassword is strong and acceptable.")
				retry = input("Would you like to retry passwords? ")
				if (retry.casefold()=="Y".casefold() or retry.casefold()=="YES".casefold()):
					continue
				elif(retry.casefold()=="N".casefold() or retry.casefold()=="NO".casefold()):
					Bf_P.insert(pw)
					return
				break
				
			usersadded+=1
			adding = input("Would you like to add another user? ")
			if (adding.casefold()!="Y".casefold() and adding.casefold()!="YES".casefold()):
				break
			elif(retry.casefold()=="N".casefold() or retry.casefold()=="NO".casefold()):
				return
if __name__ == "__main__":
	main()