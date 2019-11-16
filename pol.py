class Stack(list):
 
	def __init__(self,):
		self = []
    
	def put(self, c):
		self.append(c)
    
	def drop(self):
		self.pop()
        
	def pull(self):
		return self.pop()
	
	def dup(self):
		return self.append(self[-1])
		
	def reverse(self):
		if len(self)>=2:
			t = self[-1]
			self[-1] = self[-2]
			self[-2] = t
		
	def rotate(self):
		if len(self)>=3:
			t = self[-1]
			self[-1] = self[-2]
			self[-2] = t
			t = self[-2]
			self[-3] = self[-3]
			self[-3] = t
