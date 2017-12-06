from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from amazon.api import AmazonAPI
import time

amazon = AmazonAPI('AKIAJUEBQSRYM67EZTAA', 'PzSanYuYOnu1OgZXsYe0WRCYbPSZjBuPEcIVqvHX', 'datawareho0a3-20')
Base = declarative_base()
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/datawarehouse')
DBSession = sessionmaker(bind=engine)
session = DBSession()
class Product(Base):
    __tablename__ = 'products'
    productId = Column(String(20), primary_key=True)


def getProduct(productId):
    time.sleep(1.1)
    try:
        product = amazon.lookup(ItemId=productId)
        return product
    except:
        print(productId+' not found!')


# 遍历product表，查询插入数据
query = session.query(Product)
for product in query:  # 遍历时查询
    print(getProduct(product.productId))

session.commit()
session.close()
