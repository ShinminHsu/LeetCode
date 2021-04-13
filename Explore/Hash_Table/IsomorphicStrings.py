class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        hash_map = {}

        for char_s, char_t in zip(s, t):

            if char_s in hash_map:
                if hash_map[char_s] != char_t:
                    return False
            else:
                # check if char_t in hash_map but without the same key
                if char_t in hash_map.values():
                    return False
                else:
                    hash_map[char_s] = char_t

        return True


