import unittest


def generate_string(string, frequency):
    for i in string:
        yield i*frequency

# string = "hello"
# frequency = 3
# #expected = "hhheeellllllooo"
# print (list(generate_string(string, frequency)))



class GenerateString:
    def __init__(self, string, frequency):
        self.string = string
        self.frequency = frequency

    def __iter__(self):
        self.current_index = 0
        self.count = 0
        return self
    
    def __next__(self):
        if self.count >= self.frequency:
            self.count = 0
            self.current_index +=1
        if self.current_index >= len(self.string):
            raise StopIteration 

        self.count += 1
        return self.string[self.current_index]

        

    

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        string = "hello"
        frequency = 3
        expected = "hhheeellllllooo"
        function_result = generate_string(string, frequency)
        class_result = GenerateString(string, frequency)
        self.assertEqual("".join(list(function_result)), expected)
        self.assertEqual("".join(list(class_result)), expected)

    def test_case_2(self):
        string = "tim"
        frequency = 5
        expected = "tttttiiiiimmmmm"
        function_result = generate_string(string, frequency)
        class_result = GenerateString(string, frequency)
        self.assertEqual("".join(list(function_result)), expected)
        self.assertEqual("".join(list(class_result)), expected)

    def test_case_3(self):
        string = "123"
        frequency = 4
        expected = "111122223333"
        function_result = generate_string(string, frequency)
        class_result = GenerateString(string, frequency)
        self.assertEqual("".join(list(function_result)), expected)
        self.assertEqual("".join(list(class_result)), expected)

    def test_case_4(self):
        string = ""
        frequency = 10
        expected = ""
        function_result = generate_string(string, frequency)
        class_result = GenerateString(string, frequency)
        self.assertEqual("".join(list(function_result)), expected)
        self.assertEqual("".join(list(class_result)), expected)

    def test_case_5(self):
        string = "string"
        frequency = 10
        expected = "ssssssssssttttttttttrrrrrrrrrriiiiiiiiiinnnnnnnnnngggggggggg"
        function_result = generate_string(string, frequency)
        class_result = GenerateString(string, frequency)
        self.assertEqual("".join(list(function_result)), expected)
        self.assertEqual("".join(list(class_result)), expected)

    def test_case_6(self):
        string = "Python"
        frequency = 13
        expected = "PPPPPPPPPPPPPyyyyyyyyyyyyyttttttttttttthhhhhhhhhhhhhooooooooooooonnnnnnnnnnnnn"
        function_result = generate_string(string, frequency)
        class_result = GenerateString(string, frequency)
        self.assertEqual("".join(list(function_result)), expected)
        self.assertEqual("".join(list(class_result)), expected)

    def test_case_7(self):
        string = " "
        frequency = 5
        expected = "     "
        function_result = generate_string(string, frequency)
        class_result = GenerateString(string, frequency)
        self.assertEqual("".join(list(function_result)), expected)
        self.assertEqual("".join(list(class_result)), expected)

    def test_case_8(self):
        string = "large string"
        frequency = 3
        expected = "lllaaarrrgggeee   ssstttrrriiinnnggg"
        function_result = generate_string(string, frequency)
        class_result = GenerateString(string, frequency)
        self.assertEqual("".join(list(function_result)), expected)
        self.assertEqual("".join(list(class_result)), expected)


if __name__ == '__main__':
    unittest.main()