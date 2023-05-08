class Solution:
    def sortSentence(self, s: str) -> str:
        reordered = ['' for i in range(len(s.split()))]
        
        for word in s.split():
            reordered[int(word[-1]) - 1] = word[:-1]
        
        return ' '.join(reordered)