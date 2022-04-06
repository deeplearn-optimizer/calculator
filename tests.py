from django.test import TestCase
from main_application.views import perform
from math import sqrt, log, factorial, pow

class OpsTestCase(TestCase):
    def setUp(self):
        pass

    def test_operations(self):
        """WE WILL TEST ALL OPERATIONS ARE PERFORMED CORRECTLY OR NOT"""

        self.assertEqual(perform('9','root'), str(sqrt(9)))
        self.assertEqual(perform('9','log'), str(log(9)))
        self.assertEqual(perform('9','fact'), str(factorial(9)))
        self.assertEqual(perform('9,2','power'), str(pow(9,2)))
