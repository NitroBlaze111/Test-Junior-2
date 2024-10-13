import unittest
from src.traffic_analyzer import find_busiest_intersections

class TestTrafficAnalyzer(unittest.TestCase):
    def test_single_busiest_intersection(self):
        intersections = {"A": 5, "B": 3, "C": 7, "D": 2}
        result = find_busiest_intersections(intersections)
        print(f"\nTest case: Single busiest intersection")
        print(f"Input: {intersections}")
        print(f"Output: {result}")
        self.assertEqual(result, ["C"])

    def test_multiple_busiest_intersections(self):
        intersections = {"A": 5, "B": 7, "C": 7, "D": 5}
        result = find_busiest_intersections(intersections)
        print(f"\nTest case: Multiple busiest intersections")
        print(f"Input: {intersections}")
        print(f"Output: {result}")
        self.assertEqual(set(result), {"B", "C"})

    def test_all_intersections_equal(self):
        intersections = {"A": 5, "B": 5, "C": 5, "D": 5}
        result = find_busiest_intersections(intersections)
        print(f"\nTest case: All intersections equal")
        print(f"Input: {intersections}")
        print(f"Output: {result}")
        self.assertEqual(set(result), {"A", "B", "C", "D"})

    def test_empty_dictionary(self):
        intersections = {}
        result = find_busiest_intersections(intersections)
        print(f"\nTest case: Empty dictionary")
        print(f"Input: {intersections}")
        print(f"Output: {result}")
        self.assertEqual(result, [])

    def test_single_intersection(self):
        intersections = {"A": 10}
        result = find_busiest_intersections(intersections)
        print(f"\nTest case: Single intersection")
        print(f"Input: {intersections}")
        print(f"Output: {result}")
        self.assertEqual(result, ["A"])

if __name__ == '__main__':
    unittest.main(verbosity=2)