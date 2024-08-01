from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Content(Base):
    __tablename__ = "contents"

    content_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    residence1 = Column(String)
    residence2 = Column(String)
    allergy = Column(String)
    howtoeat = Column(String)
    brand = Column(String)
    comment = Column(String)
    create_at = Column(DateTime, default=datetime.datetime.now(), nullable=False)
    
    # Taste fields
    umamiA = Column(Integer)
    umamiB = Column(Integer)
    sweetA = Column(Integer)
    sweetB = Column(Integer)
    bitterA = Column(Integer)
    bitterB = Column(Integer)
    sourA = Column(Integer)
    sourB = Column(Integer)
    saltyA = Column(Integer)
    saltyB = Column(Integer)
    astringencyA = Column(Integer)
    astringencyB = Column(Integer)

    # Texture fields
    shakishakiA = Column(Integer)
    shakishakiB = Column(Integer)
    fuwafuwaA = Column(Integer)
    fuwafuwaB = Column(Integer)
    peelfirmnessA = Column(Integer)
    peelfirmnessB = Column(Integer)
    pulpfirmnessA = Column(Integer)
    pulpfirmnessB = Column(Integer)