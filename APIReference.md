# Bloom Filter Package API Reference

This document provides detailed information about the API of the `PyBloom` library. The package implements a Bloom Filter data structure for probabilistic membership testing.

## Table of Contents

1. [Classes](#classes)
   - [BloomFilter](#bloomfilter)
2. [Methods](#methods)
   - [__init__(self, capacity: int, hash_functions: int) -> None](#initself-capacity-int-hash_functions-int)
   - [__contains__(self, item: bytes) -> bool](#containsself-item-bytes-bool)
   - [add(self, item: bytes) -> None](#addself-item-bytes)
   - [number_of_items(self) -> int](#number_of_itemsself-int)
   - [false_positive_rate(self) -> float](#false_positive_rateself-float)
   - [union(self, bf2: 'BloomFilter') -> 'BloomFilter'](unionself-bf2-bloomfilter-bloomfilter)
   - [intersection(self, bf2: 'BloomFilter') -> 'BloomFilter'](intersectionself-bf2-bloomfilter-bloomfilter)
   - [gamma_deniability(self) -> float](#gamma_deniabilityself)
   - [jaccard_index(self, bf2: "BloomFilter") -> float](#jaccard_indexself-bf2-bloomfilter-bloomfilter)
   - [clear(self) -> None](#clearself)

---

## Classes

### `BloomFilter`

```python
class BloomFilter:

    def __init__(self, capacity: int, hash_functions: int) -> None:
        pass

    def __contains__(self, item: bytes) -> bool:
        pass
        
    def add(self, item: bytes) -> None:
        pass
    
    def number_of_items(self) -> int:
        pass

    def false_positive_rate(self) -> float:
        pass

    def union(self, bf2: 'BloomFilter') -> 'BloomFilter':
        pass

    def intersection(self, bf2: 'BloomFilter') -> 'BloomFilter':
        pass
        
    def gamma_deniability(self) -> float:
        pass
    
    def jaccard_index(self, bf2: "BloomFilter") -> float:
        pass
        
    def clear(self) -> None:
        pass
```

## Methods

### `__init__(self, capacity: int, hash_functions: int) -> None`

    Initializes a new BloomFilter with the specified capacity and number of hash functions.
    
### `__contains__(self, item: bytes) -> bool`

    Checks if an item may be in the BloomFilter.
     
### `add(self, item: bytes) -> None`

    Adds an item to the BloomFilter.
     
### `number_of_items(self) -> int`

    Estimates the number of items present inside the Bloom Filter.
     
### `false_positive_rate(self) -> float`

    Calculates and returns the false positive rate.
     
### `union(self, bf2: 'BloomFilter') -> 'BloomFilter'`

    Creates a new Bloom Filter representing the union of two Bloom Filters.
    
### `intersection(self, bf2: 'BloomFilter') -> 'BloomFilter'`

    Creates a new Bloom Filter representing the intersection of two Bloom Filters.
    
### `gamma_deniability(self) -> float`

    Calculates the deniability of the Bloom Filter.
    
### `jaccard_index(self, bf2: "BloomFilter") -> float`
    
    Gives the value of Jaccard index between two Bloom Filters.
    
### `clear(self) -> None`
 
    Clears the Bloom Filter
