class DBService:
    def __init__(self, session, object_to_db):
        self.session = session
        self.object_to_db = object_to_db

    def save(self):
        self.session.add(self.object_to_db)
        self.session.commit()

    def delete(self):
        self.session.delete(self.object_to_db)
        self.session.commit()
