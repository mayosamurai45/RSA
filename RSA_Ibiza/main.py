import random
from math import gcd

def gcdExtended(a, b):
    # Base Case
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = gcdExtended(b % a, a)

    # Update x and y using results of recursive
    # call
    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y


def KibovEuk (a,b,x,y):
    if a==0:
        x=1
        y=0
        return b
    x1=1
    y1=1
    lnko=KibovEuk(b,a%b,x,y)
    x=y1-(b//a)*x1
    y=x1
    return(lnko)


def ModPow(a,e,m):
    result=1
    apow=a
    while e!=0:
        if e and 0x01==0x01:
            result=(result*apow) % m
        e>>=1
        apow=(apow*apow) % m
    return result


def ModInverse(a,m):
    m0=0
    x=1
    y=0
    if m==1:
        return 0
    while (a>1):
        q=a/m
        b=m
        m=a%m
        a=b
        b=y
        y=x-q*y
        x=b
    if x<0:
        x+=m0
    return x


def FermatTeszt(n,k):
    if n<=1 or n==4:
        return False
    if n<=3:
        return True
    while k>0:
        a=random.randrange(2,n-2)
        if a^(n-1)%n!=1 or (a,n)!=1:
            return False
        k=k-1
    return True


def millerRabinTest(n,m):
    a = random.randrange(2, n-2)
    x = pow(a, m, n)
    if x == 1 or x == n-1:
        return True
    while m != n-1:
        x = x * x % n
        m = m * 2
        if x == 1:
            return False
        if x == n-1:
            return True
    return False


def isPrime (n,k):
    if n<=1 or n==4:
        return False
    if n<=3:
        return True
    m=n-1
    while (m%2==0):
        m=m//2
    for i in range(1,k):
        if not millerRabinTest(n,m):
            return False
    return True


def CRT(c, m):
    M = m[0]
    for i in range(1, len(m)):
        M *= m[i]
    x = 0
    for i in range(0, len(c)):
        M_i = M // m[i]
        y_i = gcdExtended(M_i, m[i])[1]
        x += c[i] * M_i * y_i
    x = x % M
    return x


def Enc(m,e,n):
    return pow(m,e,n)


def Dec(c, p, q, d):
    c1 = c % p
    c2 = c % q
    d1 = d % (p-1)
    d2 = d % (q-1)
    cList = [pow(c1, d1, p), pow(c2, d2, q)]
    mList = [p, q]
    return CRT(cList, mList)


def getRandPrimes(bits):
    p=random.getrandbits(bits)
    q=random.getrandbits(bits)
    while not isPrime(q, 10):
        q = random.getrandbits(bits)
    while (not isPrime(p, 10) or p==q):
        p = random.getrandbits(bits)
    return (p,q)



if __name__ == '__main__':

    p,q=getRandPrimes(128)

    n=q*p
    fi=(p-1)*(q-1)
    e = random.randrange(1,fi)
    while gcd(e, fi) != 1:
        e = random.randrange(1, fi)
    d=pow(e,-1,fi)



    m=9
    print (m)
    print(Enc(m,e,n))
    m=Enc(m,e,n)
    print(Dec(m,p,q,d))






                    