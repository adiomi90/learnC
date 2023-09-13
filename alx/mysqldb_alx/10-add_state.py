import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from state_model import Base, State
import urllib.parse

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python filename.py <username> <password> <dbname>")
        sys.exit(1)
    username = sys.argv[1]
    password = urllib.parse.quote(sys.argv[2])
    dbname = sys.argv[3]

    try:
        engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}?charset=utf8mb4',
            pool_pre_ping=True)

        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        Louisiana = session.query(State).filter(State.id == 3).first()
        Louisiana.name = 'San diego'
        session.commit()


        print(Louisiana.id, Louisiana.name, sep=":")
        
        session.close() 

    except Exception as e:
        print(f"Error: {e}")
