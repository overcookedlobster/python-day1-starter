import unittest
from io import StringIO
import sys

class TestDay1Subtasks(unittest.TestCase):
    def run_script_with_input(self, script_name, inputs, expected_substring):
        sys.stdin = StringIO('\n'.join(inputs))
        sys.stdout = StringIO()
        exec(open(script_name).read())
        output = sys.stdout.getvalue().strip()
        self.assertIn(expected_substring, output)

    # Sub-Task 1: Variables (No input, check outputs assuming fixed values in code)
    def test_variables_name(self):
        self.run_script_with_input("subtask1_variables.py", [], "My name is")  # Checks print

    def test_variables_double_age(self):
        self.run_script_with_input("subtask1_variables.py", [], "Double my age:")  # Assumes age set

    def test_variables_height_cm(self):
        self.run_script_with_input("subtask1_variables.py", [], "Height in cm:")

    def test_variables_rect_area(self):
        self.run_script_with_input("subtask1_variables.py", [], "Rectangle area: 15")  # 5*3=15

    # Sub-Task 2: I/O
    def test_io_greeting(self):
        self.run_script_with_input("subtask2_io.py", ["Alice", "25"], "Hello, Alice")

    def test_io_age(self):
        self.run_script_with_input("subtask2_io.py", ["Alice", "25"], "You are 25")

    def test_io_sum_nominal(self):
        self.run_script_with_input("subtask2_io.py", ["Alice", "25", "10", "5"], "Sum: 15")

    def test_io_sum_decimal(self):
        self.run_script_with_input("subtask2_io.py", ["Alice", "25", "10.5", "5.5"], "Sum: 16.0")

    # Sub-Task 3: Shape Area Calculator
    def test_shape_circle(self):
        self.run_script_with_input("subtask3_shape_calculator.py", ["circle", "3"], "The area is: 28.26")

    def test_shape_rectangle(self):
        self.run_script_with_input("subtask3_shape_calculator.py", ["rectangle", "5", "3"], "The area is: 15")

    def test_shape_triangle(self):
        self.run_script_with_input("subtask3_shape_calculator.py", ["triangle", "5", "3"], "The area is: 7.5")

    # Homework: Basic Arithmetic Calculator
    def test_calculator_addition(self):
        self.run_script_with_input("homework_basic_calculator.py", ["+", "10", "5"], "Result: 15")

    def test_calculator_subtraction(self):
        self.run_script_with_input("homework_basic_calculator.py", ["-", "10", "5"], "Result: 5")

    def test_calculator_multiplication(self):
        self.run_script_with_input("homework_basic_calculator.py", ["*", "10", "5"], "Result: 50")

    def test_calculator_division(self):
        self.run_script_with_input("homework_basic_calculator.py", ["/", "10", "5"], "Result: 2")

    def test_calculator_division_by_zero(self):
        self.run_script_with_input("homework_basic_calculator.py", ["/", "10", "0"], "Invalid operator!")

if __name__ == '__main__':
    unittest.main()

