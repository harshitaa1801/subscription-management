from io import StringIO
import os
import unittest
from geektrust import get_subscription_data
from unittest.mock import patch

class TestSubscription(unittest.TestCase):
    def check_output(self, input_file, expected_file):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            get_subscription_data(os.path.join("sample_input", input_file))
            actual = fake_out.getvalue().strip()

        with open(os.path.join("expected_output", expected_file), "r") as f:
            expected = f.read().strip()

        self.assertEqual(actual, expected)


    def test_proper(self):
        self.check_output("input1.txt", "output1.txt")
        self.check_output("input2.txt", "output2.txt")


    def test_no_topup(self):
        self.check_output("input3.txt", "output3.txt")

    def test_invalid_date(self):
        self.check_output("input4.txt", "output4.txt")

    def test_duplicates(self):
        self.check_output("input5.txt", "output5.txt")


if __name__ == '__main__':
    unittest.main()
