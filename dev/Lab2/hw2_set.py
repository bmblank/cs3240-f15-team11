class OurSet(object):
    """
    An iterable class that implements a simple set ADT using a list as its underlying data store.

    def add(self, item): adds the item to OurSet if it's not a duplicate

    def add_list(self, list): adds the non duplicate items in the list to OurSet

    def union(self, set2): Returns the union of OurSet and parameter set2

    def intersection(self, set2): returns the intersection of OurSet and parameter set 2

    """

    def __init__(self):
        """OurSet constructor that initializes an empty set"""
        self.setlist = []

    def add(self, item):
        """adds the parameter to the set if not already in the object set and returns True or False to indicate if the item was added to the set"""
        if item in self.setlist:
            return False
        else:
            self.setlist.append(item)
            return True

    def add_list(self, list):
        """Adds each item in the list to the set if it's not in the set already and returns True or False depending on whether any new items were added to the set"""
        new_item_flag = False
        for item in list:
            if item not in self.setlist:
                self.setlist.append(item)
                new_item_flag = True
        if new_item_flag == True:
            return True
        else:
            return False

    def __str__(self):
        """Helps to print out the OurSet set in angle brackets"""
        ret = "<"
        for item in self.setlist:
            ret = ret + str(item) +  ", "
        ret = ret[:-2]
        ret += ">"
        return ret

    def __len__(self):
        """returns the length of the OurSet set"""
        return len(self.setlist)

    def __iter__(self):
        """Allows for the use of in and not in to process items in an OurSet object"""
        return iter(self.setlist)

    def union(self, set2):
        """Carries out a set union operation between the current set object and the parameter and returns the union set without modifying the current set"""
        set_union = self.setlist[:]
        for item in set2:
            if item not in set_union:
                set_union.append(item)
        return set_union

    def intersection(self, set2):
        """Carries out a set intersection operation between the current set object and the parameter and returns the intersection set without modifying the current set"""
        set_inter = []
        for item in set2:
            if item in self.setlist and item not in set_inter:
                set_inter.append(item)
        return set_inter

# os = OurSet()
# os.add_list([1,2,3])
# print(os.intersection([2,2,3,3,4]))


# os = OurSet()
# print(os.add(1))
# print(os.add(3))
# print(os.add(-15))
# print(os.add(1))
# print(os.add('moo'))
# print(os.setlist)

# seto = OurSet()
# seto.add(4)
# print(seto.add_list([22,4,3,5,6,4,3]))
#
# print(seto.add_list([4,4,7,4,13, 22]))
# print(seto.add_list([4,7,22]))
# print(seto)

# seta = OurSet()
# seta.add_list([3,4,33,3,2,3,1])
# print(len(seta))
# seta.add(77)
# print(len(seta))
# seta.add(3)
# print(len(seta))

# seti = OurSet()
# seti.add_list([3,3,1,35,15,1,7])
# blank = [2,3]
# for item in seti:
#     # if item not in blank:
#     #     print(item)
#     print(item)
#
# # print(blank)

# unionset = OurSet()
# unionset.add_list([5,1,2,3,3,4,1,7, 8, 7])
# print(unionset.union([5,100,1,3,2,23])) #expect [5,1,2,3,4,7,8,100,23]
# print(unionset.setlist)
# print(unionset.union({4,4,4,1,5,105}))
# print(unionset.union({}))

# intersection = OurSet()
# intersection.intersection({1,3,5,4})
# intersection.add(77)
# intersection.add_list([88,2,3,1,9,77])
# print(intersection)
# print(intersection.intersection({27,88,100,88,1}))
# print(intersection)