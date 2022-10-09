import unittest

# def flatten_lists(funct):
#     def inner(*args):
#         #print("in flatten" ,args)
#         r =[]
#         for ele in args:
#             if isinstance(ele, list):
#                 r += ele
#             else:
#                 r.append(ele)
#         result = funct(*r)
#         return result
#     return inner


# def convert_strings_to_ints(funct):
#     print("in convert")
#     def inner(*args):
#         r =[]
#         for i in args:
#             if isinstance(i, str) and i.isdigit():
#                 r.append(int(i))
#             else:
#                 r.append(i)
#         result = funct(*r)
#         return result
#     return inner



# def filter_integers(func):
#     print("in filter integers")
#     def inner(*args):
#         new_arg =[]
#         for arg in args:
#             if isinstance(arg, int):
#                 new_arg.append(arg)
#         result = func(*new_arg)
#         return result
#     return inner
        
# # def filter_integers(func):
# #     def wrapper(*args):
# #         new_args = []
# #         for arg in args:
# #             if isinstance(arg, int):
# #                 new_args.append(arg)

# #         result = func(*new_args)
# #         return result

# #     return wrapper

# # def addone(funct):
    
# #     def inner(*a,**b):        
# #         theresult = funct(*a,**b)
# #         return theresult + 1
# #     return inner


# @flatten_lists
# @convert_strings_to_ints
# @filter_integers
# def integer_sum(*args):
#     print("in integer sum", args)
#     return sum(args)


# def integer_sum(*args):
#     r=[]
#     for ele in args:
#         if isinstance(ele, list):
#             r += ele
#         else:
#             r.append(ele)
#     s = 0
#     for i in r:
#         if not isinstance(i, float) and not isinstance(i, list):
#             try:
#                 s += int(i)
#             except ValueError:
#                 continue
    
#     return s


# args = [True, "1", "2", -0.9, 4, [5, "hi", "3"]]
# print(integer_sum(*args))


def flatten_lists(funct):
    def inner(*args):
        new_args =[]
        for ele in args:
            if isinstance(ele, list):
                new_args += ele
            else:
                new_args.append(ele)
        result = funct(*new_args)
        return result
    return inner

def convert_strings_to_ints(funct):
    def inner(*args):
        new_args =[]
        for ele in args:
            if isinstance(ele, str) and ele.isdigit():
                new_args.append(int(ele))
            else:
                new_args.append(ele)
        result = funct(*new_args)
        return result
    return inner

def filter_integers(funct):
    def inner(*args):
        new_args =[]
        for ele in args:
            if isinstance(ele, int):
                new_args.append(ele)
        result = funct(*new_args)
        return result
    return inner


@flatten_lists
@convert_strings_to_ints
@filter_integers
def integer_sum(*args):
    print(args)
    return sum(args)




class TestProgram(unittest.TestCase):
    def test_case_1(self):
        
        args = [True, "1", "2", -0.9, 4, [5, "hi", "3"]]
        expected = 16
        result = integer_sum(*args)
        self.assertEqual(result, expected)

    def test_case_2(self):
        args = [2, 3, 4, -2, "2", ["1", "2", 3], 2.3]
        expected = 15
        result = integer_sum(*args)
        self.assertEqual(result, expected)

    def test_case_3(self):
        args = []
        expected = 0
        result = integer_sum(*args)
        self.assertEqual(result, expected)

    def test_case_4(self):
        args = ["2.3", "true", [1, "hello", 4]]
        expected = 5
        result = integer_sum(*args)
        self.assertEqual(result, expected)

    def test_case_5(self):
        args = [[1], [2], ["3", "4"], [1, 2]]
        expected = 13
        result = integer_sum(*args)
        self.assertEqual(result, expected)

    def test_case_6(self):
        args = ["1", "2", "5", "6", ["1", "2"]]
        expected = 17
        result = integer_sum(*args)
        self.assertEqual(result, expected)

    def test_case_7(self):
        args = [[1, [2]], [1, 2]]
        expected = 4
        result = integer_sum(*args)
        self.assertEqual(result, expected)

    def test_case_8(self):
        args = ["5", "6", "2", 4]
        expected = 17
        result = integer_sum(*args)
        self.assertEqual(result, expected)

    def test_case_9(self):
        args = []
        expected = 0
        result = integer_sum(*args)
        self.assertEqual(result, expected)

    def test_case_10(self):
        args = [2.4]
        expected = 0
        result = integer_sum(*args)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()