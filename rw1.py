from LinkedQ import LinkedQ
import timeit

class Switch:
	def __init__(self):
		self.a = None
		self.b = None
		self.c = None

		self.state = "B"

		self.checked_positive = False
		self.checked_negative = False

		self.positive_parent = None

	def change_state(char):
		self.state = char

	def set_connection(self, connection, other):
		"""binder en connection till ett annat objekt"""
		if connection == "A": 
			self.a = other
		elif connection == "B":
			self.b = other
		elif connection == "C": 
			self.c = other
		else: 
			raise TypeError("Ej A/B/C in i set_connection")

	def get_connection(self, child, parent=None): 
		if self.a == child: 
			if self.b == parent:
				return "B"
			elif self.c == parent:
				return "C" 
		if self.b == child:
			return "B" 
		if self.c == child:
			return "C" 
		else: 
			raise TypeError("Ej A/B/C in i get_connection")

	def set_state(self, child, parent=None):
		if self.a == child: 
			if self.b == parent:
				self.state = "B"
			elif self.c == parent:
				self.state = "C" 
		elif self.b == child:
			self.state = "B" 
		elif self.c == child:
			self.state = "C" 
		else: 
			raise TypeError("Ej A/B/C in i set state")


	def get_neighbour(self, connection):
		if connection == "a":
			return self.a
		elif connection == "b":
			return self.b
		elif connection == "c":
			return self.c


	def get_direction(self, other):
		"""checks the direction going from other to self"""
		if other == self.b or other == self.c: 
			return False
		elif other == self.a: 
			return True
		else:
			raise TypeError("Other did not match any neighbor in get_direction")

	def get_parent(self, child):
		"""checks parent going from child to self"""
		if child == self.a:
			return self.positive_parent
		if child == self.b or child == self.c:
			return self.a


	def is_checked(self, direction):
		if direction: 
			return self.checked_positive
		else: 
			return self.checked_negative

	def set_checked(self, direction):
		if direction: 
			self.checked_positive = True
		else: 
			self.checked_negative = True

	def check_positive_parent(self, parent): 
		"""If this is the first time self is used in positive direction, set parent to positive parent. """
		if self.positive_parent is None: 
			if parent == self.b or parent == self.c: 
				self.positive_parent = parent


def breadth_first_search(switches): 
	q = LinkedQ() #Takes Switch and its parent
	success = False
	switches[0].b.check_positive_parent(switches[0]) #Kollar om this switch is a positive parent
	switches[0].c.check_positive_parent(switches[0])
	q.enqueue((switches[0].b, switches[0])) #Queues neighbours to the first switch
	q.enqueue((switches[0].c, switches[0]))
	while not q.isEmpty() and not success:
		next = q.dequeue()
		this_switch, previous_switch = next[0], next[1]
		direction = this_switch.get_direction(previous_switch)
		if this_switch == switches[0] and direction is True: 
			success = True
		elif not this_switch.is_checked(direction): #Om denna switch i denna riktning ej redan kollats. 
			if direction is True: #Om positiv riktning
				if this_switch.b is not None: #om empty do nothing
					this_switch.b.check_positive_parent(this_switch) #Kollar om this switch is positiv parent
					q.enqueue((this_switch.b, this_switch)) #runt towards b or c
				if this_switch.c is not None: #if empty do nothing
					this_switch.c.check_positive_parent(this_switch)
					q.enqueue((this_switch.c, this_switch))
			elif direction is False: #Om negativ riktning
				if this_switch.a is not None:
					this_switch.a.check_positive_parent(this_switch)
					q.enqueue((this_switch.a, this_switch)) #walk towards a
			this_switch.set_checked(direction)

	if success: 
		set_states(switches, previous_switch, this_switch, previous_switch)
		#out = get_output(switches)
		kortid = timeit.timeit(stmt = lambda: get_output(switches), number = 15000)
		print("Output tog", round(kortid, 4) , "sekunder")
		#print (out)
	else: 
		print ("Impossible")



def set_states(switches, switch, child, previous_switch): #Parent = den som kommer fore en switch. child = den som kommer efter
	if switch == switches[0] and child != previous_switch: #om startswitchen och child inte ar den man kom from
		return switch.get_connection(child)
	else: 
		parent = switch.get_parent(child)
		switch.set_state(child, parent)
		set_states(switches, parent, switch, previous_switch)

def get_output(switches): 
	out = ""
	for switch in switches: 
		out += switch.state
	return (out)

def set_switches(switches, C1, C2): 
	"""funktion som sets in switchar (anropar set_connection)
	Tar in C1 och C2 pa formen "1234A" eller "1B" med godtyckligt antal siffror och en bokstav, A, B eller C. """
	char1, char2 = C1[-1], C2[-1] #Plockar ut bokstaverna
	num1, num2 = int(C1[:-1]), int(C2[:-1]) #plockar fram siffrorna
	switches[num1-1].set_connection(char1, switches[num2-1])
	switches[num2-1].set_connection(char2, switches[num1-1]) #Switchobjekt.setconnection(bokstav, annat switchobjekt)

def read_testfile():
	with open("inputfile.txt", "r") as songdata: #, encoding="utf-8"
		firstline = songdata.readline()
		M, N = firstline.split()
		switches = [Switch() for i in range(int(M))] #Skapar en lista av M switchar. 
		for line in songdata:
			linelist = line.split()
			set_switches(switches, linelist[0],linelist[1])
	breadth_first_search(switches)

	#tidtag
	kortid = timeit.timeit(stmt = lambda: breadth_first_search(switches), number = 1)
	print("Bfs tog", round(kortid, 4) , "sekunder")

def read_input(): #korning i kattis. 
	for row in sys.stdin:
		if row == "#":
			break
		else:
			try:
				syntax_input(row)
			except Syntax_fel as message:
				print(message)


def tidtagare(): 
	kortid = timeit.timeit(stmt = lambda: read_testfile(), number = 1)
	print("Programmet tog", round(kortid, 4) , "sekunder")
	print ("Slut")



read_testfile()
#tidtagare()



