class Solution(object):
	def __init__(self):
		self.queue = []
  self.curr_sum = 0
 def movingAverage(self, num, size):
		if len(self.queue) >= size:
			val = self.queue.pop(0)
   self.curr_sum -= val
  self.curr_sum += num
  self.queue.append(num)
  return float(self.curr_sum)/len(self.queue)
window_size = int(input())
num = int(input())
while num != -1:
 num = int(input())
