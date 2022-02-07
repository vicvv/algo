


def sort_employees(employees, sort_by):
    h={"name":0, "age":1, "salary":2}
    return sorted(employees,key=lambda i:i[h[sort_by]])


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        employees = [
            ["John", 33, 65000],
            ["Sarah", 24, 75000],
            ["Josie", 29, 100000],
            ["Jason", 26, 55000],
            ["Connor", 25, 110000],
        ]
        sort_by = "age"
        expected = [
            ["Sarah", 24, 75000],
            ["Connor", 25, 110000],
            ["Jason", 26, 55000],
            ["Josie", 29, 100000],
            ["John", 33, 65000],
        ]
        result = program.sort_employees(employees, sort_by)
        self.assertEqual(result, expected)

    def test_case_2(self):
        employees = [
            ["John", 33, 65000],
            ["Sarah", 24, 75000],
            ["Josie", 29, 100000],
            ["Jason", 26, 55000],
            ["Connor", 25, 110000],
        ]
        sort_by = "salary"
        expected = [
            ["Jason", 26, 55000],
            ["John", 33, 65000],
            ["Sarah", 24, 75000],
            ["Josie", 29, 100000],
            ["Connor", 25, 110000],
        ]
        result = program.sort_employees(employees, sort_by)
        self.assertEqual(result, expected)

    def test_case_3(self):
        employees = [
            ["John", 33, 65000],
            ["Sarah", 24, 75000],
            ["Josie", 29, 100000],
            ["Jason", 26, 55000],
            ["Connor", 25, 110000],
        ]
        sort_by = "name"
        expected = [
            ["Connor", 25, 110000],
            ["Jason", 26, 55000],
            ["John", 33, 65000],
            ["Josie", 29, 100000],
            ["Sarah", 24, 75000],
        ]
        result = program.sort_employees(employees, sort_by)
        self.assertEqual(result, expected)

    def test_case_4(self):
        employees = []
        sort_by = "salary"
        expected = []
        result = program.sort_employees(employees, sort_by)
        self.assertEqual(result, expected)

    def test_case_5(self):
        employees = []
        sort_by = "name"
        expected = []
        result = program.sort_employees(employees, sort_by)
        self.assertEqual(result, expected)

    def test_case_6(self):
        employees = []
        sort_by = "age"
        expected = []
        result = program.sort_employees(employees, sort_by)
        self.assertEqual(result, expected)    