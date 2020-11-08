import collections

class Solution:
    def canVisitAllRooms(self, rooms):

        all = set()
        queue = collections.deque()
        queue.append(rooms[0])

        while queue:
            for key in queue.popleft():
                if key == 0:
                    continue
                if key not in all:
                    all.add(key)
                    queue.append(rooms[key])
        return False if len(all) + 1 != len(rooms) else True

rooms = [[], [1]]
s = Solution()
print(s.canVisitAllRooms(rooms))
