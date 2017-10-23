class Node:
    def __init__(self, value): 
        self.__value = value
        self.__right = None
        self.__left = None

    def getValue(self):
        return self.__value

    def getLeft(self):
        return self.__left
    def getRight(self):
        return self.__right

    def setRight(self, right):
        self.__right = right
    def setLeft(self, left):
        self.__left = left

class Bintree:
    def __init__(self, root = None):
        self.root = root
        self.counter = 0

    def put(self,newvalue):
        if self.root == None: #Om roten är tom
            self.root = Node(newvalue)
            #print(self.root)
        else: 
            putta(self.root,newvalue) #Lägg till ny nod

    def __contains__(self,value):
        #print ("Value: "+value)
        if self.root == None: #Om trädet är tomt
            return False
        else: 
            a = finns(self.root,value)
            #print ("Return: "+str(a))
            if a is None: #Om finns returnerar none är svaret false. 
                return False
            elif a is True: 
                return True


    def write(self):
        skriv(self.root)
        print("\n")


def putta(nod, newvalue): 
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
     

def finns(nod, value): 
    if value == nod.getValue(): #Om värdet hittas
        return True
    elif value < nod.getValue(): #Om värdet är mindre än noden: 
        if nod.getLeft() is not None:
            return finns(nod.getLeft(), value) # Gör om Finns åt vänster (gå ett steg ner åt vänster)
    elif value > nod.getValue(): 
        if nod.getRight() is not None:
            return finns(nod.getRight(), value)

def skriv(nod):
    if nod != None: 
        skriv(nod.getLeft())
        print (nod.getValue())
        skriv(nod.getRight())