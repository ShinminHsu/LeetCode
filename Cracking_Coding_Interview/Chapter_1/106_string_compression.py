import unittest

def compress(s: str) -> str:

    res = []
    pre_c = ''
    count = 0

    for c in s:
        if pre_c and c != pre_c:
            res.append(pre_c + str(count))
            count = 0

        pre_c = c
        count += 1

    # append the last character
    res.append(pre_c + str(count))

    return ''.join(res) if len(res) < len(s) else s

class Test(unittest.TestCase):
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('aabccccca', 'a2b1c5a1'),
        ('abc', 'abc')
    ]

    def test_compress(self):
        for test_string, answer in self.data:
            result = compress(test_string)
            self.assertEqual(result, answer)

if __name__ == '__main__':
    unittest.main()