#!/usr/bin/python3
"""
Creates the State "California" with the City "San Francisco" 
from the database hbtn_0e_100_usa using the cities relationship.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == '__main__':
    mysql_user = sys.argv[1]
    mysql_pwd = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine(
        f'mysql+mysqldb://{mysql_user}:{mysql_pwd}@localhost:3306/{db_name}',
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    california = State(name='California')
    san_francisco = City(name='San Francisco')
    california.cities.append(san_francisco)
    session.add(california)
    session.commit()
    session.close()
