class SubstringSearch:
    """
    Brute force substring search.
    Takes O(s(b-s)) time where s is the size of substring and b is the
    size of main string.

    ...
    Attributes
    ----------
    main_string : str
        The string to be searched in
    sub_string: str
        The string to be seached
    
    Methods
    -------
    search()
        Seaches for substring in main string.
    """
    def __init__(self, main_string='', sub_string=''):
        self.main_string=main_string
        self.sub_string=sub_string
    
    def search(self):
        """
        Seaches for substring in main string.
        """
        for i in range(len(self.main_string)-len(self.sub_string)):
            character_match = [0]*len(self.sub_string)
            for j in range(len(self.sub_string)):
                if(self.main_string[i+j]==self.sub_string[j]):
                    character_match[j]=1
                    continue
                else:
                    break
            if(sum(character_match)==len(self.sub_string)):
                print("Substring \"{}\" found at index {} in \"{}\""\
                            .format(self.sub_string, i, 
                            self.main_string))
                break
            else:
                if(i==(len(self.main_string)-len(self.sub_string)-1)):
                    print("Substring \"{}\" not found in \"{}\""\
                            .format(self.sub_string,
                            self.main_string))

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
        substring_search = SubstringSearch()
        substring_search.main_string='Around the world'
        substring_search.sub_string='he wo'
        substring_search.search()

driver = Driver()
driver.execute()