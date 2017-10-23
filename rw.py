

graph = {}

class Station:
	def __init__(a=None, b=None, c=None):
		self.a = a
		self.b = b
		self.c = c
	def connect(switch, station): #Tar in en switch och ansluter denna till en annan stations switch. 
		if switch == 'a': 
			self.a = station
		elif switch == 'b': 
			self.b = station
		elif switch == 'c': 
			self.c = station


def create_stations(N):
	for i in N:
		graph[i] = Station()

def set_connection(C1, C2):
	graph[int(C1[0])].connect(graph(C1[1],int(C2[0])))
	graph[int(C2[0])].connect(graph(C2[1],int(C1[0])))

def read_input(): 
	first = True
	with open "inputfile.txt" as stdin:
		for row in stdin: #sys.stdin:
			if first: 
				N = row[0]+row[1]
				M = row[3]+row[4]
				first = False
			else: 
				set_connection(str(row[0]+row[1]), str(row[3]+row[4]))
				
