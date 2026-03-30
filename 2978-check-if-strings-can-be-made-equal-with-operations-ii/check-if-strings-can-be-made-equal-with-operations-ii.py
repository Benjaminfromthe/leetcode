from collections import Counter

class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        # Separate characters by even and odd indices for s1
        s1_even = s1[0::2]
        s1_odd = s1[1::2]
        
        # Separate characters by even and odd indices for s2
        s2_even = s2[0::2]
        s2_odd = s2[1::2]
        
        # Two strings can be made equal if:
        # 1. Their even-indexed characters are the same (any order)
        # 2. Their odd-indexed characters are the same (any order)
        return Counter(s1_even) == Counter(s2_even) and \
               Counter(s1_odd) == Counter(s2_odd)