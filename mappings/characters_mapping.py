from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()

class Character(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True, autoincrement=True,unique=True)
    name = Column(String(36),unique=True)
    description = Column(String(256))
    power = Column(String(256))
    power_level = Column(Integer(), default= 5)


    def __repr__(self):
        return 'Character: {},{},{},{},{}'.format(self.id, self.name, self.description,self.power,self.power_level)

