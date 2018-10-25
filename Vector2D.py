class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.row = 0
        self.col = 0
        self.tmp = None
        self.getnextcnt = 0
        self.vec2d = vec2d
       
        

    def next(self):
        """
        :rtype: int
        """
        self.getnextcnt +=1
        return self.tmp

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.row < len(self.vec2d):
            if self.col < len(self.vec2d[self.row]):
                self.tmp = self.vec2d[self.row][self.col]
                self.col +=1
                return True
            else:
                self.row +=1
                self.col = 0
           
        return False

    def _remove(self):
        if self.getnextcnt == 0:
            raise Exception ('no next available to be removed')
        else:
            if self.col == 0:
                self.row -=1
                self.col = len(self.vec2d[self.row]) - 1
                self.vec2d[self.row].pop(self.col)
            else:
                self.col -=1
                self.vec2d[self.row].pop(self.col)
            self.getnextcnt -=1
            return 

        
if __name__ == "__main__":
# Your Vector2D object will be instantiated and called as such:
    vec2d = [[],[3,4],[6,5]]
    i = Vector2D(vec2d)
    v = []
    while i.hasNext():
        res = i.next()
        v.append(res)
        if res == 6:
            i._remove()
    print(v)
   
    