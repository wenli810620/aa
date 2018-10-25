
class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
       
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        row = len(board)
        col = len(board[0])
        start = ""
        goal = ""
        for i in xrange(row):
            for j in xrange(col):
                start += str(board[i][j])
                goal += str((i*col+j+1)%(row*col))
        if start == goal : return 0
        
        queue = [start]
        visited = set()
        visited.add(start)
        cnt = 0
        
        while queue:
            size = len(queue)
            cnt +=1
            for i in xrange(size):
                s = queue.pop(0)
                p = s.index('0')
                x = p/col 
                y = p%col

                for dir in directions:
                    xx = x+ dir[0]
                    yy = y+dir[1]
                    if xx >= row or xx< 0 or yy >=col or yy < 0: 
                        continue
                    pp = xx*col + yy
                    t = list(s)
                    t[p],t[pp] = t[pp],t[p]
                  
                    t = "".join(t)
                    if t in visited: continue
                    if t == goal :
                        return cnt
                    
                    queue.append(t)
                    visited.add(t)
              
           
                   
        return -1


class A_search(object):
    def slidingPuzzle(self, board):
        self.row = len(board)
        self.col = len(board[0])
        self.goal = ""
        bs = ""
        for i in xrange(2):
            for j in xrange(3):
                bs += str(board[i][j])
                self.goal += str((i*self.col+j+1)%(self.row*self.col))
        heap = [(0,0,bs)]
        closed = []

        while len(heap) > 0:
            h,d,b = heapq.heappop(heap)
            if self.get_score(b) == 0:
                return d
            elif b in closed:
                continue
            else:
                for neighbor in self.get_neighbors(b):
                    if neighbor in closed: continue
                    heapq.heappush(heap, (d + 1 + self.get_score(neighbor), d + 1, neighbor))
            closed.append(b)
        return -1

    def get_neighbors(self, bs):
        res = []
        directions = ((0,1),(0,-1),(1,0),(-1,0))
        p = bs.index('0')
        x = p/self.col 
        y = p%self.col

        for dir in directions:
            xx = x+ dir[0]
            yy = y+dir[1]
            if xx >= self.row or xx< 0 or yy >=self.col or yy < 0: 
                continue
            pp = xx*self.col + yy
            t = list(bs)
            t[p],t[pp] = t[pp],t[p]
            t = "".join(t)
            res.append(t)
        return res

    def get_score(self, bs):
        score = 0
        for i in xrange(len(bs)):
            score += abs(int(bs[i]) - int(self.goal[i]))
        return score

class Game(object):
    
    def run_game(self,board):
        bs = ""
        self.row = len(board)
        self.col = len(board[0])
        self.goal = ""
        for i in xrange(self.row):
            for j in xrange(self.col):
                bs += str(board[i][j])
                self.goal +=   str((i*self.col+j+1)%(self.row*self.col))
        queue = []
        queue.append(bs)
        visited = set()
        visited.add(bs)
        cnt = 0
        while queue :
            size = len(queue)
            cnt +=1
            directions = ((0,1),(0,-1),(1,0),(-1,0))
            for i in xrange(size):
                cur = queue.pop(0)
                for roff,coff in directions:
                    self.move(cur,roff,coff)
                    if self.check(): return cnt
                    if self.curbs not in visited:
                        queue.append(self.curbs)
                        visited.add(self.curbs)
        return -1

    def move(self,bs,roff,coff):
        
        p = bs.index('0')
        x = p/self.col
        y = p%self.col
        xx = x+ roff
        yy = y+ coff
        if xx >= self.row or xx< 0 or yy >=self.col or yy < 0: 
            return 
        pp = xx*self.col + yy
        t = list(bs)
        t[p],t[pp] = t[pp],t[p]
        t = "".join(t)
        self.curbs = t
        return 
            

    def check(self):
        if self.curbs == self.goal:
            return True
        else:
            return False

if __name__ == "__main__":
    board = [[1,2,3],[4,0,5]]
    board1 = [[4,1,2],[5,0,3]]

    print(Game().run_game(board1))

