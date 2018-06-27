import os
import unittest
# os.path.dirname(os.path.abspath('/home/misba/Documents/largeapp2/'))
import sys
# sys.path.append("/home/misba/Documents/largeapp2/")
from database.database_session import get_session

sys.path.append(os.path.abspath('/home/misba/Documents/largeapp2/'))
# print(sys.path)
#path = os.path.dirname(os.path.abspath(__file__))
from mappings.characters_mapping import Character

class TestCharacters(unittest.TestCase):
    @classmethod
    def setUp(cls):
        pass

    def tearDown(cls):
        pass

    def test_displayAll(self):
        print(os.path.dirname(os.path.abspath('/home/misba/Documents/largeapp2/database/database_session/')))
        self.session = get_session()
        self.charactercount = self.session.query(Character).count()
        # self.assertEqual(self.charactercount, 5)
        #

        # self.assertNotEqual(self.charactercount, 4)
        #
        # self.assertRaisesRegex(NoResultFound, "Please add the name of the character")





