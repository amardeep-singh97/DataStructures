#structure of single node of a linked list
class Node:
	def __init__(self,data,next_val):
		#self.data used to store the actual element 
		self.data = data
		#Pointer value to next node
		self.next = next_val

class createLinkedList:
	def __init__(self):
		self.head = None

	def insertion_at_start(self,value):
		node = Node(value,self.head)
		self.head = node


	def insertion_at_end(self,value):
		if self.head == None:
			self.head = Node(value,None)

		itr = self.head
		while itr.next:
			itr = itr.next

		itr.next = Node(value,None)

	def insert_list(self, data_list,orientation='f'):
		#creating new linked list if linked list is empty 
		if self.head == None:
			if orientation == 'f':
				for value in data_list:
					self.insertion_at_end(value)
			elif orientation == 'b':
				for value in data_list:
					self.insertion_at_start(value)
		else:
			itr = self.head
			while itr.next:
				itr = itr.next
			for value in data_list:
				itr.next = Node(value,None)
				itr = itr.next

	def get_length(self):
		length = 0

		if self.head is None:
			return 0

		itr = self.head
		while itr:
			length += 1
			itr = itr.next
		return length

	def remove_at_index(self,index):

		if index < 0 or index >= self.get_length():
			raise Exception("index is invalid")
		elif index == 0:
			self.head = self.head.next
		else:
			count = 0
			itr = self.head
			while itr:
				if count == index-1:
					itr.next = itr.next.next
					break
				itr = itr.next
				count+=1

	def insert_at_index(self,index,value):
		if index < 0 or index >= self.get_length():
			raise Exception("Invalid index")
		elif index == 0:
			self.insertion_at_start(value)
		else:
			count = 0
			itr = self.head
			while itr:
				if count == index-1:
					itr.next = Node(value,itr.next)
				itr = itr.next
				count +=1

	def insert_after_value(self,find_value,insert_value):
		itr = self.head
		while itr:
			if itr.data == find_value:
				print("Data Found {0}".format(itr.data))
				itr.next = Node(insert_value,itr.next)
				break
			itr = itr.next

	def remove_by_value(self,value):
		itr = self.head
		count = 0
		while itr:
			if itr.data == value:
				self.remove_at_index(count)
				break
			itr = itr.next
			count += 1 

	def print(self):
		if self.head is None:
			print("Linked list is empty")
			return 
		itr = self.head
		while itr:
			print(itr.data)
			itr = itr.next

if __name__ == '__main__':
	ll = createLinkedList()

	ll.insert_list([8,6,8,12,44],'b')
	ll.remove_by_value(6)
	ll.print()
	print("Length of linked list is {0}".format(ll.get_length()))