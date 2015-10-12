import unittest
from hw2_set import OurSet

class TestSet1(unittest.TestCase):

    def setUp(self):
        self.emptySet = OurSet()
        o = OurSet()
        o.add_list([1,2,3])
        self.os = o

    def test_union1(self):
        """Q7: Test union of OurSet and set with 1 duplicate"""
        u = self.os.union([3,4])
        self.assertEqual(u, [1,2,3,4], "did not correctly union set with duplicates")
        self.assertEqual(self.os.setlist, [1,2,3], "original OurSet changed with union")

    def test_union2(self):
        """Q8: Test union of OurSet and set with no duplicates"""
        u = self.os.union([4,5])
        self.assertEqual(u, [1,2,3,4,5], "did not correctly union set without duplicates")
        self.assertEqual(self.os.setlist, [1,2,3], "original OurSet changed with union")

    def test_union3(self):
        """Q9: Test union of empty OurSet with empty list"""
        u = self.emptySet.union([])
        self.assertEqual(u, [], "did not correctly union empty sets")
        self.assertEqual(self.os.setlist, [1,2,3], "original OurSet changed with union")

    def test_intersection1(self):
        """Q10:Test intersection of OurSet with set with 1 common item"""
        i = self.os.intersection([3,4])
        self.assertEqual(i, [3], "did not intersect with commons correctly")
        self.assertEqual(self.os.setlist, [1,2,3], "original OurSet changed with union")

    def test_intersection2(self):
        """Q11: Test intersection of OurSet with set with no common items"""
        i = self.os.intersection([5,4])
        self.assertEqual(i, [], "did not intersect without common items correctly")
        self.assertEqual(self.os.setlist, [1,2,3], "original OurSet changed with union")

    def test_intersection3(self):
        """Q12: Test intersection of empty OurSet with empty set"""
        i = self.emptySet.intersection([])
        self.assertEqual(i, [], "empty sets intersection incorrect")
        self.assertEqual(self.os.setlist, [1,2,3], "original OurSet changed with union")

    def test_intersection4(self):
        """Q13: Test intersection of OurSet with bad set with duplicates"""
        i = self.os.intersection([2,2,3,3,4,4])
        self.assertEqual(i, [2,3], "duplication bad sets intersection incorrect")
        self.assertEqual(self.os.setlist, [1,2,3], "original OurSet changed with union")

    def test_union4(self):
        """Q14: Test union of OurSet with bad set with duplicates"""
        i = self.os.union([2,2,3,3,4,4])
        self.assertEqual(i, [1,2,3,4], "duplication bad sets union incorrect")
        self.assertEqual(self.os.setlist, [1,2,3], "original OurSet changed with union")

if __name__ == '__main__':
    unittest.main()
