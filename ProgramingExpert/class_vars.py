class Employee:
    average_age = 0
    average_salary = 0
    count = 0

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
      
        total_salary = Employee.average_salary * Employee.count
        total_age = Employee.average_age * Employee.count
        Employee.average_salary = (total_salary + self.salary)/(Employee.count + 1)
        Employee.average_age = (total_age + self.age)/(Employee.count +1)
        Employee.count +=1


       
        print("avSalary ", Employee.average_salary)
        print("avAge ", Employee.average_age)
        



import unittest

class TestProgram(unittest.TestCase):
    # def test_case_1(self):
    #     self.assertTrue(inspect.isclass(Employee), "Employee should be a class.")

    def test_case_2(self):
        self.assertTrue(hasattr(Employee, "average_age"), "Employee should have a `average_age` attribute.")
        self.assertTrue(hasattr(Employee, "average_salary"), "Employee should have a `set_balance` attribute.")

    def test_case_3(self):
        print("Test 1", Employee.count)
        employee = Employee("Tim", 10, 65000)
        self.assertEqual(10, Employee.average_age)
        self.assertEqual(65000, Employee.average_salary)

    def test_case_4(self):
        print("Test 2", Employee.count)
        employee = Employee("Clement", 23, 10000)
        self.assertEqual(16.5, Employee.average_age)
        self.assertEqual(37500, Employee.average_salary)

    def test_case_5(self):
        print("Test 3", Employee.count)
        employee = Employee("Conner", 45, 15000)
        self.assertEqual(26, Employee.average_age)
        self.assertEqual(30000, Employee.average_salary)

    def test_case_6(self):
        print("Test 4", Employee.count)
        employee = Employee("Alex", 60, 95000)
        self.assertEqual(34.5, Employee.average_age)
        self.assertEqual(46250, Employee.average_salary)



if __name__ == "__main__":
    unittest.main()