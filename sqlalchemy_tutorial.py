from sqlalchemy import create_engine
engine=create_engine("sqlite:///test.db")# for absolute path use four slashes
results=engine.execute("select name from name_table where emp_id=:emp_id",emp_id=3)
conn =engine.connect()
from sqlalchemy import MetaData,Table,Column,Integer,String
###one way to follow for ACID properties
with engine.begin() as conn:
    conn.execute("query1")
    conn.execute("query2")

#Reflection in sqlalchemy is creation of python objects from database scehema
#metadata object is a collection of tables
metadata=MetaData()
user_table=Table('user',metadata,
                Column('id',Integer,primary_key =True),
                Column('name',String).
                Column('fullname',String)
                )





     
    


 

