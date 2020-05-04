class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        
        while len(stones) >= 2:
            stones = sorted(stones)
            stones.append(stones.pop() - stones.pop())
            
        return stones[0]