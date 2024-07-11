import unittest
from solution import encrypt_string


class TestEncryptString(unittest.TestCase):

    def test_encrypt_string_with_positive_shift(self):
        input_string = "Hello"
        expected_output = "Khoor"
        actual_output = encrypt_string(input_string, 3)
        self.assertEqual(actual_output, expected_output)

    def test_encrypt_string_with_negative_shift(self):
        input_string = "Hello"
        expected_output = "Ebiil"
        actual_output = encrypt_string(input_string, -3)
        self.assertEqual(actual_output, expected_output)

    def test_encrypt_string_with_large_shift(self):
        input_string = "Hello"
        expected_output = "Khoor"
        actual_output = encrypt_string(input_string, 29)
        self.assertEqual(actual_output, expected_output)

    def test_encrypt_string_with_empty_string(self):
        input_string = ""
        expected_output = ""
        actual_output = encrypt_string(input_string, 3)
        self.assertEqual(actual_output, expected_output)

    def test_encrypt_string_with_mixed_case(self):
        input_string = "AbCdE"
        expected_output = "DeFgH"
        actual_output = encrypt_string(input_string, 3)
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()
