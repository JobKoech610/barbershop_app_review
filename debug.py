import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker

from models import Review, Barbershop, Customer, barbershop_customer

import ipdb;
if __name__ == '__main__':
    
    engine = create_engine('sqlite:///restaurants.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    fake = Faker()
    
   
    ipdb.set_trace()