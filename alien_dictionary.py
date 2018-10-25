class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        
        inb = collections.defaultdict(int)
        oub = collections.defaultdict(set)
        ch_set = set()
        for word in words:
            for w in word:
                ch_set.add(w)
        
        for i in xrange(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            for j in xrange(min(len(word1),len(word2))):
                if word1[j] != word2[j]:
                    if word2[j] not in oub[word1[j]]:
                        oub[word1[j]].add(word2[j])
                        inb[word2[j]] +=1
                    break
        queue = []
        for ch in ch_set:
            if inb[ch] == 0:
                queue.append(ch)
               
        res = []    
        while queue:
            cur = queue.pop(0)
            res.append(cur)
            for nxt in oub[cur]:
                inb[nxt] -=1
                if inb[nxt] == 0:
                    queue.append(nxt)
        if len(res) == len(ch_set): return "".join(res)
        else: return ""