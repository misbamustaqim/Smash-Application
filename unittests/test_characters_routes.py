import unittest
import os


#os.path.dirname(os.path.abspath('/home/misba/Documents/largeapp2'))
from sqlalchemy.orm.exc import NoResultFound

from database.database_session import get_session
from mappings.characters_mapping import Character


class TestCharacters(unittest.TestCase):
    @classmethod
    def setUp(cls):
        pass

    def tearDown(cls):
        pass

    def test_displayAll(self):
        self.session = get_session()
        self.charactercount = self.session.query(Character).count()
        self.assertEqual(self.charactercount , 5)

        self.assertNotEqual(self.charactercount,4)

        self.assertRaisesRegex(NoResultFound, "Please add the name of the character")

    def test_returndescription(self):
        #self.assertRaises(NoResultFound, returndescription)
        self.session = get_session()
        self.info = self.session.query(Character).filter_by(name='Dr. Mario').one()
        self.character = Character(name='Dr. Mario',description='KO power.',power='  KO power.')
        self.assertEqual(self.info.name, self.character.name)
        print(self.info.description)
        print(self.character.description)
        self.assertEqual(self.info.description, self.character.description)
        self.assertEqual(self.info.power, self.character.power)


        self.tempname = 'Dr. Msdhi'
        self.assertNotEqual(self.tempname, self.character.name)

        self.assertRaisesRegex(NoResultFound, "Please add the name of the character")

    def test_insert_characters(self):
        #is empty

        self.assertRaisesRegex(NoResultFound, "All fields are required")
        # session is not connected
        pass

    def test_deleteentry(self):

        # database count greater that 4
        self.session = get_session()
        self.charactercount = self.session.query(Character).count()
        self.assertGreater(self.charactercount, 4)

        #if name is not equal
        self.info = self.session.query(Character).filter_by(name='Dr. Mario').one()
        self.tempname = 'Dr. Msdhi'
        self.assertNotEqual(self.tempname, self.info.name)

        self.assertRaisesRegex(NoResultFound, "Please add name of the character")


    def test_updateTheEntry(self):
        # with self.assertRaises(NoResultFound) as cm:
        #     "Please add discription"
        # the_exception = cm.exception
        # self.assertEqual(the_exception.error_code, "Please add discription")
        self.assertRaisesRegex(NoResultFound, "Please add discription")






