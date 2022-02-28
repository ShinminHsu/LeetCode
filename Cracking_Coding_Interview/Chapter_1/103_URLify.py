import unittest

def urlify(s: str, length: int) -> str:

    """
    inplace replacement
    """

    # new_index = len(s) - 1  # this can be used because we already know we have an extra buffer at the end
    # but it will be nicer if we compute the number of spaces by ourselves

    space_count = 0
    for i in range(length):
        if s[i] == ' ':
            space_count += 1

    new_index = length + space_count * 2

    for i in reversed(range(length)):

        if s[i] == ' ':  # replace the whitespace
            s[new_index - 3: new_index] = '%20'
            new_index -= 3

        else:
            s[new_index - 1] = s[i]
            new_index -= 1

    return s


class Test(unittest.TestCase):
    dataT = [
        ((list('Mr John Smith    '), 13, 
        list('Mr%20John%20Smith'))),
        (list('much ado about nothing      '), 22,
         list('much%20ado%20about%20nothing')),
    ]

    def test_urlift(self):
        for test_string, test_length, test_ans in self.dataT:
            actual = urlify(test_string, test_length)
            self.assertEqual(actual, test_ans)

if __name__ == '__main__':
    unittest.main()