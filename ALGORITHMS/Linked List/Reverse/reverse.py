# Python program to reverse a linked list
# Time Complexity : O(n)
# Space Complexity : O(1)

# Node class


class Node:

	# Constructor to initialize the node object
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None

	# Function to reverse the linked list
	def reverse(self):
		prev = None
		current = self.head
		while(current is not None):
			next = current.next
			current.next = prev
			prev = current
			current = next
		self.head = prev

	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node


	def printList(self):
		temp = self.head
		while(temp):
			print temp.data,
			temp = temp.next



llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)

print "Given Linked List"
llist.printList()
llist.reverse()
print "\nReversed Linked List"
llist.printList()


