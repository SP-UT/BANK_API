from sqlalchemy import Column, Integer
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP, Boolean, String
from sqlalchemy.schema import Sequence
from .database import Base

class Post(Base):
    __tablename__ = "online_account"
    seq = Sequence('tbl_oid_seq', start=10001, increment=1)
    oid = Column(Integer, 
                 seq,
                 primary_key=True, 
                 nullable=False, 
                 server_default=seq.next_value()
                )
    verified_account = Column(Boolean, server_default='False', nullable=False)
    email = Column(String, nullable=False, unique=True)
    passwd = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), 
                        nullable=False, 
                        server_default=text('now()')
                        )