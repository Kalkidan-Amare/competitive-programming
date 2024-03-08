class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        ptr1 = ptr2 = 0

        while ptr1 < len(name) or ptr2 < len(typed):
            if ptr2 == len(typed):
                return False

            if ptr1 < len(name) and name[ptr1] == typed[ptr2]:
                ptr1 += 1
                ptr2 += 1
            elif ptr2 - 1 >= 0 and typed[ptr2] == typed[ptr2-1]:
                ptr2 += 1
            else:
                return False

        return True