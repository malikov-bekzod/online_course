import sys 
sys.path.append("./manage")

from manage.create_tables import create_tables
from manage.insert_tables import insert_tables

create_tables()
insert_tables()