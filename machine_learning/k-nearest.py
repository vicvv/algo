'''
K Nearest Neighbors
Use the k-nearest neighbors algorithm to return the k nearest neighbors of the provided features.
These features are the result of a dimensionality reduction by PCA on some operating-system data related 
to processes and their intrusivity in some network. You'll have access to an EXAMPLES dictionary, mapping 
each process identifier "pid_i" 
to a respective dictionary containing its associated features as well as a label representing whether 
the relevant process was intrusive to the network. A label of 0
means that it wasn't intrusive, while a label of 1 means that it was intrusive.

Below is an example portion of the EXAMPLES :
{
 "pid_0": {
 "features": [3.968642003034218, 3.9553899901567955, 3.8067717105202794, # ... more words],
 "is_intrusive": 0,
 }
'''
import math
def predict_label(examples, features, k, label_key="is_intrusive"):
    k_nn = find_k_nearest_neighbors(examples, features, k)
    k_nn_labels = [examples[pid][label_key] for pid in k_nn]
    return round(sum(k_nn_labels)/k)


def find_k_nearest_neighbors(examples, features, k):
    distances={}
    for pid, features_label_map in examples.items():
        distance = get_euclidean_distance(features,features_label_map["features"])
        distances[pid] = distance
    return sorted(distances, key=distances.get)[:k]

def get_euclidean_distance(features, other_features):
    squared_differences =[]
    for i in range(len(features)):
        squared_differences.append((other_features[i] - features[i])**2)
    return math.sqrt(sum(squared_differences))
        




import program
import unittest

import os
import pickle

_DATA_DIR = os.path.dirname(os.path.realpath(__file__)) + "/data"


def get_knn_examples():
    with open(f"{_DATA_DIR}/knn.pickle", "rb") as handle:
        return pickle.load(handle)


EXAMPLES = get_knn_examples()


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        features = [4.30936122, 4.28739283, 4.29680938, 4.33571647, 4.28774593]
        k = 1
        expected = ["pid_500"]
        actual = program.find_k_nearest_neighbors(EXAMPLES, features, k)
        self.assertEqual(sorted(actual), sorted(expected))

    def test_case_2(self):
        features = [4.30936122, 4.28739283, 4.29680938, 4.33571647, 4.28774593]
        k = 1
        expected = 1
        actual = program.predict_label(EXAMPLES, features, k)
        self.assertEqual(actual, expected)

    def test_case_3(self):
        features = [4.30936122, 4.28739283, 4.29680938, 4.33571647, 4.28774593]
        k = 3
        expected = ["pid_500", "pid_535", "pid_545"]
        actual = program.find_k_nearest_neighbors(EXAMPLES, features, k)
        self.assertEqual(sorted(actual), sorted(expected))

    def test_case_4(self):
        features = [4.30936122, 4.28739283, 4.29680938, 4.33571647, 4.28774593]
        k = 3
        expected = 1
        actual = program.predict_label(EXAMPLES, features, k)
        self.assertEqual(actual, expected)

    def test_case_5(self):
        features = [4.30936122, 4.28739283, 4.29680938, 4.33571647, 4.28774593]
        k = 5
        expected = ["pid_500", "pid_535", "pid_545", "pid_512", "pid_516"]
        actual = program.find_k_nearest_neighbors(EXAMPLES, features, k)
        self.assertEqual(sorted(actual), sorted(expected))

    def test_case_6(self):
        features = [4.30936122, 4.28739283, 4.29680938, 4.33571647, 4.28774593]
        k = 5
        expected = 1
        actual = program.predict_label(EXAMPLES, features, k)
        self.assertEqual(actual, expected)

    def test_case_7(self):
        features = [4.30936122, 4.28739283, 4.29680938, 4.33571647, 4.28774593]
        k = 7
        expected = ["pid_500", "pid_535", "pid_545", "pid_512", "pid_516", "pid_513", "pid_537"]
        actual = program.find_k_nearest_neighbors(EXAMPLES, features, k)
        self.assertEqual(sorted(actual), sorted(expected))

    def test_case_8(self):
        features = [4.30936122, 4.28739283, 4.29680938, 4.33571647, 4.28774593]
        k = 7
        expected = 1
        actual = program.predict_label(EXAMPLES, features, k)
        self.assertEqual(actual, expected)

    def test_case_9(self):
        features = [4.30936122, 4.28739283, 4.29680938, 4.33571647, 4.28774593]
        k = 9
        expected = ["pid_500", "pid_535", "pid_545", "pid_512", "pid_516", "pid_513", "pid_537", "pid_540", "pid_528"]
        actual = program.find_k_nearest_neighbors(EXAMPLES, features, k)
        self.assertEqual(sorted(actual), sorted(expected))

    def test_case_10(self):
        features = [4.30936122, 4.28739283, 4.29680938, 4.33571647, 4.28774593]
        k = 9
        expected = 0
        actual = program.predict_label(EXAMPLES, features, k)
        self.assertEqual(actual, expected)