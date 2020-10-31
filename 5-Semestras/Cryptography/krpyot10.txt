#Viešas raktas:
V = [33415, 35218, 230274, 69475, 189589, 82664, 73209, 185458]

# Pirma privataus rakto komponentė
W = [1715, 0, 0, 0, 0, 0, 0, 0]

# Modulis:
p = 267835

#šifras:
C = [408176, 603089, 796412, 593634, 713748, 230274, 408176, 796412, 606823, 533614, 593634, 230274, 490840, 450950, 593634, 450950, 408176, 450950]

w1 = W[0]
v1 = V[0]

def getT(vi, wi):
    d = gcd(vi, p)
    ti = (wi/d) / (vi/d) % (p/d)
    res = []
    if d == 1:
        print "d=1"
        return [ti]
    else:
        res.append(ti)
        for i in range(1,d):
            ti = ti + i*(p/d)
            res.append(ti)
        print "d=", d
        return res

res = getT(v1, w1)

print "res=", res

for ti in res:
    W = [elem * ti % p for elem in V]
    print "ti=", ti, "W=", W

# pasirenkame W (ten kur vis greitejanciai dideja skaiciai)
W = [1715, 2048, 4204, 8375, 16744, 33539, 66999, 134078]

t = 96706
# t = 364541

lg = len(C)

CR = []

for i in range(lg):
    #print i
    CR.append(t * C[i] % p)
    
print "CR=", CR


def get_WI(CR):
    WI = [0,0,0,0,0,0,0,0]
    for i in range(7,-1,-1):
        tmp = CR - W[i]
        if tmp >= 0:
            WI[i] = 1
            CR = tmp
    #print CR
    return WI

ATS = []

for j in range(lg):
    ats = get_WI(CR[j])
    ats = ''.join([str(i) for i in ats])
    # print ats
    ATS.append(ats)
    
ATS_integers = [int(i,2) for i in ATS]
ATS = ''.join([chr(i) for i in ATS_integers])
print "Tekstas=", ATS
print "Priv.Raktas=", W