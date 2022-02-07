
'''
Abstract class example. Abstact class can have methods of its own.
'''
import unittest
class Animal:
    def sleep(self):
        print('ZzzZzz')

    def animal_sound(self):
        raise NotImplementedError

    def wake_up(self):
        self.animal_sound()
        print('I am awake')


class Lion(Animal):
    def __inint__(self):
        pass
   
    def animal_sound(self):
        print('Roar!')


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        leo = Lion()
        leo.sleep()

    def test_case_2(self):
        leo = Lion()
        leo.animal_sound()

    def test_case_3(self):
        leo = Lion()
        leo.sleep()
        leo.animal_sound()
        leo.wake_up()

    def test_case_4(self):
        with self.assertRaises(NotImplementedError):
            animal = Animal()
            animal.animal_sound()

    def test_case_5(self):
        self.assertIn(Animal, Lion.__bases__)
        self.assertTrue(hasattr(Lion, "animal_sound"), "The Lion class should override the `animal_sound` method.")
        self.assertFalse(Lion().animal_sound == Animal().animal_sound,
                         "The Lion class should override the `animal_sound` method.")



if __name__ == "__main__":
     unittest.main()