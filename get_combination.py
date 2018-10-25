import random
class Findwin():

	def __init__(self):
		
		self.can = [i for i in xrange(1,10)]
		self.result = []
		

	def run_game(self):
		
		while True:
			cur = random.randrange(1,12)
			
			self.play(cur)
			if len(self.can) == 0:
				return self.result
		return None

	def play(self,cursum):
		
		if len(self.can) == 0:
			return 

		res = self.comb(cursum)
		for r in res:
			for x in r:
				self.can.remove(x)
			self.result += r

	def comb(self,s):
		
		res = []
		self.get_comb(self.can, 0, [],s,res)
		return res

	def get_comb(self,nums,index,cur,s,res):

		if s == 0:
			res.append(cur)
			return 
		for i in xrange(index,len(nums)):
			self.get_comb(nums,i+1,cur+[nums[i]],s-nums[i],res)



if __name__ == "__main__":
	obj = Findwin()
	print(obj.run_game())
	