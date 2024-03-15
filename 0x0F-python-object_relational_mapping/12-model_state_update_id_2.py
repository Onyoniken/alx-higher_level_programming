#!/usr/bin/python3
"""
script changes name of state object from database
"""
from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    update state objects from database
    """
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3])

    engine = create_engine(db_url)
    Session =sessionmaker(bind=engine)

    session = Session()

    state = session.query(State).filter(State.id == 2).first()
    state.name = "New Mexico"
    session.commit()

    session.close()
