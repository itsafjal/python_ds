class Node(object):
	def __init__(self, data=None, next_node =None):
		self.data = data
		self.next = next_node



def print_list(head):
	if(head==None):
		print("empty list")
		return
	else:
		current = head
		while(current.next!=None):
			print(current.data)
			current = current.next
	return head

Node1 = Node(1)
Node2 = Node(2)
Node3 = Node(3)
Node3.next = None
head = Node1
print(Node3.data)
print_list(head)
