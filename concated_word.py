class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        words = sorted(words, key = lambda x: len(x))
       
        res = []
        pre_word = set()
        
        for s in words:
            if len(s) == 0:
                continue
            if self.word_break(s,pre_word):
                res.append(s)
            pre_word.add(s)
            
        return res
    
    def word_break(self,word,wordset):
        if len(wordset) == 0:
            return False
        dp = [False for _ in xrange(len(word)+1)]
        dp[0] = True
        for i in xrange(1,len(word)+1):
            for j in xrange(i):
                if dp[j] and word[j:i] in wordset:
                    dp[i] = True
                    break
        return dp[-1]