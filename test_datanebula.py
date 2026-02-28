# test_datanebula.py
"""
Tests for DataNebula module.
"""

import unittest
from datanebula import DataNebula

class TestDataNebula(unittest.TestCase):
    """Test cases for DataNebula class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DataNebula()
        self.assertIsInstance(instance, DataNebula)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DataNebula()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
