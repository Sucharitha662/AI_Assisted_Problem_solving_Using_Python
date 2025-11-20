import unittest
from task2 import assign_grade

class TestAssignGrade(unittest.TestCase):
    
    # Boundary tests for grade A
    def test_score_100_returns_A(self):
        self.assertEqual(assign_grade(100), 'A')
    
    def test_score_90_returns_A(self):
        self.assertEqual(assign_grade(90), 'A')
    
    # Boundary tests for grade B
    def test_score_89_returns_B(self):
        self.assertEqual(assign_grade(89), 'B')
    
    def test_score_80_returns_B(self):
        self.assertEqual(assign_grade(80), 'B')
    
    # Boundary tests for grade C
    def test_score_79_returns_C(self):
        self.assertEqual(assign_grade(79), 'C')
    
    def test_score_70_returns_C(self):
        self.assertEqual(assign_grade(70), 'C')
    
    # Boundary tests for grade D
    def test_score_69_returns_D(self):
        self.assertEqual(assign_grade(69), 'D')
    
    def test_score_60_returns_D(self):
        self.assertEqual(assign_grade(60), 'D')
    
    # Boundary tests for grade F
    def test_score_59_returns_F(self):
        self.assertEqual(assign_grade(59), 'F')
    
    def test_score_0_returns_F(self):
        self.assertEqual(assign_grade(0), 'F')
    
    # Mid-range tests
    def test_score_85_returns_B(self):
        self.assertEqual(assign_grade(85), 'B')
    
    def test_score_75_returns_C(self):
        self.assertEqual(assign_grade(75), 'C')
    
    def test_score_65_returns_D(self):
        self.assertEqual(assign_grade(65), 'D')
    
    # Invalid input tests
    def test_negative_score_returns_invalid(self):
        self.assertEqual(assign_grade(-5), "Invalid input")
    
    def test_score_above_100_returns_invalid(self):
        self.assertEqual(assign_grade(105), "Invalid input")
    
    def test_string_input_returns_invalid(self):
        self.assertEqual(assign_grade("eighty"), "Invalid input")
    
    def test_none_input_returns_invalid(self):
        self.assertEqual(assign_grade(None), "Invalid input")


if __name__ == '__main__':
    unittest.main()