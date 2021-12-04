class Node:
    """
    A data structure containing a value (of any type) and another node 
    (that will be referred as next).

    ...
    Attributes
    ----------
    value : int
        Integer value
    
    Methods
    -------

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
        Node object. The first node in chain
    
    Methods
    -------
    append(value=4)
        Adds new value to LinkedList
    remove(value=5)
        Removed the specified value (Node) from LinkedList
    show()
        Displays complete LinkedList
    """
    def __init__(self, head=Node()):
        self.head = head
    
    def append(self, value):
        """
        Adds new value to LinkedList

        Parameters
        ----------
        value : int
            Value to be added to LinkedList
        """
        if self.head.value == None:
            self.head.value = value
        else:
            temp = Node(None, self.head)
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
        if self.head.value == None:
            print("Linked List is empty.")
        elif self.head.value == value:
            self.head = self.head.next
        else:
            temp = self.head
            while(temp.next != None):
                if (temp.next.value == value):
                    temp.next = temp.next.next
                    break
                temp = temp.next
            else:
                print("{} is not in the Linked List.".format(value))

    def show(self):
        """
        Displays complete LinkedList
        """
        if self.head.value == None:
            print("Linked List is empty.")
        else:
            print("The Linked List:")
            temp = Node(None, self.head)
            while(temp.next!=None):
                temp = temp.next
                print(temp.value, end='->')
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
        n = Node(6)
        ll = LinkedList(n)
        k = Node(36)
        ll.head.next = k
        ll.append(87)
        ll.append(76)
        ll.remove(6)
        ll.remove(76)
        ll.remove(7)
        ll.show()
        ll2 = LinkedList()
        ll2.show()
        ll2.remove(9)

driver = Driver()
driver.execute()