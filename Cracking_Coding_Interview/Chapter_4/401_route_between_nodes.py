from typing import List
from collections import deque
import unittest

def routeBtnNodes(n: int, edges: List[List[int]], source: int, destination: int) -> bool:

    """
    In CtCI, it's directed graph. But in leetcode, it's bi-directed graph
    """

    if source == destination:
        return True

    visited = set()

    # BFS
    # convert edges into adjacency list
    adjacency_list = [[] for _ in range(n)]
    for s, d in edges:
        adjacency_list[s].append(d)
        adjacency_list[d].append(s)

    queue = deque()

    # append the first level first
    for n in adjacency_list[source]:
        queue.append(n)

    while queue:
        node = queue.popleft()
        if node == destination:
            return True
        for n in adjacency_list[node]:
            if n not in visited:
                visited.add(n)
                queue.append(n)

    return False


class Test(unittest.TestCase):
    data = [
        (3, [[0,1],[1,2],[2,0]], 0, 2, True),
        (6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5, False),
        (6, [[0,1],[0,2],[1,3],[3,5],[5,4],[4,3]], 0, 5, True),
        (1, [], 0, 0, True),
        (2, [[0, 1]], 0, 0, True),
        (2, [[0, 1]], 0, 1, True),
        (2, [], 0, 1, False),
        (10, [[0,7],[0,8],[6,1],[2,0],[0,4],[5,8],[4,7],[1,3],[3,5],[6,5]], 7, 5, True)
    ]

    def test_route(self):
        for n, edges, source, destination, answer in self.data:
            result = routeBtnNodes(n, edges, source, destination)
            self.assertEqual(result, answer)


if __name__ == '__main__':
    unittest.main()