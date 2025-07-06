import random
from sympy import *

def generated_keys():
  p = random.randint(100, 200)
  q = random.randint(100, 200)
  while(not isprime(p) or not isprime(q)):
    p = random.randint(100, 200)
    q = random.randint(100, 200)
  n = p * q
  euler = (p - 1) * (q - 1)
  # 1 < e < euler
  e = random.randint(2, euler - 1)
  while (gcd(e, euler) != 1):
    e = random.randint(2, euler - 1)
  d = mod_inverse(e, euler)
  # return public key (n, e) and private key (n, d)
  return (n, e), (n, d)
  
def encrypt(message, public_key):
  n, e = public_key
  c = (message ** e) % n
  return c
  
def decrypt(message, private_key):
  n, d = private_key
  m = (message ** d) % n
  return m
  
def main(): 
  public_key, private_key = generated_keys()
  print("Public Key:", public_key)
  print("Private Key:", private_key)
  message = random.randint(1, 100)
  print("Original Message:", message)
  encrypted_message = encrypt(message, public_key)
  print("Encrypted Message:", encrypted_message)
  decrypted_message = decrypt(encrypted_message, private_key)
  print("Decrypted Message:", decrypted_message)
  
if __name__ == "__main__":
  main()