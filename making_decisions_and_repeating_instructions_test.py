import unittest
from unittest.mock import patch
import sys
from io import StringIO
from making_decisions_and_repeating_instructions import *


class TestExercise02(unittest.TestCase):
    @patch('builtins.input', side_effect=[4, 3])
    def test_all_numbers(self, mock_input):
        captured_output = StringIO()
        sys.stdout = captured_output
        all_numbers()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "0 1 2")

    @patch('builtins.input', side_effect=[20])
    def test_dog_years(self, mock_input):
        captured_output = StringIO()
        sys.stdout = captured_output
        dog_years()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(),
                         "The dog's age in dog's years is 93")

    @patch('builtins.input')
    def test_consonant_or_vowel(self, mock_input):
        captured_output = StringIO()
        sys.stdout = captured_output
        mock_input.return_value = 'b'
        vowels_list = ('a', 'e', 'i', 'o', 'u')
        user_input = input()
        consonant_or_vowel()
        output = captured_output.getvalue().strip()
        sys.stdout = sys.__stdout__

        if (user_input in vowels_list):
            self.assertEqual(output, (f"{user_input} is a vowel."))
        else:
            self.assertEqual(output, (f"{user_input} is a consonant."))

    @patch('builtins.input')
    def test_month_numbers(self, mock_input):
        captured_output = StringIO()
        sys.stdout = captured_output
        mock_input.return_value = "April"
        months_list = [("February"), ("April", "June", "September", "November"),
                       ("January", "March", "May", "July", "August", "October", "December")]
        user_input = input()
        month_numbers()
        output = captured_output.getvalue().strip()
        sys.stdout = sys.__stdout__

        if (user_input == "February"):
            self.assertEqual(
                output, "List of months: January, February, March, April, May, June, July, August, September, October, November, December\nNo. of days: 28/29 days")
        elif (user_input in months_list[1]):
            self.assertEqual(
                output, "List of months: January, February, March, April, May, June, July, August, September, October, November, December\nNo. of days: 30 days")
        elif (user_input in tuple(months_list[2])):
            self.assertEqual(
                output, "List of months: January, February, March, April, May, June, July, August, September, October, November, December\nNo. of days: 31 days")
        else:
            self.assertEqual(
                output, "List of months: January, February, March, April, May, June, July, August, September, October, November, December\nWrong month name")

    @patch('builtins.input', side_effect=[5])
    def test_pyramids(self, mock_input):
        captured_output = StringIO()
        sys.stdout = captured_output
        pyramids()
        output = captured_output.getvalue().strip()
        sys.stdout = sys.__stdout__

        self.assertEqual(
            output, """@ \r\n@ @ \r\n@ @ @ \r\n@ @ @ @ \r\n@ @ @ @ @ \r\n@ @ @ @ \r\n@ @ @ \r\n@ @ \r\n@""")

    @patch('builtins.input', side_effect=[3, 30])
    def test_fibonacci(self, mock_input):
        captured_output = StringIO()
        sys.stdout = captured_output
        fibonacci()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue().strip()
        self.assertEqual(output,
                         "Fibonacci sequence:\n3  30  33  63  96  159  255  414  669")


if __name__ == "__main__":
    unittest.main()
