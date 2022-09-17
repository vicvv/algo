import numpy as np
def get_statistics(input_list):
    sorted_input = sorted(input_list)
    input_len = len(input_list)
    
    mean = sum(sorted_input)/input_len
    middle_index = (len(sorted_input) - 1)//2
    median = sorted_input[middle_index]
    if input_len %2 == 0:
        middle_number1 = sorted_input[middle_index]
        middle_number2 = sorted_input[middle_index+1]
        median = ( middle_number1 + middle_number1)/2

    number_counts ={x:sorted_input.count(x) for x in set(sorted_input)}
    mode = max(number_counts.keys(), key = lambda unique_number: number_counts[unique_number])
    sample_variance = sum([(number-mean) ** 2 /(input_len -1) for number in sorted_input])
    sample_standard_deviation = sample_variance ** 0.5    
    mean_standard_error = sample_standard_deviation / input_len ** 0.5
    z_score_standard_error = 1.96 * mean_standard_error
    mean_confidence_interval = [mean - z_score_standard_error, mean + z_score_standard_error]
    return {
        "mean": mean,
        "median": np.median(input_list),
        "mode": mode,
        "sample_variance": sample_variance,
        "sample_standard_deviation": sample_standard_deviation,
        "mean_confidence_interval": mean_confidence_interval,
    }
    
    
import unittest    
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [2, 1, 3, 4, 4, 5, 6, 7]
        expected = {
            "mean": 4.0,
            "median": 4.0,
            "mode": 4.0,
            "sample_variance": 4.0,
            "sample_standard_deviation": 2.0,
            "mean_confidence_interval": [2.6141, 5.3859],
        }
        actual = get_statistics(input)
        self.assertEqual(round_output_values(actual), expected)

    def test_case_2(self):
        input = [2, 3, 4, 5, 6, 7, 8, 8, 8, 1, 1, 1, 10, 10, 10, 11, 12, 12, 12]
        expected = {
            "mean": 6.8947,
            "median": 8.0,
            "mode": 1.0,
            "sample_variance": 15.7661,
            "sample_standard_deviation": 3.9707,
            "mean_confidence_interval": [5.1093, 8.6802],
        }
        actual = get_statistics(input)
        # print("actual",actual)
        # print("\n")
        # print(expected)
        self.assertEqual(round_output_values(actual), expected)

    def test_case_3(self):
        input = [0, 1]
        expected = {
            "mean": 0.5,
            "median": 0.5,
            "mode": 0.0,
            "sample_variance": 0.5000,
            "sample_standard_deviation": 0.7071,
            "mean_confidence_interval": [-0.48, 1.48],
        }
        actual = get_statistics(input)
        self.assertEqual(round_output_values(actual), expected)


def round_output_values(stats):
    if type(stats) is not dict:
        # Bad output; let tests fail.
        return stats

    new_output = {}
    for key in stats.keys():
        new_output[key] = stats[key]

        if type(stats[key]) is list:
            if len(stats[key]) >= 1:
                new_output[key][0] = round_to_4(stats[key][0])
            if len(stats[key]) >= 2:
                new_output[key][1] = round_to_4(stats[key][1])
        else:
            new_output[key] = round_to_4(stats[key])

    return new_output


def round_to_4(number):
    if not is_number(number):
        # Bad output; let tests fail.
        return number

    return round(number, 4)


def is_number(element):
    return type(element) in (int, float)


if __name__ =="__main__":
    unittest.main()