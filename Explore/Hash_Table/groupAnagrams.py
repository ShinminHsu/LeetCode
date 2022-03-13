class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)

        for element in strs:
            sortedStr = ''.join(sorted(element))
            hash_map[sortedStr].append(element)

        return hash_map.values()

class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)

        for element in strs:
            count = [0] * 26
            for c in count:
                count[ord(c) - ord('a')] += 1

            hash_map[tuple(count)].append(element)

        return hash_map.values()