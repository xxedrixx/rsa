import math
from icecream import ic

def prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
    
def get_p():
    p = int (input ("Enter p: "))
    while True:
        if prime(int (p)):
            print(f"p={p}\n")
            return (int (p))
        else:
            print(f"{p} is NOT a prime number")
            p = input ("Enter p: ")
    
def get_q():
    q = int (input ("Enter q: "))
    while True:
        if prime(int (q)):
            print(f"q={q}\n")
            return (int (q))
        else:
            print(f"{q} is NOT a prime number")
            q = input ("Enter q: ")
    
def get_r(L):
    r = int (input("Enter r: "))
    while True:
        if int (math.gcd(r,L)) == 1:
            print(f"r={r}\n")
            return (int (r))
        else:
            print(f"{r} and {L} are NOT coprime")
            r = int (input("Enter r: "))
    
p = get_p()
q = get_q()
L = math.lcm(p-1,q-1)
r = get_r(L)
print (f"p={p}, q={q}")
n = p*q
print (f"n={n}\nr={r}\nL={L}\n")
s = pow (r, -1, L)
print (f"s={s}")


message = str(input ("Enter message: "))
to_ascii = [ord(char) for char in message]
print (f"{message} to ascii: {to_ascii}")

encrypted = []
decrypted = []

def encryption():
    for char in to_ascii:
        encr = (char**r) % n
        encrypted.append(encr)
    print (f"Encrypted ASCII: {encrypted}")
        
encryption()

def decryption():
    for char in encrypted:
        decr = (char**s) % n
        decrypted.append(decr)
    print (f"Decrypted ASCII: {decrypted}")
    
decryption()
    
to_string = ''.join(chr(value) for value in decrypted)
print(f"Decrypted message: {to_string}")