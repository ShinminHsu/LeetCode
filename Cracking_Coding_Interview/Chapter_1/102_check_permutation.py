import collections
import unittest

"""
# Time Complexity: O(nlogn)
def check_permutation(s1: str, s2: str) -> bool:
    return sorted(s1) == sorted(s2)

# Mine 2
def check_permutation(s1: str, s2: str) -> bool:
    hash_1 = collections.Counter(s1)
    for c in s2:
        if c not in hash_1:
            return False

        if c in hash_1:
            hash_1[c] -= 1

        if hash_1[c] < 0:  # we can return here immediately to be faster
            return False
    
    return not hash_1
"""

def check_permutation(str1, str2):
    if len(str1) != len(str2):  # 沒想到這一段
        return False
    counter = collections.Counter()
    for c in str1:
        counter[c] += 1
    for c in str2:
        if counter[c] == 0:
            return False
        counter[c] -= 1
    return True

class Test(unittest.TestCase):
    dataT = [(('abcd'), ('cbda'))]
    dataF = [(('abcd'), ('cda'))]

    def test_unique(self):
        for test_string1, test_string2 in self.dataT:
            actual = check_permutation(test_string1, test_string2)
            self.assertTrue(actual)

        for test_string1, test_string2 in self.dataF:
            actual = check_permutation(test_string1, test_string2)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()
