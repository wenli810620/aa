#shut_box
#time complexity (2^n)
#space complexity (n)
import random
class Shut_box(object):
	def __init__(self,total):
		self.queue = [i for i in xrange(1,total+1)]
		self.range = [2,3,4,5,6,7,8,9,10,11,12]

	def getcomb(self,cur):
		
		cur_nums = []
		res = []
		cur_nums = self.queue
		self.dfs(cur_nums,0,[],res,cur)
		if len(res) > 0:
			res = sorted(res, key = lambda x:(len(x),x[0]))
			
			return res[0]
		return res
	def dfs(self,nums,index,cur_path,res,target):
		if target == 0:
			res.append(cur_path)
			return 
		for i in xrange(index,len(nums)):
			if nums[i] > target: break
			if not cur_path or nums[i] >= cur_path[-1]:
				self.dfs(nums, i+1, cur_path+[nums[i]], res, target-nums[i])

	def run_game(self):
		cnt = 0
		is_done = False
		ans = []
		while not is_done and cnt < 40: 
			cur = random.choice(self.range)
			comb = []
			if cur in self.queue:
				self.queue.remove(cur)
				ans.append(cur)
			else:
				comb = self.getcomb(cur)

				for x in comb: 
					ans.append(x)
					self.queue.remove(x)
			
			if len(self.queue) == 0 :
					is_done = True
			cnt +=1
		
		return ans

#combination => 



if __name__ == "__main__":
	obj = Shut_box(9)
	print(obj.run_game())







