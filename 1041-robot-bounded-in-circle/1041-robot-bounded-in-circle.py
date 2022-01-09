class Solution:
    def isRobotBounded(self, ins: str) -> bool:
        x, y, cx, cy = 0, 0, 0, 1
        for i in ins:
            if i == 'R': 
                cx, cy = cy, -cx
            if i == 'L': 
                cx, cy = -cy, cx
            if i == 'G': 
                x, y = x + cx, y + cy
        if (x, y) == (0, 0) or (cx, cy) != (0,1):
            return True
        return False