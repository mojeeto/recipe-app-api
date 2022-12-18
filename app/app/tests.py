from django.test import SimpleTestCase 
from .calc import sum


class SimpleTestCalculations(SimpleTestCase):
    def testing_sum_def(self):
        self.assertEqual(sum(1,1), 2)
