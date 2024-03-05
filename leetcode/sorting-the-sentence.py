class Solution:
    def sortSentence(self, s: str) -> str:
        splitted = s.split(' ')
        ans = ['']*len(splitted)

        for ele in splitted:
            index = int(ele[-1]) - 1
            ans[index] = ele[:-1]

        return ' '.join(ans)