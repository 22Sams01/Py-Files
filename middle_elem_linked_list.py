#find middle elem of linked list
# if even -> 2nd middle element should b o/p

class ListNode:
	"""docstring for ListNode"""
	def __init__(self, value,next=None):
		super(ListNode, self).__init__()
		self.value = value
		self.next=next

class Nod:
	def LL(self,curr):
		while (curr!=None):
			print("{}->".format(curr.value),end='')
			curr=curr.next
		print("None")

	def finlen(self,curr):
		lm=0
		while(curr!=None):
			lm+=1
			curr=curr.next
		print("LENGTH>>>",lm)
		return lm

	def middle(self,curr,leng):
		if curr!=None:
			a=leng//2
		while a !=0:
			curr=curr.next
			a-=1
		print("MIDDLE ELEMENT IS",curr.value)

node1=ListNode("1")
node2=ListNode("2")
node3=ListNode("3")
node4=ListNode("4")
# node5=ListNode("5")
node1.next=node2
node2.next=node3
node3.next=node4
# node4.next=node5
curr=node1
nod=Nod()
nod.LL(curr)
lm=nod.finlen(curr)
nod.middle(curr,lm)