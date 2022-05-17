from sqlalchemy import String, Integer, Column

from producer.db import Base


class Emails(Base):
    """ Email models.
    name's table: emails
    fields: id,
            email,
            message """

    __tablename__ = 'emails'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False)
    message = Column(String, nullable=False)

    def __str__(self):
        return self.email, self.message
