import unittest
from math_quiz import Limitfunc, Operatorfunc, Mathfunc
class TestMathGame(unittest.TestCase):

    def test_Limitfunc(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = Limitfunc(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)
    def test_Operatorfunc(self): 
        valid = ("+  -  *")
        for _ in range(1000):
                operator = Operatorfunc()
                self.assertIn(operator,valid)
        pass  
    def test_Mathfunc(self):
            test_case = [
                (5, 2, '+', '5 + 2', 7),
                (6, 1, '-', '6 - 1', 5),
                (3, 3, '*', '3 * 3', 9),
                (4, 4, '+', '4 + 4', 8),
                (9, 5, '-', '9 - 5', 4),         
            ]
            for number1, number2, operator, expected_problem, expected_answer in test_case:
                prob, answer = Mathfunc(number1, number2, operator)
                self.assertEqual(prob, expected_problem)   
                self.assertEqual(answer, expected_answer)
            pass
if __name__ == "__main__":
    unittest.main()