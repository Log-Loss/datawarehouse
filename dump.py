from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

item = {}
all_item = []
for line in open('data.txt', 'rb').readlines():
    line = line.decode('unicode_escape')
    if line == '\n':
        all_item.append(item)
        item = {}
        continue
    key, value = line.strip().split(':', 1)
    item[key] = value.strip()

Base = declarative_base()
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/datawarehouse')
DBSession = sessionmaker(bind=engine)
session = DBSession()
class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    productId = Column(String(20))
    userId = Column(String(20))
    profileName = Column(String(100))
    helpfulCnt = Column(Integer)
    rateCnt = Column(Integer)
    score = Column(Integer)
    time = Column(Integer)
    summary = Column(String(200))
    text = Column(String(20000))

for item in all_item:
    helpfulCnt, rateCnt = str(item['review/helpfulness']).split('/', 1)
    new_comment = Comment(productId=item['product/productId'], userId=item['review/userId'],
                          profileName=item['review/profileName'], helpfulCnt=helpfulCnt,
                          rateCnt=rateCnt, score=item['review/score'],
                          time=item['review/time'], summary=item['review/summary'],
                          text=item['review/text'])
    session.add(new_comment)

session.commit()
session.close()

