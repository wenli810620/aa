#time O(N*L^2)
def palindromePairs(words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        res = set()
        re_dict = {}
        for i in xrange(len(words)):
            reverse = words[i][::-1]
            re_dict[reverse] = i
            
        for i in xrange(len(words)):
            word = words[i]
            for j in xrange(len(word)+1):
                first = word[:j]
                second = word[j:]
                if first in re_dict and re_dict[first] != i and ispal(second):
                    res.add((i,re_dict[first]))
                if second in re_dict and re_dict[second] != i and ispal(first):
                    res.add((re_dict[second],i))
        return list(res)

def ispal(word):
    return True if word[::-1] == word else False

#Trie method
class Trie(object):
    def __init__(self):
        self.paths = collections.defaultdict(Trie)
        self.wordEndIndex = -1
        self.palBelow = []
    
    def add_word(self,word,index):
        trie = self
        n = len(word)
        for i, char in enumerate(word[::-1]):
            if word[:n-i] == word[:n-i][::-1]:
                trie.palBelow.append(index)
            trie = trie.paths[char]
        trie.wordEndIndex = index
    
            
class PalindromePairs(object):
    def __init__(self):
        self.root = Trie()
        
    def getpalindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        for i in xrange(len(words)):
            self.root.add_word(words[i],i)
            
        output = []
        for i, word in enumerate(words):
            candidates = self.getPalindromes(word, i)
            for c in candidates:
                if i != c:
                    out.append([words[i],words[c]])
        return output
        
    def getPalindromes(self,word, index):
        node = self.root
        output = []
        while word:
            if node.wordEndIndex >= 0:
                if self.isPalindrome(word):
                    output.append(node.wordEndIndex)
            if word[0] not in node.paths:
                return output
            node = node.paths[word[0]]
            word = word[1:]

        if node.wordEndIndex >= 0:
            output.append(node.wordEndIndex)
        output += node.palBelow
        return output

    def isPalindrome(self,word):
        return True if word == word[::-1] else False

if __name__ == "__main__":
    print(palindromePairs(["bcd","dcb","lllss","lll"]))




