
class Trie(object):
	def __init__(self):
		self.children = {}
		

class FileSystem(object):
	def __init__(self):
		self.root = Trie()
		self.content_map = {}
		self.callbackmap = {}

	def create_path(self,path,value):
		if not path or value is None:
			return False
		cur = self.root
		paths = [p for p in path.split("/")]
		
		for i in xrange(len(paths)):
			if len(paths[i]) == 0:
				continue
			if paths[i] not in cur.children:
				if i == len(paths) -1:
					cur.children[paths[i]] = Trie()
				else:
					return False
			
			cur = cur.children[paths[i]]
		cur.isFile = True
		self.content_map[path] = value
		return True

    			
	def get_content(self,path):
		if path not in self.content_map[path]:
			return False
		cur = self.root
		paths = [p for p in path.split("/")]
		for p in paths:
			if len(p) == 0:
				continue
			if p not in cur.children:
				return "Error"
			cur = cur.children[p]
		if cur.isFile:
			return self.content_map[path]
		else:
			return "Error"
	def set_content(self,path,val):
		if path not in self.content_map:
			return False
		self.content_map[path] = val
		i = 0
		while i < len(path):
			cur_path = path[:-i or None]
			if cur_path in self.callbackmap:
				func = self.callbackmap[cur_path]
				func()
			i +=1
		return True

	def watch(self, path, callback):
		if not path in self.content_map:
			return False
		self.callbackmap[path] = callback
		callback()

	def callback0(self):
		print("No")

	def callback1(self):
		print("Yes")

   
if __name__ == "__main__":
	obj = FileSystem()
	print(obj.create_path("",None))
	print(obj.create_path("/a",1))
	print(obj.create_path("/a/b",4))
	obj.watch("/a",obj.callback0)
	obj.watch("/a/b",obj.callback1)
	#print(obj.get_content("/a"))
	print(obj.set_content('/a',2))
	print(obj.set_content("/a/b",3))

	'''print(obj.create_path("/a/b",2))
	print(obj.get_content("/a/b"))
	print(obj.create_path("/c/d",1))
	print(obj.get_content("/c/d"))'''




