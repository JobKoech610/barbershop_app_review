import os
import sys

sys.path.append(os.getcwd)
from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, Table
from sqlalchemy.orm import relationship, backref , sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# convention = {
#     "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
# }
# metadata = MetaData(naming_convention=convention)

Base = declarative_base()
if __name__ == '__main__':
    engine = create_engine('sqlite:///barbershop.db', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
      
#Table associations
barbershop_customer = Table(
    'barbershop_customer',
    Base.metadata,
    Column('barbershop_id',ForeignKey('barbershops.id'),primary_key=True),
    Column('customer_id',ForeignKey('customers.id'),primary_key=True),
    extend_existing=True,

)

#barbershops table
class Barbershop(Base):
    __tablename__ = 'barbershops'
    id = Column(Integer(),primary_key=True)
    name = Column(String())
    location = Column(String())
    price = Column(Integer())
    customers = relationship('Customer',secondary='barbershop_customer',back_populates=('barbershops'))
    reviews = relationship("Review", backref=backref("barbershops")) 

    def __repr__(self):
    
        return f'Barbershop(id={self.id}, ' + \
            f'name={self.name}, ' + \
            f'location={self.location})' 

#Customer table
class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer(),primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    barbershops = relationship('Barbershop',secondary='barbershop_customer',back_populates=('customers'))
    reviews = relationship("Review", backref=backref("customer")) 
    #check review for a specific customer
    def customer_review(self):
        return self.reviews
    #customer = session.query(Customer)[10]
    # customer.customer_review()

    def customer_full_name(self):
        return f"{self.first_name} {self.last_name}"
    #customer = session.query(Customer)[10]
    #customer.customer_full_name()  

    def customer_barbershop(self):
        return self.barbershops
    #customer = session.query(Customer)[10]
    #customer.customer_barbershop()

    def add_review(self,barbershop,rating,session):
        review = Review(customer=self, barbershop=barbershop, star_rating=rating)
        session.add(review)
        session.commit()

    def delete_reviews(self, barbershop, session):
        reviews_to_delete = [review for review in self.reviews if review.barbershop == barbershop]
        for review in reviews_to_delete:
            session.delete(review)
        session.commit()    



    def __repr__(self):
    
        return f'Customer(id={self.id}, ' + \
            f'first_name={self.first_name}, ' + \
            f'last_name={self.last_name})' 


class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer(), primary_key=True)
    star_rating = Column(Integer())
    barbershop_id = Column(Integer(), ForeignKey('barbershops.id'))
    customer_id = Column(Integer(), ForeignKey('customers.id'))
    
    #return the customer for this review
    def customer(self):
        return self.customer
    
    #return the barbershop for this review
    def barbershop(self):
        return self.barbershop

    def __repr__(self):
    
        return f'Review(id={self.id}, ' + \
            f'star_rating={self.star_rating}, ' + \
            f'barbershop_id={self.barbershop_id}), ' +\
            f'customer_id={self.customer_id})' 

