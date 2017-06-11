
class Node(object):
	def __init__(self, data=None, next_node=None):
	   self.data = data
	   self.next = next_node

def print_list(head):
    if head is not None:
        current = head
        while(current!=None):
            print(current.data)
            current = current.next

def insert_node(head, data):
	current = head
	if current==None:
		current = Node(data)
		head = current
	else:
		while(current.next!=None):
			current = current.next
		current.next = Node(data)
	return head

if __name__ == "__main__":
	head = None
	head = insert_node(head, 1)
	head = insert_node(head, 2)
	print_list(head)
