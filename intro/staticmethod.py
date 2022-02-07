class Physics:
    # Write your code here
    
    @staticmethod
    def calculate_net_force(mass, acceleration):
        if mass <= 0 or acceleration <= 0:
            return 0.0
        else:
            return float(mass) *float (acceleration)
    
    @staticmethod
    def calculate_acceleration(mass, net_force):
        if mass <= 0 or net_force <=0:
            return 0.0
        else:
            return float (net_force)/float(mass) 

    @staticmethod
    def calculate_mass(net_force, acceleration):
        if net_force <= 0 or acceleration <=0:
            return 0.0
        else:
            print(net_force, acceleration)
            return float(net_force)/float(acceleration) 


import unittest



class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(40, Physics.calculate_net_force(4, 10))
        self.assertEqual(0, Physics.calculate_net_force(0, 0))

    def test_case_2(self):
        self.assertEqual(2, Physics.calculate_acceleration(5, 10))
        self.assertEqual(4, Physics.calculate_acceleration(2.5, 10))

    def test_case_3(self):
        self.assertEqual(25, Physics.calculate_mass(50, 2))
        self.assertEqual(0, Physics.calculate_mass(0, 2))

    def test_case_4(self):
        self.assertEqual(0, Physics.calculate_net_force(-50, -2))
        self.assertEqual(0, Physics.calculate_acceleration(-5, 10))
        self.assertEqual(0, Physics.calculate_mass(-50, -2))

    def test_case_5(self):
        self.assertEqual(0, Physics.calculate_acceleration(0, 10))
        self.assertEqual(0, Physics.calculate_mass(50, 0))


if __name__ == "__main__":
    unittest.main()