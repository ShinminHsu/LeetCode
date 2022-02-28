import unittest

def one_edit_replace(s, t):
    edited = False
    for c1, c2 in zip(s, t):
        if c1 != c2:
            if edited:
                return False
            else:
                edited = True
    return True

def one_edit_insert(s, t):
    """
    t is the longer one (index: j)
    """
    edited = False
    i = j = 0

    while i < len(s) and j < len(t):

        if s[i] != t[j]:

            if edited:
                return False
            
            else:
                edited = True
                j += 1

        else:
            i += 1
            j += 1

    return True


def oneAway(s: str, t: str) -> bool:

    if len(s) == len(t):
        return one_edit_replace(s, t)
    elif len(s) - 1 == len(t):
        return one_edit_insert(t, s)
    elif len(t) - 1 == len(s):
        return one_edit_insert(s, t)    

    return False


def oneAway_2(s: str, t: str) -> bool:
    """
    Merge one_edit_replace and one_edit_insert
    """

    if abs(len(s), len(t)) > 1:
        return False

    # get shorter and longer string
    s1 = s if len(s) < len(t) else t
    s2 = t if len(t) < len(s) else s

    i = j = 0
    edited = False

    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if edited:
                return False
            
            edited = True

        # if matches or their lengths are equal
        if len(s1) == len(s2) or s1[i] == s2[j]:
            i += 1

        # always move the pointer for longer string
        j += 1

    return True
    

class Test(unittest.TestCase):
    data = [
        ('pale', 'ple', True),
        ('pale', 'pales', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'paless', False),
        ('pa', 'pale', False),
        ('pale', 'pale', True),
        ('lpe', 'ple', False),
        ('lpes', 'ple', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

    def test_oneAway(self):
        for test_s, test_t, answer in self.data:
            result = oneAway(test_s, test_t)
            self.assertEqual(answer, result)

if __name__ == '__main__':
    unittest.main()