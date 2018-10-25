String Pyramids Transition Matrix
#time O(A^N)
#space O(N^2)
class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        
        self.parent = collections.defaultdict(set)
        for l,r,w in allowed:
            self.parent[l,r].add(w)
        return self.solve(bottom)
            
    
        
    def build(self,A,ans,i = 0):
        if i + 1 == len(A):
            yield "".join(ans)
        else:
            for w in self.parent[A[i], A[i+1]]:
                ans.append(w)
                for result in self.build(A, ans, i+1):
                    yield result
                ans.pop()
    def solve(self,A):
        if len(A) == 1: return True
        
        return any(self.solve(cand) for cand in self.build(A,[]))