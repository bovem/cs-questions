def normal_hash(string):
    """
    Returns a hash value based on mapping.
    {' ':1, 'a':2, .....}

    Parameters
    ----------
    string : str
        String to be hashed.
    
    Returns
    -------
    hash_val: int
        Hash value that is calculated as an integer.
    """
    string_map = dict(zip(list(" abcdefghijklmnopqrstuvwxyz"), range(1, 28)))
    hash_val = 0
    for i in range(len(string)):
        hash_val += string_map[string[i]]
    return hash_val

def rabin_fingerprint(string, base):
    """
    Returns a hash value based on Rabin Fingerprint Function.
    Converts mapping from normal_hash() into a number with specified base.

    Parameters
    ----------
    string: str
        String to be hashed.
    base: int
        Base for the hash to be generated

    Returns
    -------
    hash_val: int
        Hash value calculated as a number with specified base
        in parameters.
    """
    hash_val = 0
    for i in range(len(string)):
        hash_val += normal_hash(string[len(string)-1-i])*(base**i)
    return hash_val

class RabinKarpSubstringSearch:
    """
    Rabin-Karp substring search.
    Takes O(s+b) time where s is the size of substring and b is the
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
    normal_hash_search()
        Seaches for substring in main string using normal_hash() as 
        hashing function.
    rabin_fingerprint_hash_search()
        Searches for substring in main string using rabin_fingerprint()
        as hashing function.
    """
    def __init__(self, main_string='', sub_string=''):
        self.main_string=main_string
        self.sub_string=sub_string
    
    def normal_hash_search(self):
        """
        Seaches for substring in main string using normal_hash()
        """
        temp_hash = normal_hash(self.main_string[:len(self.sub_string)])
        sub_string_hash = normal_hash(self.sub_string)
        found = False
        for i in range(len(self.main_string)-len(self.sub_string)+1):
            if temp_hash == sub_string_hash:
                found = True
                break
            
            temp_hash = temp_hash\
                        - normal_hash(self.main_string[i])\
                        + normal_hash(self.main_string[i+len(self.sub_string)])

        if(found==True):
            print("Substring \"{}\" found at index {} in \"{}\""\
                .format(self.sub_string, i, 
                self.main_string))
        else:
            print("Substring \"{}\" not found in \"{}\""\
                .format(self.sub_string,
                self.main_string))
    
    def rabin_fingerprint_hash_search(self, base=128):
        """
        Searches for substring in main string using rabin_fingerprint()
        """
        temp_hash = rabin_fingerprint(self.main_string[:len(self.sub_string)], base)
        sub_string_hash = rabin_fingerprint(self.sub_string, base)
        found = False
        for i in range(len(self.main_string)-len(self.sub_string)+1):
            if temp_hash == sub_string_hash:
                found = True
                break

            temp_hash = (temp_hash\
                        -normal_hash(self.main_string[i])*(base**(len(self.sub_string)-1)))*base\
                        +rabin_fingerprint(self.main_string[i+len(self.sub_string)], base)
        
        if(found==True):
            print("Substring \"{}\" found at index {} in \"{}\""\
                .format(self.sub_string, i, 
                self.main_string))
        else:
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
        substring_search = RabinKarpSubstringSearch()
        substring_search.main_string='around the world'
        substring_search.sub_string='the w'
        #substring_search.sub_string='world'
        substring_search.normal_hash_search()
        substring_search.rabin_fingerprint_hash_search(base=128)

driver = Driver()
driver.execute()