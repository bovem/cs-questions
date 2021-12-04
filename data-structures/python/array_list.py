class ArrayList:
    """
    A dynamically resizing array-like data structure.
    Initial size is 1.
    Doubles in size everytime array is full.

    ...
    Attributes
    ----------
    array : list(int)
        Array containing elements of ArrayList.
    size: int
        Size of Array containing elements of ArrayList.
    
    Methods
    -------
    insert(value=4)
        Adds new value to ArrayList
    remove(value=5)
        Removed the specified value from ArrayList
    get_array()
        Returns array without None values
    """
    def __init__(self, size=1):
        self.array = [None]*size
        self.size = size
    
    def insert(self, value):
        """
        Adds new value to ArrayList
        Resizes array to double if there is no space.

        Parameters
        ----------
        value : int
            Value to be added to ArrayList
        """
        if(self.array[-1]!=None):
            new_array = [None]*(2*self.size)
            for i in range(self.size):
                new_array[i] = self.array[i]
            self.array = new_array
            self.size = 2*self.size
        for i in range(self.size):
            if self.array[i] == None:
                self.array[i] = value
                break
    
    def remove(self, value):
        """
        Removes value from ArrayList

        Parameters
        ----------
        value : int
            Value to be removed from ArrayList
        """
        for i in range(self.size):
            if(self.array[i]==value):
                self.array[i]=None
                break
    
    def get_array(self):
        """
        Returns array without None elements

        Returns
        -------
        return_array : list(int)
            Array without None values
        """
        return_array = []
        for i in range(self.size):
            if(self.array[i]!=None):
                return_array.append(self.array[i])
        return(return_array)

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
        array_list = ArrayList()
        array_list.insert(1)
        array_list.insert(32)
        array_list.insert(5)
        array_list.remove(32)
        print(array_list.array)
        print(array_list.get_array())

driver = Driver()
driver.execute()