class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        start = bisect_right(letters,target)
        if start == len(letters):
            return letters[0]
        return letters[start]