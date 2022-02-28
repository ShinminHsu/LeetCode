"""
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
"""
import unittest

"""
class Solution:
    def is_unique(self, s: str) -> bool:
        
        hash = set()

        for c in s:
            if c in hash:
                return False

            hash.add(c)
        
        return True

class Solution2:
    def is_unique(self, s: str) -> bool:
        
        s = sorted(s)
        pre_c = ''
        for c in s:
            if c == pre_c:
                return False
            pre_c = c
        
        return True
"""

def is_unique(string):
    # Assuming character set is ASCII (128 characters)
    if len(string) > 128:
        return False

    char_set = [False for _ in range(128)]
    for char in string:
        val = ord(char)
        if char_set[val]:
            # Char already found in string
            return False
        char_set[val] = True

    return True

class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = is_unique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = is_unique(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()