import unittest
import os


os.path.dirname(os.path.abspath('/home/misba/Documents/largeapp2'))





class TestCharacters(unittest.TestCase):
    @classmethod
    def setUp(cls):
        pass

    def tearDown(cls):
        pass

    def test_displayAll(self):
        self.session = self.get_session()
        from mappings.characters_mapping import Character
        self.charactercount = self.session.query(Character).count()
        self.assertEqual(self.charactercount , 5)






