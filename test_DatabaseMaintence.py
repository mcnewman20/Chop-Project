from unittest import TestCase
import DatabaseMaintence

class Test(TestCase):
    def test_get_engine(self):
        assert DatabaseMaintence.get_engine() != None
