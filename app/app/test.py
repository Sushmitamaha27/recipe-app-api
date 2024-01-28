'''
sample tests
'''

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the Calc module."""
    
    def test_add_number(self):
        """Test adding number together."""
        res=calc.add(5,6)
        
        self.assertEqual(res,11)
        
    def subtract_number(self):
        """Testing subtract number"""
        res=calc.subtract(10,15)


        self.assertEqual(res,5)