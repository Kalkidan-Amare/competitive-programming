class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dict = defaultdict(int)

        for ele in bills:
            dict[ele] += 1
            if ele == 10:
                if dict[5]:
                    dict[5] -= 1
                else:
                    return False
            elif ele == 20:
                if dict[10] and dict[5]:
                    dict[10] -= 1
                    dict[5] -= 1
                elif dict[5] >= 3:
                    dict[5] -= 3
                else:
                    return False
            
        return True