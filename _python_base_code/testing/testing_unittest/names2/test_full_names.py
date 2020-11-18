import unittest
from full_names import get_full_names

class NamesTestCase(unittest.TestCase):
    'test for names.py'

    def test_first_last(self):
        'test names like Janis Joplin'
        full_name = get_full_names('Janis', 'Joplin')
        self.assertEqual(full_name, 'Janis Joplin')

    def test_middle(self):
        full_name  = get_full_names('David', 'Roth', 'Lee')
        self.assertEqual(full_name, 'David Lee Roth')

if __name__ == '__main__':
    unittest.main()