project name: barbershop app review 

**database
created a database with 3 tables 


**CLI
i used click library

how to run the program 
-fork the repository
-run pipenv shell in the terminal
-run  python3 cli-fil.py # this will help you check the availables commands in cli
includes: Commands:
                   add-barbershop
                   delete-barbershop
                   list-customers
                   list-reviews
                   recent-barbershop

example how to check the list of customers ** python3 cli-fil.py list-customers **    


** seed data
used the fake library

** packages install and used
[packages]
click = "*"
sqlalchemy = "*"
ipdb = "*"
faker = "*"
alembic = "*"

** models.py
creeated the class tables and association tables
include: Review, Barbershop, Customer, barbershop_customer

