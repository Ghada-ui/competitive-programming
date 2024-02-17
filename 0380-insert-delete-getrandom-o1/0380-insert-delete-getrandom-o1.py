class RandomizedSet(object):
    
    def __init__(self):
        self.myset=set()

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.myset:
            return False
        else:
            self.myset.add(val)
            return True
            
    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.myset:
            return False
        else:
            self.myset.remove(val)
            return True
        

    def getRandom(self):
        """
        :rtype: int
        """
        random_value = random.choice(list(self.myset))
        return random_value
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()