"""
@Author : Swapnil Shrungare
@Goal : Create Class that represents single finite field element
@Description : 
This class is representation of single element of Finite Fields. 
"""

from ast import Return


class FieldElement:
    def __init__(self,num,prime) -> None:
        if type(num) != int or type(prime)!= int:
            raise TypeError(f"num or prime are not intgers")
        
        if num >= prime or num < 0:
            raise ValueError(f"num {num} is not in range of 0 to {prime - 1}")
        
        self.num = num
        self.prime = prime
    
    def __str__(self) -> str:
        return f"FieldElement_{self.prime}({self.num})"
        
    __repr__ = __str__

    def __eq__(self, __o: object) -> bool:
        if __o is None:
            return False
        return self.num == __o.num and self.prime == __o.prime

    def __ne__(self, __o: object) -> bool:
        return self != __o
    
    def __add__(self,__o:object) :
        if self.prime != __o.prime:
            raise TypeError("Can not add numbers in different fields")
        num = (self.num + __o.num) % self.prime
        return FieldElement(num,self.prime)
    
    def __call__(self, num , prime) :
        return FieldElement(num,prime)

    def __sub__(self,__o:object):
        if self.prime != __o.prime:
            raise TypeError("Can not substract numbers in different fields")
        num = (self.num - __o.num) % self.prime
        return FieldElement(num,self.prime)

    def __sub__(self,__o:object):
        if self.prime != __o.prime:
            raise TypeError("Can not multiply numbers in different fields")
        num = (self.num * __o.num) % self.prime
        return FieldElement(num,self.prime)
    
    def __pow__(self,exponent):
        if type(exponent) != int:
            raise TypeError("Exponent must be integer")
        n = exponent % (self.prime - 1)    
        num =pow(self.num , n, exponent)
        return FieldElement(num,self.prime)

    def __truediv__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot divide two numbers in different Fields')
        num = (self.num * pow(other.num, self.prime - 2, self.prime)) % self.prime
        return FieldElement(num, self.prime)