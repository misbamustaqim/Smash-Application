from sqlalchemy import create_engine, literal, func
from sqlalchemy.orm import session, scoped_session, sessionmaker

from database.database_session import Session, exists, get_session
from mappings.characters_mapping import Character

engine = create_engine('sqlite:///database3.db', echo=True)
character = Character(name = 'Ross Bing' , description = 'Chandler Muriel Bing is a fictional character from the NBC sitcom Friends, portrayed by Matthew Perry..' , power = 'comedian')
session = get_session()
Session = scoped_session(sessionmaker(bind=engine))
true, false = literal(True), literal(False)
(ret, ), = Session.query(exists().where(Character.name=='Ross Bing'))

#q = session.query(Character).filter(character.name == 'mka Bing')
#session.query(q.exists())

print(ret)

if ret:
    print("already exists")
else:
    print("Does not exist")
session.commit()
session.close()

