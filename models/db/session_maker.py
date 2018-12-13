from sqlalchemy.orm import sessionmaker


class SessionMaker:
    def make_session(self, engine):
        session = sessionmaker(bind=engine)
        return session()
