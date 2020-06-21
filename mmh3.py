import math
import horners

def murmur(w, indi):
    word=[]
    word=w
    c1=int(0xcc9e2d51)
    c2=int(0x1b873593)
    m=int(0x5)
    n=int(0xe6546b64)
    l = len(w)
    #print(l)
    seed=1234
    if (indi==0):
        #H = Horner(w)
        seed = horners.getKey(w) % 256
    if (indi==1):
        #H = Horner(w)
        seed = horners.getKey((w[:int(math.ceil(l*0.5))])) % 256

    if (indi==2):
        #H = Horner(w)
        seed = horners.getKey((w[:int(math.ceil(l*0.5))])) % 256

    Hash=seed
    BIG=int(math.pow(2,64))
    
    if len(word)<4:
        leftover=[]
        leftover=word[0:]
        b=16
        k2=0
        for i in range(len(leftover)):
            a=ord(leftover[i].lower())
            a=a<<b
            b-=8
            k2+=a
        #print (k,k2)
        k2*=c1
        k2<<15
        k2*=c2
        Hash=Hash^k2

        Hash=Hash^(len(word))
        #print (Hash)
        Hash ^= (Hash>>16)
        Hash *= int(0x85ebca6b)
        #Hash %= BIG
        Hash ^= (Hash>>13)
        Hash *= int(0xc2b2ae35)
        #Hash %= BIG
        Hash ^= (Hash>>16)
        return (Hash)
    

    if (len(word) >= 4) and (len(word) < 8) :
        word1=[]
        word1=word[:4]
        b=24
        k=0
        for i in range(len(word1)):
            a=ord(word1[i].lower())
            a=(a<<b)
            b-=8
            k=(k+a)
        #print (hex(k))
        k*=c1
        k=k<<15
        k*=c2
        Hash ^= k
        Hash = Hash<<13
        Hash = (Hash*m)+n
        #print (hex(Hash))
        
        leftover=[]
        leftover=word[4:]
        b=16
        k2=0
        for i in range(len(leftover)):
            a=ord(leftover[i].lower())
            a=a<<b
            b-=8
            k2+=a
        #print (k,k2)
        k2*=c1
        k2<<15
        k2*=c2
        Hash ^= k2

        Hash ^= len(word)
        #print (Hash)
        Hash ^= (Hash>>16)
        Hash *= int(0x85ebca6b)
        #Hash %= BIG
        Hash ^= (Hash>>13)
        Hash *= int(0xc2b2ae35)
        #Hash %= BIG
        Hash ^= (Hash>>16)
        return (Hash)
    
     
    if len(word)>=8 and len(word)<12:
        word1=[]
        word1=word[:4]
        b=24
        k=0
        for i in range(len(word1)):
            a=ord(word1[i].lower())
            a=(a<<b)
            b-=8
            k=(k+a)
        #print (hex(k))
        k*=c1
        k=k<<15
        k*=c2
        Hash=Hash^k
        Hash=Hash<<13
        Hash=(Hash*m)+n
        #print (hex(Hash))
        
        word2=[]
        word2=word[4:8]
        b=24
        k3=0
        for i in range(len(word2)):
            a=ord(word2[i].lower())
            a=(a<<b)
            b-=8
            k3=(k3+a)
        #print (hex(k))
        k3*=c1
        k3=k3<<15
        k3*=c2
        Hash=Hash^k3
        Hash=Hash<<13
        Hash=(Hash*m)+n
        
        leftover=[]
        leftover=word[8:]
        b=16
        k2=0
        for i in range(len(leftover)):
            a=ord(leftover[i].lower())
            a=a<<b
            b-=8
            k2+=a
        #print (k,k2)
        k2*=c1
        k2<<15
        k2*=c2
        Hash=Hash^k2

        Hash=Hash^(len(word))
        #print (Hash)
        Hash ^= (Hash>>16)
        Hash *= int(0x85ebca6b)
        #Hash %= BIG
        Hash ^= (Hash>>13)
        Hash *= int(0xc2b2ae35)
        #Hash %= BIG
        Hash ^= (Hash>>16)
        return (Hash)

    if len(word)>=12 and len(word)<16:
        word1=[]
        word1=word[:4]
        b=24
        k=0
        for i in range(len(word1)):
            a=ord(word1[i].lower())
            a=(a<<b)
            b-=8
            k=(k+a)
        #print (hex(k))
        k*=c1
        k=k<<15
        k*=c2
        Hash=Hash^k
        Hash=Hash<<13
        Hash=(Hash*m)+n
        #print (hex(Hash))
        
        word2=[]
        word2=word[4:8]
        b=24
        k3=0
        for i in range(len(word2)):
            a=ord(word2[i].lower())
            a=(a<<b)
            b-=8
            k3=(k3+a)
        #print (hex(k))
        k3*=c1
        k3=k3<<15
        k3*=c2
        Hash=Hash^k3
        Hash=Hash<<13
        Hash=(Hash*m)+n
        
        word3=[]
        word3=word[8:12]
        b=24
        k=0
        for i in range(len(word3)):
            a=ord(word3[i].lower())
            a=(a<<b)
            b-=8
            k=(k+a)
        #print (hex(k))
        k*=c1
        k=k<<15
        k*=c2
        Hash=Hash^k
        Hash=Hash<<13
        Hash=(Hash*m)+n
        
        leftover=[]
        leftover=word[12:]
        b=16
        k2=0
        for i in range(len(leftover)):
            a=ord(leftover[i].lower())
            a=a<<b
            b-=8
            k2+=a
        #print (k,k2)
        k2*=c1
        k2<<15
        k2*=c2
        Hash=Hash^k2

        Hash=Hash^(len(word))
        #print (Hash)
        Hash ^= (Hash>>16)
        Hash *= int(0x85ebca6b)
        #Hash %= BIG
        Hash ^= (Hash>>13)
        Hash *= int(0xc2b2ae35)
        #Hash %= BIG
        Hash ^= (Hash>>16)
        return (Hash)
    
    return 0

#print (murmur("Vivin", 1))