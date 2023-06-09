from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy import insert
from sqlalchemy.orm import sessionmaker 

from models import Review, Barbershop, Customer, barbershop_customer


if __name__ == '__main__':
    engine = create_engine('sqlite:///barbershop.db', echo=True)
    

  
    session = sessionmaker(bind=engine)
    session = session()

    session.query(Barbershop).delete()
    session.query(Customer).delete()
    session.query(Review).delete()

    fake = Faker()

    barbershop = [
        Barbershop(
           name=fake.name(),
           location=fake.word(),
           price=random.randint(100, 5000)
        )
    for i in range(50)]
    session.bulk_save_objects(barbershop)

    customer = [
        Customer(
           first_name=fake.name(),
           last_name=fake.name()
        )
    for i in range(50)]
    session.bulk_save_objects(customer)

    review = [
        Review(
            star_rating = random.randint(1,5),
            barbershop_id = random.randint(1,20),
            customer_id = random.randint(1,20)
        )
    for i in range(20)]

    session.bulk_save_objects(review)

combinations = set()
for _ in range(30):
    barbershop_id = random.randint(1, 20)
    customer_id = random.randint(1, 20)

    if (barbershop_id, customer_id) in combinations:
        continue
    combinations.add((barbershop_id, customer_id))
    print(barbershop_id, customer_id)

    barbershop_customer_data = {"barbershop_id": barbershop_id, "customer_id": customer_id}
    stmt = insert(barbershop_customer).values(barbershop_customer_data)
    session.execute(stmt)
    session.commit()

    
session.commit()
session.close()    


  
