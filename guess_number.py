#guess_number
import collections
class Guessgame():
	def __init__(self,target):
		self.count = 0
		self.target = target

	def guess_server(self,guess):
		self.count +=1
		map_d = collections.defaultdict(int)
		bulls = 0
		cows = 0
		for i in xrange(len(self.target)):
			if self.target[i] == guess[i]:
				bulls += 1
				continue
			map_d[self.target[i]] +=1
		for i in xrange(len(guess)):
			if map_d[guess[i]] > 0 and guess[i] != self.target[i]:
				cows +=1
				map_d[guess[i]] -=1
		res = [bulls,cows]
		return res

	def guess(self):
		res = ["0"]*4
		base = "1111"
		cur_res = self.guess_server(base)
		first = cur_res[0]
		if first == 4: return base
		for i in xrange(4):
			lastResponse = first
			chbase = list(base)
			for j in xrange(2,6):
				chbase[i] = str(j)
				tmp_res = self.guess_server("".join(chbase))
				response = tmp_res[0]
				if response == 4:
					return "".join(chbase)
				elif response != lastResponse:
					if response > lastResponse:
						res[i] = str(j)
					else:
						res[i] = "1"
					break
				else:
					#update last response
					lastResponse = response
			if "0" == res[i] : res[i] = "6"
		return ["".join(res),self.count]

	
if __name__ == "__main__":
	print(Guessgame("6666").guess())


















