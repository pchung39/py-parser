import unittest
from main import parse

class ParserTest(unittest.TestCase):
    def setUp(self):
        string_value = '''
        1
        Purple
        Concord
        purpleconcord@gmail.com
        malbe
        123.123.123
        manager

        2
        Bear
        Grizzly
        bear@gmail.com
        male
        1234.123.123
        programmer

        3
        Dodo
        Bird
        laugh@gmail.com
        male
        12.13.12.3
        programmer
        
        '''

    def test_parser(self):
        response = parse('example.csv')
        self.assertEqual(response, string_value)

if __name__ == '__main__':
    unittest.main()
