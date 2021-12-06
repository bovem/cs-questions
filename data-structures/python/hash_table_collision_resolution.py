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
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node

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
        self.head = None
    
    def insert(self, value):
        """
        Adds new value to LinkedList

        Parameters
        ----------
        value : int
            Value to be added to LinkedList
        """
        temp = Node(next_node=self.head)
        if(self.head==None):
            self.head = Node(value)
        while(temp.next!=None):
            temp = temp.next
        new_node = Node(value)
        temp.next = new_node
    
    def remove(self, value):
        """
        Removes value from LinkedList

        Parameters
        ----------
        value : int
            Value to be removed from LinkedList
        """
        temp = Node(next_node=self.head)
        if(self.head.value == value):
            self.head = self.head.next
        else:
            while(temp.next!=None):
                if(temp.next.value==value):
                    temp.next = temp.next.next
                temp = temp.next
    
    def search(self, value):
        """
        Searches value in LinkedList

        Parameters
        ----------
        value : int
            Value to be searched from LinkedList
        
        Returns
        -------
        found: bool
            Boolean representing presence of value
        """
        found = False
        temp = Node(next_node=self.head)
        while(temp.next!=None):
            if(temp.next.value==value):
                found = True
                break
            temp = temp.next
        return found
    
    def show(self):
        """
        Returns a string containing complete LinkedList

        Returns
        ----------
        return_string : str
            String with contents of LinkedList
        """
        return_string=''
        temp = Node(next_node=self.head)
        while(temp.next!=None):
            temp = temp.next
            return_string+="{}->".format(temp.value)
        return return_string

def normal_hash(value):
    """
    Returns a hash value

    Returns
    ----------
    hash_val : int
        Hash value calculated from given integer
    """
    return value%7

