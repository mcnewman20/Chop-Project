import sqlalchemy
from sqlalchemy import create_engine


class ChopDB:
    def __init__(self):
        self.engine = self.get_engine()

    def get_engine(self):
        return create_engine("mysql+pymysql://admin:yTQUnAoPzodblWWorYCC@database-2.c4qu6fslstvx.us-east-1.rds"
                             ".amazonaws.com/chop", echo=True)
