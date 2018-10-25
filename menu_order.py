#menu_order
#one element can used multiple times in the result. combination sum i

#or one element can only be used once 
#check if dup exist in the input
def getcom(comb,target):
	res = []
	if len(comb) == 0 or target <= 0:
		return res
	nums = []
	for key in comb:
		nums.append(int(round(comb[key]*100000)))
	search(nums,int(round(target*100000)),[],res)
	return res


def search(nums,remain,cur_path,res):
	if remain == 0:
		res.append(remain)
		return 
	for num in nums:
		if num > remain: break
		if cur_path and num < cur_path[-1] : continue
		else:
			search(nums, remain-num, cur_path+[num], res)

#time worst case 
# time O(M*N)
#space O(N)
def getcom2(comb,target):
	res = []
	if len(comb) == 0 or target <= 0:
		return res
	nums = []
	for key in comb:
		nums.append((int(round(comb[key]*10000)),key))

	search2(nums,int(round(target*10000)),[],[],res)
	return res

def search2(nums,remain,cur_path,cur_key,res):
	if remain == 0:
		res.append(cur_key)
		return 
	for num,key in nums:
		
		if num > remain: break 
		if cur_path and num < cur_path[-1]: continue
		search2(nums,remain - num, cur_path + [num], cur_key + [key], res)

def dp(candidates,target):
	dp = [[] for _ in xrange(target)]
    candidates = sorted(candidates, key = lambda x:x[0])
    for t in xrange(1,target+1):
        new_dp = []
        for num,key in candidates:
            if num > t:
            	break
            elif num == t:
                new_dp.append([num])
            else:
                for comb in dp[t-num-1]:
                	if comb[-1][0] <= num:
                    	new_dp.append(comb + [num])
           dp[t-1] = new_dp
        
    return dp[-1]


#if dup
def search2(nums,remain,cur_path,cur_key,res):
	if remain == 0:
		res.append(cur_key)
		return 
	for i in xrange(len(nums)):
		if i > 0 and nums[i-1][1] == nums[i][1]: continue
		if nums[i][0] > remain: break 
		if cur_path and nums[i][0] < cur_path[-1]: continue
		search2(nums,remain - nums[i][0], cur_path + [nums[i][0]], cur_key + [nums[i][1]], res)


def search(nums, remain,cur_path,res):
	if remain == 0:
		res.append(cur_path)
		return 
	for i in xrange(len(nums)):
		if i > 0 and nums[i] == nums[i-1]: continue
		if nums[i] > remain: break
		if cur_path and cur_path[-1] > nums[i] : continue
if __name__ == "__main__":
	print(getcom2({"break":10,"lunch":20,"dinner":20,"dinner":20},30))




