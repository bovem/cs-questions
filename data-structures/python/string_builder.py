class StringBuilder:
    """
    A dynamically resizing string-like data structure.
    Initial size is 1.
    Doubles in size everytime string is full.

    ...
    Attributes
    ----------
    string_array : list(char)
        Array containing characters of StringBuilder
    size: int
        Size of Array containing characters of StringBuilder
    
    Methods
    -------
    insert(value='a)
        Adds new character to StringBuilder
    remove(value='c)
        Removed the specified character from StringBuilder
    get_string()
        Returns string without None values
    """
    def __init__(self, size=1):
        self.string_array = [None]*size
        self.size = size
    
    def insert(self, char_value):
        """
        Adds new character to string
        Resizes string array to double if there is no space.

        Parameters
        ----------
        value : char
            Character to be added to StringBuilder
        """
        if(self.string_array[-1]!=None):
            new_string_array = [None]*(2*self.size)
            for i in range(self.size):
                new_string_array[i] = self.string_array[i]
            self.string_array = new_string_array
            self.size = (2*self.size)
        for i in range(self.size):
            if(self.string_array[i]==None):
                self.string_array[i] = char_value
                break
    
    def remove(self, char_value):
        """
        Removes character from StringBuilder

        Parameters
        ----------
        value : char
            Character to be removed from StringBuilder
        """
        for i in range(self.size):
            if(self.string_array[i]==char_value):
                self.string_array[i]='_'
    
    def get_string(self):
        """
        Returns string without None elements

        Returns
        -------
        return_string_array : list(char)
            String without None values
        """
        return_string_array = []
        for i in range(self.size):
            if(self.string_array[i]!=None and self.string_array[i]!='_'):
                return_string_array.append(self.string_array[i])
        return(''.join(return_string_array))

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
        string_builder = StringBuilder()
        string_builder.insert('a')
        string_builder.insert('b')
        string_builder.remove('b')
        string_builder.insert('c')
        string_builder.insert('d')
        string_builder.remove('c')
        print(string_builder.string_array)
        print(string_builder.get_string())

driver = Driver()
driver.execute()