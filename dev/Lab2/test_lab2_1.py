
from hw2_set import OurSet

def test_add_to_empty():
    """Q1: Add one item to an empty OurSet"""
    os = OurSet()
    os.add(1)
    assert os.setlist[0] == 1

def test_add_to_nonempty():
    """Q2: Add item to a non empty list"""
    os = OurSet()
    os.add(1)
    os.add(2)
    os.add(2)
    assert os.setlist == [1,2]

def test_add_list_to_empty():
    """Q3: Add a list to an empty OurSet"""
    os = OurSet()
    os.add_list([1,2])
    assert os.setlist == [1,2]


def test_add_list_to_nonempty():
    """Q4: Add list with duplicates to non empty OurSet"""
    os = OurSet()
    os.add_list([1,2])
    os.add_list([2,3,4])
    assert os.setlist == [1,2,3,4]

def test_len_empty():
    """Q5: Test __len__ of empty list"""
    os = OurSet()
    assert len(os) == 0

def test_len_nonempty():
    """Q6: Test __len__ of nonempty list list"""

    os = OurSet()
    os.add_list([1,2])
    assert len(os) ==2

def test_add_dup_list():
    os = OurSet()
    os.add_list([1,2,3])
    os.add_list([1,2,2,3])
    assert os.setlist == [1,2,3]