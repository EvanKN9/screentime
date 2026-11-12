from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

class Group(Base):
    __tablename__ = "groups"

    # Columns will go here