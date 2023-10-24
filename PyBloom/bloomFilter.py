# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 14:25:23 2023

@author: Diegomangasco
"""

import mmh3
import math
from bitarray import bitarray

class BloomFilter():
    """
    Bloom Filter data structure.
    """
    
    def __init__(self, capacity: int, hash_functions: int, intersection: False) -> None:
        """
        Creates a new BloomFilter instance.
        
		Return: None.
        """
        
        self.capacity = capacity
        self.array = bitarray(capacity)
        self.array.setall(0)
        self.hash_functions = hash_functions
        self.flag_intersection = intersection
        self.count_1 = None
        self.count_2 = None
        self.count_union = None
        
    def __contains__(self, item: bytes) -> bool:
        """
        Checks if the item is present inside the Bloom Filter.
        
		Return: boolean value, if True the item maybe inside the filter, if False the item definitely it is not inside the filter.
        """
        
        for i in range(self.hash_functions):
            res = mmh3(item, i)
            res %= self.capacity
            if self.array[res] == 0:
                return False
        return True
    
    def add(self, item: bytes) -> None:
        """
        Inserts a new item inside the Bloom Filter.
        
		Return: None.
        """
        
        for i in range(self.hash_functions):
            res = mmh3(item, i)
            res %= self.capacity
            self.array[res] = 1
    
    def number_of_items(self) -> int:
        """
        Gives the estimate of the number of items inside the Bloom Filter.
        
		Return: int number that represents the number of elements estimated.
        """
        
        if not self.flag_intersection:
            a = - self.capacity / self.hash_functions
            x = sum([1 for b in self.array if b == 1])
            b = math.log1p(-x/self.capacity)
            n = math.ceil(a * b)
        else:
            n = self.count_1 + self.count_2 - self.count_union
        return n
            
    def false_positive_rate(self) -> float:
        """
        Gives the false positive rate.
        
		Return: float number in [0,1] that represents the false positive rate.
        """
        
        elements = self.number_of_items()
        exp = math.exp(elements*self.hash_functions/self.capacity)
        diff = 1 - exp
        if diff < 0:
            diff = 0
        fpr = diff ** self.hash_functions
        return fpr
    
    def union(self, bf2: "BloomFilter") -> "BloomFilter":
        """
        Performs the union between two Bloom Filters.
        
		Return: New BloomFilter representing the union of the two input Bloom Filters.
        """
        
        assert self.capacity == bf2.capacity
        assert self.hash_functions == bf2.hash_functions
        bf_new = BloomFilter(self.capacity, hash_functions=self.hash_functions)
        bf_new.array = self.array | bf2.array
        return bf_new

    def intersection(self, bf2: "BloomFilter") -> "BloomFilter":
        """
        Performs the intersection between two Bloom Filters.
        
		Return: New BloomFilter representing the intersection of the two input Bloom Filters.
        """
        
        assert self.capacity == bf2.capacity
        assert self.hash_functions == bf2.hash_functions
        bf_new = BloomFilter(self.capacity, hash_functions=self.hash_functions, intersection=True)
        bf_new.array = self.array & bf2.array
        bf_new.count_1 = self.number_of_items()
        bf_new.count_2 = bf2.number_of_items()
        bf_new.count_union = self.union(bf2).number_of_items()
        return bf_new
    
    def gamma_deniability(self) -> float:
        """
        Gives the gamma value for Bloom Filter deniability.

		Return: float number in [0,1] that represents the deniability.
        """

        k = self.hash_functions
        m = self.capacity
        n = self.number_of_items()
        v = ((math.pow(2, 48) - n) * (math.pow((1 - math.exp((-1 * k * n) / m)), k)))
        arg = (1 - math.exp(((-1 * v * k) / (m * (1 - math.exp((-k * n) / m))))))
        return math.pow(arg, k)
    
    def jaccard_index(self, bf2: "BloomFilter") -> float:
        """
        Gives the value of Jaccard index between two Bloom Filters.

		Return: float number in [0,1] that represents the Jaccard index.
        """
        
        bf_int = self.intersection(bf2)
        bf_union = self.union(bf2)
        return float(bf_int.number_of_items()) / float(bf_union.number_of_items())
    
    def clear(self) -> None:
        """
        Clears the Bloom Filter.

		Return: None.
        """
        
        self.array.setall(0)
