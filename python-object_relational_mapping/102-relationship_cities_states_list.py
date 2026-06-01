#!/usr/bin/python3
"""
Lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City

if __name__ == '__main__':
    mysql_user = sys.argv[1]
    mysql_pwd = sys.argv[2]
    db_name = sys.argv[3]
    
    engine = create_engine(
        f'mysql+mysqldb://{mysql_user}:{mysql_pwd}@localhost:3306/{db_name}',
        pool_pre_ping=True
    )
    
    Session = sessionmaker(bind=engine)
    session = Session()

    # Outer join ensures all states are fetched (even without cities) in one query, 
    # while allowing us to sort by both state id and city id at the DB level.
    states = session.query(State).outerjoin(City).order_by(State.id, City.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")

    session.close()
