import unittest
from solution import count_chars_in_file


class TestCharCounter(unittest.TestCase):

    def test_count_chars_in_empty_file(self):
        with open('empty.txt', 'w', encoding='utf-8') as file:
            # 创建一个空文件用于测试
            pass
        self.assertEqual(count_chars_in_file('empty.txt'), 0)

    def test_count_chars_in_non_empty_file(self):
        with open('non_empty.txt', 'w', encoding='utf-8') as file:
            file.write('Hello, World!')
        self.assertEqual(count_chars_in_file('non_empty.txt'), 13)

    def test_count_chars_with_special_characters(self):
        with open('special_chars.txt', 'w', encoding='utf-8') as file:
            file.write('你好，世界！123')
        self.assertEqual(count_chars_in_file('special_chars.txt'), 9)

    def tearDown(self):
        # 在每个测试用例结束后清理创建的文件
        for filename in ['empty.txt', 'non_empty.txt', 'special_chars.txt']:
            try:
                open(filename, 'r').close()
                open(filename, 'w').close()
            except FileNotFoundError:
                pass


if __name__ == '__main__':
    unittest.main()
