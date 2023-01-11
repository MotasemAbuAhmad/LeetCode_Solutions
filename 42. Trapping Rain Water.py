from typing import List
from queue import LifoQueue, Queue


class Solution:
    def trap(self, height: List[int]) -> int:
        stack_l = LifoQueue()
        stack_r = Queue()
        ans = 0
        i =0
        last_lvl = 0
        while i<len(height)-1:
            if height[i]==height[i+1]:
                i+=1
                continue
            if height[i]>height[i+1]:
                stack_l.put(i)
                i+=1
                continue
            last_lvl=height[i]
            if height[i]<height[i+1]:
                i+=1
                r=i
                while not stack_l.empty():
                    l = stack_l.get()
                    ans += (min(height[l], height[r]) - last_lvl) * (r - l-1 )
                    last_lvl = min(height[l], height[r])
                    if height[l] >= height[r]:
                        stack_l.put(l)
                        break
                stack_l.put(i)
        return ans




if __name__ == '__main__':
    print(Solution().trap([6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]))

