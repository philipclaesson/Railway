class Node:
    def __init__(self, A): 
        self.A = A
        self.B = None
        self.C = None

    def getA(self):
        return self.A
    def getB(self):
        return self.B
    def getC(self):
        return self.C

    def setConnection(self, connection, node):
        if connection == 'A': 
            self.A = node
        elif connection == 'B':
            self.B = node
        elif connection == 'C': 
            self.C = node
        else: 
            raise TypeError("Wrong type in setConnection. ")

class Graph: 
    def __init__(self, root): 
        self.root = root #startstationen

    def put(self,newvalue):
        if self.root == None: #Om roten är tom
            self.root = Node(newvalue)
        else: 
            putta(self.root,newvalue) #Lägg till ny nod

def putter(nod, newvalue): #Recursive put function
    if newvalue < nod.getValue(): #Om vi ska gå åt vänster
        if nod.getLeft() is not None: #Kontrollera om noden har något till vänster
            putta(nod.getLeft(), newvalue) # Om det finns något till vänster så gör om putta()
        else: 
            nod.setLeft(Node(newvalue)) # Om det är tomt till vänster: lägg till ny nod till vänster
    else: #Vi ska gå åt höger
        if nod.getRight() is not None: #Om noden till höger inte är tom
            putta(nod.getRight(), newvalue) #Starta om putta
        else: #Om noden är tom
            nod.setRight(Node(newvalue)) #Skapa nytt nodobjekt

