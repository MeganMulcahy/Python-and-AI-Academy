## Merge Streings Alternatively
My solution
```python 
class Solution(object):
    def mergeAlternately(self, word1, word2):
        min_len = min(len(word1), len(word2))
        result = ""

        for i in range(min_len):
            result += word1[i] + word2[i]
            
        result += word1[min_len:]
        result += word2[min_len:]
        
        return result
```
V.S
Two pointer DSA algorithm
```python
class Solution(object):
    def mergeAlternately(self, word1, word2):
        i, j = 0, 0
        result = ""  # Use a list for O(1) appends

        while i < len(word1) and j < len(word2):
            result += word1[i] + word2[j]
            i += 1
            j += 1
        
        result += word1[i:]
        result += word2[j:]
        
        return result
```
