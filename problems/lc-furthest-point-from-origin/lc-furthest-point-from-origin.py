class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        points = 0
        left = 0
        right = 0
        dash = 0
        for move in moves:
            if move == 'L':
                left += 1
            if move == 'R':
                right += 1
            if move == '_':
                dash += 1
        return abs(right - left) + dash