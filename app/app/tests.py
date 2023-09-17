from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):

    def test_add_numbers(self):
        res = calc.add(1, 1)

        self.assertEquals(2, res)

    def test_sub_numbers(self):
        res = calc.sub(10, 9)

        self.assertEquals(1, res)
