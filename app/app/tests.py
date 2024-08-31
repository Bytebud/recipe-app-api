"""
    Sample test
"""

from django.test import SimpleTestCase
from app.clac import add


class CalcTests(SimpleTestCase):
    def test_add_numbers(self):
        resultset = add(10, 20)
        self.assertEqual(resultset, 30)
