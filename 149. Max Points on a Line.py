from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        #we can represent every straight line as y=ax+b
        #to check the a and b for every two points would cost O(n^2) since
        #there are (n choose 2) such pairs, will do that for now:
        dicty = {}
        if len(points) == 0 or len(points) == 1:
            return len(points)
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1 == x2:
                    a = 'inf'
                    b = x1
                else:
                    a = (y2 - y1) / (x2 - x1)
                    b = y1 - a * x1
                if (a, b) in dicty:
                    dicty[(a, b)].add(i)
                    dicty[(a, b)].add(j)
                else:
                    dicty[(a, b)] = {i, j}
        if len(dicty) == 1:
            return len(points)
        return max([len(dicty[key]) for key in dicty])
