
l = "SATORAREPOTENETOPERAROTAS"

#ef WordSquare(l):
 #   t = len(l)
 #   n = t ** 0.5
 #   print(n)
 #   return n*n == t and len({i for i in l if l.count(i) % 2}) <= n
    
#WordSquare(l)

def WordSquare(L):
    l = len(L)**.5
    s = 0
    for c in set(L):
        print("this is c "+ str(c))
        s += L.count(c)&1
        print("this is s " + str(s))
        print("this is L.count(c) " + str(L.count(c)))
    return s<=l and l//1==l



#def WordSquare(s):
#n = len(s)**.5
#return not n%1 and sum(s.count(l)%2 for l in set(s)) <= n


#ordSquare = lambda W: not (len(W)**.5 % 1 or sum(W.count(c) % 2 for c in set(W)) > len(W)**.5)
