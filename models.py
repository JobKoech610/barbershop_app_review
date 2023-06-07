from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, MetaData, Table
from sqlalchemy.orm import relationship, backref , sessionmaker
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base()
if __name__ == '__main__':
    engine = create_engine('sqlite:///barbershop.db', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()


#Table associations
barbershop_customer = Table(
    'barbershop_customer',
    Base.metadata,
    Column('barbershop_id',ForeignKey('barbershops_id'),primary_key=True),
    Column('customer_id',ForeignKey('customers_id'),primary_key=True),
    extend_existing=True,

)


#barbershops table
class Barbershop(Base):
    __tablename__ = 'barbershops'
    id = Column(Integer(),primary_key=True),
    name = Column(String())
    location = Column(String())
    customers = relationship('Customer',secondary='barbershop_customer',back_populates=('customers'))
    reviews = relationship("Review", backref=backref("barbershop")) 

    def __repr__(self):
    
        return f'Barbershop(id={self.id}, ' + \
            f'name={self.name}, ' + \
            f'location={self.location})' 

#Customer table
class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer(),primary_key=True),
    first_name = Column(String())
    last_name = Column(String())  
    customers = relationship('Barbershop',secondary='barbershop_customer',back_populates=('barbershops')) 
    reviews = relationship("Review", backref=backref("customer")) 

    def __repr__(self):
    
        return f'Customer(id={self.id}, ' + \
            f'first_name={self.first_name}, ' + \
            f'last_name={self.last_name})' 


class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer(), primary_key=True)
    star_rating = Column(Integer())
    babershop_id = Column(Integer(), ForeignKey('babershop_id'))
    customer_id = Column(Integer(), ForeignKey('customers.id'))
    

    def __repr__(self):
    
        return f'Review(id={self.id}, ' + \
            f'star_rating={self.star_rating}, ' + \
            f'babershop_id={self.babershop_id}), ' +\
            f'customer_id={self.customer_id})' 

