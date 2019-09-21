class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data_dict = {}
        self.data_list = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.data_dict:
            return False
        self.data_dict[val] = len(self.data_list)
        self.data_list.append(val)
        return True
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.data_dict:
            return False
        pos = self.data_dict[val]
        if pos < len(self.data_list):
            tail = len(self.data_list) - 1
            tail_val = self.data_list[tail]
            self.data_list[pos], self.data_list[tail] = self.data_list[tail], self.data_list[pos]
            self.data_list.pop()
            self.data_dict[tail_val] = pos
        del self.data_dict[val]
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.data_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()