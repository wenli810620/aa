#Implement Queue with Limited Size of Arrays
class Queue():
	def __init__(self,k):
		self.front = 0
		self.rear = -1
		self.queue = [None]*k
		self.k = k
		self.cnt = 0

	def enqueue(self,val):
		if self.cnt >= len(self.queue):
			self.queue += [None] * self.k
		
		self.rear = (self.rear + 1) % len(self.queue)
		self.queue[self.rear] = val
		self.cnt +=1
		return True
    
	def dequeue(self):
		if self.cnt == 0:
			raise Exception('queue is empty')
		pop = self.queue[self.front]
		self.front = (self.front + 1) % len(self.queue)
		self.cnt -=1
		return pop


	def size(self):
		return self.cnt

if __name__ == "__main__":
	k = 2
	obj = Queue(k)
	obj.enqueue(2)
	obj.enqueue(3)
	obj.enqueue(5)
	print(obj.dequeue())
	print(obj.dequeue())
	print(obj.dequeue())
	print(obj.dequeue())
	
	