class HashTable:
    """
    A data structure created using an array of LinkedLists.
    Used for faster access time.
    Provides O(1) lookup.

    Implemented with collision resolution methods:
    - Chaining Linked List
    - Linear Probing
    - Quadratic Probing
    - Chaning Binary Search Tree

    ...
    Attributes
    ----------
    table : list(LinkedList)
        List of LinkedList objects.
    collision_resolution_method: str
        Specifies the method used for collision resolution.
    linear_probing_factor: int
        Increment value for index in case of collision.
    
    Methods
    -------
    insert(value=4)
        Adds new value to HashTable based on collision_resolution_method
        specified
    remove(value=5)
        Removed the specified value (Node) from Table based on 
        collision_resolution_method specified
    search(value=2)
        Searches specified value in HashTable and
        returns True if present based on collision_resolution_method
        specified
    insert_linear_probing(value=2)
        Inserts new value to hash table using linear probing method for
        handling collisions.
    remove_linear_probing(value=3)
        Removed specified value from hash table using linear probing
        method for handling collisions.
    search_linear_probing(value=4)
        Searches for specified value in hash table and returns a boolean
        specifying its presence.
        Collisions are handled by linear probing method.
    insert_linked_list(value=2)
        Inserts new value to hash table using chaining linked list
        method for handling collisions.
    remove_linked_list(value=3)
        Removed specified value from hash table using chaining linked
        list method for handling collisions.
    search_linked_list(value=4)
        Searches for specified value in hash table and returns a boolean
        specifying its presence.
        Collisions are handled by chaining linked list method.
    insert_quadratic_probing(value=2)
        Inserts new value to hash table using quadratic probing method for
        handling collisions.
    remove_quadratic_probing(value=3)
        Removed specified value from hash table using quadratic probing
        method for handling collisions.
    search_quadratic_probing(value=4)
        Searches for specified value in hash table and returns a boolean
        specifying its presence.
        Collisions are handled by quadratic probing method.
    insert_binary_search_tree(value=2)
        Inserts new value to hash table using binary search treefor
        handling collisions.
    remove_binary_search_tree(value=3)
        Removed specified value from hash table using binary search 
        tree for handling collisions.
    search_binary_search_tree(value=4)
        Searches for specified value in hash table and returns a boolean
        specifying its presence.
        Collisions are handled by binary_search_tree.
    show()
        Returns a string containing complete HashTable
    """
    def __init__(self, size=100):
        self.table = [None]*size
        self.collision_resolution_method = "linear_probing"
        self.linear_probing_factor = 5
    
    def insert(self, value):
        """
        Adds new value to HashTable
        Triggers insert method based on collision resolution method
        specified.

        Parameters
        ----------
        value : int
            Value to be added to HashTable
        """
        if(self.collision_resolution_method=="linear_probing"):
            self.insert_linear_probing(value)
        elif(self.collision_resolution_method=="linked_list"):
            self.insert_linked_list(value)
        elif(self.collision_resolution_method=="quadratic_probing"):
            self.insert_quadratic_probing(value)
        elif(self.collision_resolution_method=="binary_search_tree"):
            self.insert_binary_search_tree(value)
    
    def remove(self, value):
        """
        Removed specified value from HashTable
        Triggers remove method based on collision resolution method
        specified.

        Parameters
        ----------
        value : int
            Value to be removed from HashTable
        """
        if(self.collision_resolution_method=="linear_probing"):
            self.remove_linear_probing(value)
        elif(self.collision_resolution_method=="linked_list"):
            self.remove_linked_list(value)
        elif(self.collision_resolution_method=="quadratic_probing"):
            self.remove_quadratic_probing(value)
        elif(self.collision_resolution_method=="binary_search_tree"):
            self.remove_binary_search_tree(value)
    
    def search(self, value):
        """
        Searches for value in HashTable
        Triggers search method based on collision resolution method
        specified.

        Parameters
        ----------
        value : int
            Value to be searched in HashTable
        
        Returns
        -------
        found: bool
            Boolean value specifiying presence of specified value in 
            HashTable
        """
        if(self.collision_resolution_method=="linear_probing"):
            return self.search_linear_probing(value)
        elif(self.collision_resolution_method=="linked_list"):
            return self.search_linked_list(value)
        elif(self.collision_resolution_method=="quadratic_probing"):
            return self.search_quadratic_probing(value)
        elif(self.collision_resolution_method=="binary_search_tree"):
            return self.search_binary_search_tree(value)
    
    def insert_linear_probing(self, value):
        """
        Adds new value to HashTable
        Triggered from insert() method.
        Inserts value using Linear Probing method for collision
        resolution.

        Parameters
        ----------
        value : int
            Value to be added to HashTable
        """
        hash_val = normal_hash(value)
        index = hash_val%10

        while index < len(self.table):
            if self.table[index]==None:
                ll = LinkedList()
                self.table[index] = ll
                self.table[index].insert(value)
                break
            
            elif self.table[index].search(value):
                index = index + self.linear_probing_factor
            
            else:
                self.table[index].insert(value)
                break
    
    def search_linear_probing(self, value):
        """
        Searches for specified value in HashTable
        Triggered from search() method.
        Searches value using Linear Probing method for collision
        resolution.

        Parameters
        ----------
        value : int
            Value to be searched in HashTable
        
        Returns
        -------
        found: bool
            Boolean value specifiying presence of specified value in 
            HashTable
        """
        hash_val = normal_hash(value)
        index = hash_val%10
        found = False

        while index < len(self.table):
            if self.table[index] == None:
                break
            elif self.table[index].search(value):
                found = True
                break
            else:
                index = index + self.linear_probing_factor
        return found

    def remove_linear_probing(self, value):
        """
        Removes specified value from HashTable
        Triggered from remove() method.
        Removes value using Linear Probing method for collision
        resolution.

        Parameters
        ----------
        value : int
            Value to be removed from HashTable
        """    
        hash_val = normal_hash(value)
        index = hash_val%10

        while index < len(self.table):
            if self.table[index] == None:
                break
            elif self.table[index].search(value):
                self.table[index].remove(value)
                break
            else:
                index = index + self.linear_probing_factor
    
    def insert_linked_list(self, value):
        """
        Adds new value to HashTable
        Triggered from insert() method.
        Inserts value using Chaining Linked List method for collision
        resolution.

        Parameters
        ----------
        value : int
            Value to be added to HashTable
        """   
        hash_val = normal_hash(value)
        index = hash_val%10

        if self.table[index]==None:
            ll = LinkedList()
            self.table[index] = ll
        
        self.table[index].insert(value)
    
    def remove_linked_list(self, value):
        """
        Removes specified value from HashTable
        Triggered from remove() method.
        Removes value using Chaining Linked List method for collision
        resolution.

        Parameters
        ----------
        value : int
            Value to be removed from HashTable
        """    
        hash_val = normal_hash(value)
        index = hash_val%10

        if self.table[index] == None:
            print("{} not present in hash table".format(value))
        else:
            self.table[index].remove(value)

    def search_linked_list(self, value):
        """
        Searches for specified value in HashTable
        Triggered from search() method.
        Searches value using Chaining Linked List method for collision
        resolution.

        Parameters
        ----------
        value : int
            Value to be searched in HashTable
        
        Returns
        -------
        found: bool
            Boolean value specifiying presence of specified value in 
            HashTable
        """
        hash_val = normal_hash(value)
        index = hash_val%10
        found = False

        if self.table[index]!=None:
            found = self.table[index].search(value)
        
        return found
            
    def insert_quadratic_probing(self, value):
        """
        Adds new value to HashTable
        Triggered from insert() method.
        Inserts value using Quadratic Probing method for collision
        resolution.

        Parameters
        ----------
        value : int
            Value to be added to HashTable
        """
        hash_val = normal_hash(value)
        index = hash_val%10

        while index < len(self.table):
            if self.table[index]==None:
                ll = LinkedList()
                self.table[index] = ll
                self.table[index].insert(value)
                break

            elif self.table[index].search(value):
                index = index**2

            else:
                self.table[index].insert(value)
                break
    
    def remove_quadratic_probing(self, value):
        """
        Removes specified value from HashTable
        Triggered from remove() method.
        Removes value using Quadratic Probing method for collision
        resolution.

        Parameters
        ----------
        value : int
            Value to be removed from HashTable
        """    
        hash_val = normal_hash(value)
        index = hash_val%10

        while index < len(self.table):
            if self.table[index]==None:
                break
            elif self.table[index].search(value):
                self.table[index].remove(value)
                break
            else:
                index = index**2
        
    
    def search_quadratic_probing(self, value):
        """
        Searches for specified value in HashTable
        Triggered from search() method.
        Searches value using Quadratic Probing method for collision
        resolution.

        Parameters
        ----------
        value : int
            Value to be searched in HashTable
        
        Returns
        -------
        found: bool
            Boolean value specifiying presence of specified value in 
            HashTable
        """
        hash_val = normal_hash(value)
        index = hash_val%10
        found = False

        while index < len(self.table):
            if self.table[index]==None:
                break
            elif self.table[index].search(value):
                found=True
                break
            else:
                index = index**2
        
        return found
    
    def insert_binary_search_tree(self, value):
        """
        Adds new value to HashTable
        Triggered from insert() method.
        Inserts value using Binary Search Tree for collision
        resolution.

        Parameters
        ----------
        value : int
            Value to be added to HashTable
        """
        pass
    
    def remove_binary_search_tree(self, value):
        """
        Removes specified value from HashTable
        Triggered from remove() method.
        Removes value using Binary Search Tree for collision
        resolution.

        Parameters
        ----------
        value : int
            Value to be removed from HashTable
        """    
        pass
    
    def search_binary_search_tree(self, value):
        """
        Searches for specified value in HashTable
        Triggered from search() method.
        Searches value using Binary Search Tree for collision
        resolution.

        Parameters
        ----------
        value : int
            Value to be searched in HashTable
        
        Returns
        -------
        found: bool
            Boolean value specifiying presence of specified value in 
            HashTable
        """
        pass

    def show(self):
        """
        Displays complete HashTable
        """
        for i in range(len(self.table)):
            if self.table[i] == None:
                 print("{}   {}".format(i, self.table[i]))
            else:
                 print("{}   {}".format(i, self.table[i].show()))

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
        #hash_table.collision_resolution_method = "linear_probing"
        #hash_table.collision_resolution_method = "linked_list"
        #hash_table.collision_resolution_method = "quadratic_probing"
        hash_table.insert(2)
        hash_table.insert(3)
        hash_table.insert(5)
        hash_table.insert(5)
        hash_table.remove(3)
        hash_table.insert(3)
        hash_table.insert(6)
        hash_table.insert(12)
        hash_table.insert(12)
        print(hash_table.search(12))
        hash_table.show()

driver = Driver()
driver.execute()