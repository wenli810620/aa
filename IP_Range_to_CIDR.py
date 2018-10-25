#Time O(n)
#Space O(1)
class Solution(object):
    def ipToInt(self, ip):
        """
        :type ip: str
        :type n: int
        :rtype: List[str]
        """
        ans = 0
        for x in ip.split("."):
            ans = 256 * ans + int(x)
        return ans
    
    def intToIP(self,x):
        return ".".join(str((x >> i) % 256) for i in (24,16,8,0))

    def ipToCIDR(self,ip,n):
    	
        start = self.ipToInt(ip)
        print(self.ipToInt("255.0.0.16"))
        ans = []
        while n:
            mask = max(33 - (start & - start).bit_length(),
                        33 - n.bit_length())
            ans.append(self.intToIP(start) + '/' + str(mask))
            start += 1 << (32 - mask)
            n -= 1 << (32 - mask)
        return ans

if __name__ == "__main__":
	ip = "255.0.0.2"
	n = 10
	print(Solution().ipToCIDR(ip,n))
