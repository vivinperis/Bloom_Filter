import math

def fnv(word):
    w=word
    fnvprime=1099511628211
    hash=14695981039346656037 # fnv offset basis
    BIG=int(math.pow(2,64))
    #print(str(int(BIG))+"\n")

    for i in range(len(w)):
        charcode = int(ord(word[i]))
        firstoctet = (charcode & 0xFF)
        hash = hash ^ firstoctet
        hash = (hash * fnvprime)
        #hash = int(hash % BIG)
        secondoctet = (charcode >> 8)
        hash = hash ^ secondoctet
        hash = (hash * fnvprime)
        #hash = int(hash % BIG)

    #hash = int(hash % BIG)
    
    return hash

#print (fnv("AnakinSkywalker"))