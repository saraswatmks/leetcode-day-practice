"""
This is a graph question.

There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.
When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.
Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.

Input: rooms = [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can not enter room number 2 since the only key that unlocks it is in that room.

https://leetcode.com/problems/keys-and-rooms/description
"""


class Solution:
    def solutionOne(self, rooms):
        """
        Iterative DFS with a stack.

        Time Complexity: O(N) N- > number of keys
        Space Complexity: O(N) N -> unique keys
        """
        visited = set()
        to_visit = [0]

        # iterate through all rooms and visit whichever possible
        while to_visit:
            room = to_visit.pop()
            if room in visited:
                continue
            visited.add(room)
            to_visit.extend(rooms[room])  # here each list key is used an index

        return len(visited) == len(rooms)

    def solutionTwo(self, rooms):
        """
        Time Complexity: O(N) N- > number of keys
        Space Complexity: O(N) N -> unique keys
        """
        visited = set()

        def dfs(room: int) -> None:
            if room not in visited:
                visited.add(room)
                for key in rooms[room]:
                    dfs(key)

        dfs(0)
        return len(visited) == len(rooms)


if __name__ == "__main__":
    arr = [[1, 3], [3, 0, 1], [2], [0]]
    s = Solution().solutionTwo(arr)
    print(s)
