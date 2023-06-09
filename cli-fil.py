#!/usr/bin/env python3
import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Review, Barbershop, Customer, barbershop_customer


engine = create_engine('sqlite:///barbershop.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

@click.group()
def func():
    pass
#list reviews in tuples
@click.command()
def list_reviews():
    reviews = session.query(Review).all()
    if reviews:
        click.echo("all Reviews:")
        for review in reviews:
            rev = (review.id,review.star_rating,review.babershop_id,review.customer_id)
            click.echo(f"all Reviews:{rev}")
    else:
        click.echo("no reviews found") 

#list customers in dictionary             
@click.command()
def list_customers():
    customers = session.query(Customer).all()
    if customers:
        click.echo("All Customers:")
        for customer in customers:
            cust = {
                "id": customer.id,
                "first_name": customer.first_name,
                "last_name": customer.last_name
            }
            click.echo(cust)
    else:
        click.echo("No customers found")


#add barbershop
@click.command()
@click.option("--name", prompt="Enter the barbershop name", help="barbershop name")
@click.option("--location", prompt="Enter the location", help="barbershop location")
@click.option("--price", prompt="Enter the price", help="price")
def add_barbershop(name, location, price):
    price = int(price)  # Convert price to an integer
    #validation
    if price <= 100:
        raise click.BadParameter("Price must be above 100")
    else:
        barbershop = Barbershop(name=name, location=location, price=price)
        session.add(barbershop)
        session.commit()
        click.echo("Barbershop added successfully")

#delete barbershop
@click.command()
@click.option("--name", prompt="Enter the barbershop name", help="barbershop name")
def delete_barbershop(name):
    # Validation
    if not name.istitle():
        raise click.BadParameter("Words must be in titlecase")

    # Delete the barbershop
    barbershop_delete = session.query(Barbershop).filter(Barbershop.name == name).delete()
    session.commit()
    click.echo("Barbershop deleted successfully")

    
       
    
#check the recent added barbershop
@click.command()
def recent_barbershop():
    barbershops = session.query(Barbershop).order_by(Barbershop.id.desc()).first()
    click.echo(f"recently added barbershop:{barbershops}")
       

func.add_command(list_reviews)
func.add_command(list_customers)
func.add_command(add_barbershop)
func.add_command(recent_barbershop)
func.add_command(delete_barbershop)

if __name__ == '__main__':
    func()
