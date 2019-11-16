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

def to_pol(s):
	res = ''
	s = '( ' + s +' )'
	ops = Stack()
	prs = {'+' : 2, '-' : 2, '*' : 3, '/' : 3, '%' : 3, '(' : 1}
	for i in s.split():
		if i[-1].isdigit():
			res += i + ' '
		elif i == '(':
			ops.put(i)
		elif i == ')':
			t = ops.pull()
			while t != '(':
				res += t + ' '
				t = ops.pull()
		else:
			try:
				t = ops[-1]
				while prs[t]>=prs[i] and t != '(':
					res += ops.pull() + ' '
					t = ops[-1]
				ops.put(i)
			except:
				pass
	return res
print(to_pol('( ( 2 + 4 ) * 7 - 3 * 5 ) / ( 2 + 7 ) * 4'))
print(to_pol('( 2 + 3 ) * 5'))
print(to_pol('3 * 2 - 5'))
print(to_pol(input()))
