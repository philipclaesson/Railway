class Node():
	def __init__(self, value = None, next = None): 
		self.__value = value
		self.__next = next

	def getValue(self):
		return self.__value

	def getNext(self):
		return self.__next

	def setNext(self, next):
		self.__next = next
		
class LinkedQ():
	def __init__(self):
		self.first = None
		self.last = None

	def enqueue(self, value):
		#self.syntaxkoll(value)

		new_node = Node(value = value) # Skapar ny node
		if self.isEmpty():
			self.first = new_node	# Om kon ar tom ar den nya noden forst. Det finns ingen nod sist i kon som kan ges ett next-varde. 
		else:
			self.last.setNext(new_node) # Givet att kon inte ar tom: sista noden i listan far veta att new_node ar dess next. 
		self.last = new_node # Nya noden ar sist i listan
		

	def dequeue(self):
		if not self.isEmpty():
			out_node = self.first #Tar ut forsta noden i listan. 
			self.first = out_node.getNext() #Satter nasta nod som forst i listan. 
			return out_node.getValue() #Returnerar det varde som plockats ut. 
		else: 
			raise Exception

	def isEmpty(self):
		return self.first == None

	def peek(self): 
		return self.first.getValue()