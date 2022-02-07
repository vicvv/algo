class Group:
    def __init__(self, name, members=[]):
        self.name = name
        self.members = members

    # Write your code here
    def add(self, name):
        if name not in self.members:
            self.members.append(name)

    def delete(self, name):
        if name not in self.members:
            raise Exception ("Member not in group")
        self.members.remove(name)

    def get_members(self):
        return sorted(self.members)

    def merge(self, othergroup):
        combined_members=self.members + othergroup.members
        new_group = Group("New Group", combined_members)
        return new_group




import unittest


class TestProgram(unittest.TestCase):
   

    def test_case_2(self):
        group = Group("group1", ["A", "C", "B"])
        self.assertTrue(hasattr(group, "get_members"), "A Group should have a `get_members` method.")
        self.assertTrue(hasattr(group, "add"), "A Group should have an `add` method.")
        self.assertTrue(hasattr(group, "delete"), "A Group should have a `delete` method.")

    def test_case_3(self):
        group = Group("group2", ["A", "C", "B"])
        self.assertEqual(["A", "B", "C"], group.get_members())

    def test_case_4(self):
        group = Group("group3", ["A", "C", "B"])
        group.delete("A")
        self.assertEqual(["B", "C"], group.get_members())

    def test_case_5(self):
        group = Group("group4", ["A", "D"])
        group.add("C")
        self.assertEqual(["A", "C", "D"], group.get_members())

    def test_case_6(self):
        group = Group("group5", ["A", "D"])
        with self.assertRaisesRegexp(Exception, "Member not in group"):
            group.delete("Z")

    def test_case_7(self):
        group6 = Group("group6", ["A", "D"])
        group7 = Group("group7", ["B", "C"])
        merged_group = group6.merge(group7)
        self.assertEqual(["A", "B", "C", "D"], merged_group.get_members())


if __name__ == "__main__":
    unittest.main()