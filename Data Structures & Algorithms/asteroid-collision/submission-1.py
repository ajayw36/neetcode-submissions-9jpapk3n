class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                if a + stack[-1] < 0:
                    stack.pop()
                elif a + stack[-1] > 0:
                    break
                else:
                    stack.pop()
                    break
            else: stack.append(a)
        return stack