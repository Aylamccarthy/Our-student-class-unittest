import unittest
from student import Student

class TestStudent(unittest.TestCase):

    def setUp(self):
        print('SetUp')
        self.student = Student('John', 'Doe')

    def tearDown(self):
        print('tearDown')


    def test_full_name(self):
        print('test_full_name')

        self.assertEqual(self.student.full_name, 'John Doe')

    def test_alert_santa(self):
        print('test_alert_santa')
        self.student.alert_santa()

        self.assertTrue(self.student.naughty_list)

    def test_email_address(self):
        print('test_email_address')
        self.assertEqual(self.student.email_address, 'john.doe@email.com')


if __name__ == '__main__':
    unittest.main()
