class TreeNode(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
	
def lowestCommonAncestor(root, p, q):
        
        parent = {}
        parent[root] = None
        queue = [root]
        while p not in parent or q not in parent:
            root = queue.pop(0)
            if root.left:
                parent[root.left] = root
                queue.append(root.left)
            if root.right:
                parent[root.right] = root
                queue.append(root.right)
        ancestor = set()
        while p in parent:
            ancestor.add(p)
            p = parent[p]
            
        while q not in ancestor:
            q = parent[q]
        return q.val



if __name__ == "__main__":
	root = TreeNode(3)
	child1 = TreeNode(2)
	child2 = TreeNode(4)
	root.left = child1
	root.right = child2
	p = child1
	q = child2
	print(lowestCommonAncestor(root,p,q))
