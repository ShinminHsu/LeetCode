import unittest

class Solution:
    def rotateString(self, s1: str, s2: str) -> bool:

        if len(s1) != len(s2):
            return False
        
        for i, c in enumerate(s2):
            if c == s1[0]:
                new_s = ''.join([s2[i:], s2[:i]])  #O(1)
                if new_s == s1:
                    return True
        return False

    def isSubstring(self, s1: str, s2: str) -> bool:
        return

class Solution2:
    def isSubstring(self, string: str, sub: str) -> bool:
        return string.find(sub) != -1

    def rotateString(self, s1: str, s2: str) -> bool:
        if len(s1) == len(s2) != 0:
            return self.isSubstring(s1 + s2, s2)
        return False

class Test(unittest.TestCase):
    data = [
        ("waterbottle", "erbottlewat", True),
        ("abcde", "cdeab", True),
        ("abcde", "abced", False),
        ('aaabb', 'abbaa', True),
        ('foo', 'bar', False),
        ('foo', 'foofoo', False)
        ]

    def test_rotateString(self):
        sol = Solution()
        for test_s1, test_s2, answer in self.data:
            result = sol.rotateString(test_s1, test_s2)
            self.assertEqual(answer, result)

if __name__ == "__main__":
    unittest.main()