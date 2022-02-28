from cgi import test
import collections
import unittest

def palindrome_permutation(string: str) -> bool:

    odd_appear = False
    counter = collections.Counter(string.lower())

    for c, cnt in counter.items():
        if c == ' ':
            continue
        if cnt % 2 == 1:
            if odd_appear:
                return False
            else:
                odd_appear = True
    return True

class Test(unittest.TestCase):
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_palindrome_permutation(self):
        for test_string, answer in self.data:
            result = palindrome_permutation(test_string)
            self.assertEqual(result, answer)

if __name__ == '__main__':
    unittest.main()