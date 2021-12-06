class Node:
    """
    A data structure containing a value (of any type) and another node 
    (that will be referred as next).

    ...
    Attributes
    ----------
    value : int
        Integer value
    next: Node
        Next Node in chain
    """
    def __init__(self, value=None, nextNode=None):
        self.value = value
        self.next = nextNode
    
class LinkedList:
    """
    A data structure created by chaining nodes.

    ...
    Attributes
    ----------
    head : Node
        Node object. The first node in the chain.
    
    Methods
    -------
    insert(value=4)
        Adds new value to LinkedList
    remove(value=5)
        Removed the specified value (Node) from LinkedList
    search(value=2)
        Searches specified value in LinkedList and
        returns True if present.
    show()
        Returns a string containing complete LinkedList
    """
    def __init__(self, head=None):
        self.head = head
    
    def insert(self, value):
        """
        Adds new value to LinkedList

        Parameters
        ----------
        value : int
            Value to be added to LinkedList
        """
        if(self.head==None):
            self.head = Node(value)
        else:
            temp = Node(nextNode=self.head)
            while(temp.next!=None):
                temp = temp.next
            temp.next = Node(value)
    
    def remove(self, value):
        """
        Removes value from LinkedList

        Parameters
        ----------
        value : int
            Value to be removed from LinkedList
        """
        if(self.head==None):
            print("LinkedList empty")
        elif(self.head.value == value):
            self.head = self.head.next
        else:
            temp = Node(nextNode=self.head)
            while(temp.next.next!=None):
                temp = temp.next
                if(temp.next.value == value):
                    temp.next = temp.next.next
    
    def search(self, value):
        """
        Searches value in LinkedList

        Parameters
        ----------
        value : int
            Value to be searched from LinkedList
        
        Returns
        -------
        isPresent: bool
            Boolean representing presence of value
        """
        if(self.head.value==value):
            return True
        else:
            temp = Node(nextNode=self.head)
            while(temp.next.next!=None):
                temp = temp.next
                if(temp.next.value==value):
                    return True
            return False
    
    def show(self):
        """
        Returns a string containing complete LinkedList

        Returns
        ----------
        return_string : str
            String with contents of LinkedList
        """
        temp = Node(nextNode=self.head)
        return_string = ""
        while(temp.next!=None):
            temp = temp.next
            return_string = return_string + str(temp.value) + "->"
        return(return_string)
            
def calculate_hash(value):
    """
    Returns a hash value

    Returns
    ----------
    hash_val : int
        Hash value calculated from given integer
    """
    return(value%7)

class HashTable:
    """
    A data structure created using an array of LinkedLists.
    Used for faster access time.
    Provides O(1) lookup.

    ...
    Attributes
    ----------
    table : list(LinkedList)
        List of LinkedList objects.
    
    Methods
    -------
    insert(value=4)
        Adds new value to HashTable
    remove(value=5)
        Removed the specified value (Node) from Table
    search(value=2)
        Searches specified value in HashTable and
        returns True if present.
    show()
        Returns a string containing complete HashTable
    """
    def __init__(self):
        self.table = [None]*100
    
    def insert(self, value):
        """
        Adds new value to HashTable

        Parameters
        ----------
        value : int
            Value to be added to HashTable
        """
        hash_val = calculate_hash(value)
        table_index = hash_val%100
        if(self.table[table_index]==None):
            linked_list = LinkedList()
            self.table[table_index]=linked_list
        self.table[table_index].insert(value)
    
    def remove(self, value):
        """
        Removes value from HashTable

        Parameters
        ----------
        value : int
            Value to be removed from HashTable
        """
        hash_val = calculate_hash(value)
        table_index = hash_val%100
        if(self.table[table_index]==None):
            print("Empty")
        elif(self.table[table_index].head.next==None):
            self.table[table_index] = None
        else:
            self.table[table_index].remove(value)
    
    def search(self, value):
        """
        Searches for value in HashTable

        Parameters
        ----------
        value : int
            Value to be searched in HashTable
        """
        hash_val = calculate_hash(value)
        table_index = hash_val%100
        search_space = self.table[table_index]

        if(search_space==None):
            print("Empty")
        else:
            if(search_space.head == None):
                return(False)
            else:
                return(search_space.search(value))
    
    def show(self):
        """
        Displays complete HashTable
        """
        for i in range(len(self.table)):
            if(self.table[i]==None):
                print("{}   {}".format(i, self.table[i]))
            else:
                print("{}   {}".format(i, self.table[i].show()))
            print()

class Driver:
    """
    Driver code

    ...
    Methods
    -------
    execute()
        Code used for testing
    """
    def __init__(self):
        pass
    
    def execute(self):
        hash_table = HashTable()
        hash_table.insert(2)
        hash_table.insert(3)
        hash_table.insert(5)
        hash_table.insert(0)
        hash_table.remove(3)
        print(hash_table.search(3))
        print(hash_table.search(0))
        hash_table.show()

driver = Driver()
driver.execute()