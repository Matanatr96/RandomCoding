class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

	def append(self, data):
		temp = Node(data)
		while (self.next):
			self = self.next
		self.next = temp;

	def print(self):
		while(self):
			print(self.data)
			self = self.next

	def reverse(self):
		prev = None
		current = self

		while(current):
			nxt = current.next
			current.next = prev
			prev = current
			current = nxt

		return prev


head = Node(1)
head.append(2)
head.append(3)
head.append(4)

head2 = Node(5)
head2.append(6)
head2.append(7)
head2.append(8)

rversed = head.reverse()
rversed.print()