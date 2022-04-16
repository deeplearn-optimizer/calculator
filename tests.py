from django.test import TestCase
from main_application.views import perform
from math import sqrt, log, factorial, pow

class OpsTestCase(TestCase):
    def setUp(self):
        pass

    def test_operations(self):
        """WE WILL TEST ALL OPERATIONS ARE PERFORMED CORRECTLY OR NOT"""
        
        self.assertEqual(perform('9','root'), str(sqrt(9)))
        self.assertEqual(perform('14','root'), str(sqrt(14)))
        self.assertEqual(perform('25','root'), str(sqrt(25)))
        self.assertEqual(perform('36','root'), str(sqrt(36)))
        
        self.assertEqual(perform('9','log'), str(log(9)))
        self.assertEqual(perform('14','log'), str(log(14)))
        self.assertEqual(perform('25','log'), str(log(25)))
        self.assertEqual(perform('36','log'), str(log(36)))
        
        self.assertEqual(perform('9','fact'), str(factorial(9)))
        self.assertEqual(perform('14','fact'), str(factorial(14)))
        
        self.assertEqual(perform('9,2','power'), str(pow(9,2)))
        self.assertEqual(perform('14,2','power'), str(pow(14,2)))
        self.assertEqual(perform('15,2','power'), str(pow(15,2)))
        self.assertEqual(perform('20,2','power'), str(pow(20,2)))
        
