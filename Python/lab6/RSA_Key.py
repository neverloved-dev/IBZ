#TODO
#1. Form p and q and assign them random values
#2. Form e and d by the formula

import math

class Key:
    def __init__(self):
        pass

    @staticmethod
   def form_n():
       p = math.random()
       q = math.random()
       n = int(p * q)
       return n

   @staticmethod
   def calc_totient(p,q):
     totient = (p-1)*(q-1)
     return totient

   def gcd(m, n):
     if n == 0:
        return 0
     else:
            return gcd(n, m % n)