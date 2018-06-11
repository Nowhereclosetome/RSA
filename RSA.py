import random
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def generatePrimeArr(start, stop):
    if start >= stop:
        return []
    primes = [2]
    for n in range(3, stop + 1, 2):
        for i in primes:
            if n % i == 0:
                break
            else:
                primes.append(n)
    while primes[0] < start:
        del primes[0]
    return primes

def arePrimeRelatively(a, b):
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            return False
    return True

def generatePair(length):#length - length of binary push to make n-interval
    # minN must be different from maxN for 2 bits
    minN = 1 << (length - 1)
    maxN = 1 << (length + 1)
    interval_start = 1 << (length // 2 - 1)
    interval_stop = 1 << (length // 2 + 1)
    primeArr = generatePrimeArr(interval_start, interval_stop)

    while primeArr:
        p = random.choice(primeArr)
        primeArr.remove(p)
        varients_of_q = [q for q in primeArr
                        if (p * q >= minN) and (p * q <= maxN)]
        if varients_of_q: #take from varients of q and break the loop
            q = random.choice(varients_of_q)
            break
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 0
    for i in range(3, phi, 2):
        if arePrimeRelatively(i, phi):
            e = i
            break

    d = 0
    for i in range(3, phi, 2):
        if i * e % phi == 1: 
            d = i
            break
    return [[n,e],[n,d]]

def encrypt(x, n, e):
    return pow(x, e, n)

def decrypt(y, n, d):
    return pow(y, d, n)

Keys = generatePair(4)
PublicKey, PrivateKey = Keys[0],Keys[1]
print(Keys)
print(PublicKey)
print(PrivateKey)
c = encrypt(3,PublicKey[0],PublicKey[1])
print(c)
dec = decrypt(c,PrivateKey[0],PrivateKey[1])
print(dec)