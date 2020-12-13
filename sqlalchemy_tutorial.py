from sqlalchemy import create_engine
engine=create_engine("sqlite:///test.db")# for absolute path use four slashes
results=engine.execute("select name from name_table where emp_id=:emp_id",emp_id=3)
conn =engine.connect()
from sqlalchemy import *
###one way to follow for ACID properties
with engine.begin() as conn:
    conn.execute("query1")
    conn.execute("query2")

#metadata object is a collection of tables
metadata=MetaData()
user_table=Table('user',metadata,
                Column('id',Integer,primary_key =True),
                Column('name',String).
                Column('fullname',String,ForeignKey('remote.id'))
                )
#if you have more than one primary key i.e composite key
ForeignKeyConstraint(['id','name'],
                                     ['remote.id','remote.name']
                                    )            

#Reflection in sqlalchemy is creation of python objects from database scehema
metadata2=MetaData()
user_reflected=Table('user',metadata2,autoload=True,autoload_with=engine)




#it created all the tables which does not exist in database
metadata.create_all(engine)

# inspect gives official information of obhject
inspector=inspect(engine)
print(inspector.get_table_names())

for tname in inspector.get_table_names():
    for column inspector.get_columns(tname):
        if column['name']=='story_id':
            print(tname)

from sqlalchemy.ext.declarative import declarative_base
Base=declarative_base()
print(Base.metadata)
class User(Base):
    __tablename__='user'
    id=Column(Integer,primary_key =True)
    name=Column(String)
    fillname=Column(String)
    def __repr__(self):
        return f'{self.name}  {self.fillname}'

e_user=User(id=1,name="aman",fillname="lalwani")
from sqlalchemy.orm import Session,aliased 
session=Session(bind=engine)
session.add(e_user)
session.commit()
Base.metadata.create_all(engine)
query=session.query(User).filter(User.name=="ed").order_by(User.id)
print(query.all())

for row in session.query(User,User.name):
    print(row.User,row.name)

for name in session.query(User.name).filter_by(fillname="Ed Jones"):
    print(name)
for data in session.query(User).filter(or_(User.name=="ed",User.id=1)).order_by(User.id):
    print(data)

# one gives exception when no rows or more than one rows found
user_alias=aliased(User,name='user_alias')
for rows in session.query(user_alias,user_alias.name).all():
    print(row.user_alias)

query.filter(User.name.like('%ed%')) 
query.filter(USer.name .ilike('%ed%'))

query.filter(tupele_(User.name ,User.nickname).\
    in_([('ed','edsnickname'),('wendy','windy')]))

query.filter(User.name.isnot(None))
session.query(User).from_statement(text("select * from users where name=:name")).params(name="ed").all()
from sqlalchemy.orm import relationship
class Address(Base):
    __tablename__='addresses'
    id=Column(Integer,primary_key=True)
    email_address=Column(String,nullable=False)
    user_id=Column(Integer,ForeignKey('users.id'))
    user=relationship("User",back_populates="addresses")

#query with joins
for u,a in session.query(Use,Address).filter(User.id===Address.id).filter(Address.email_address=="jack@google.com").all():
    print(u)
    print(a)

session.query(User).join(Address).filter(Address.email_address=='jack@google.com').all()
#select in loading
from sqlalchemy.orm  import selectinload
jack=session.query(User).options(selectinload(User.addresses)).filter_by(name='jack').one()

#eager loading
jack=session.query(User).options(joinedload(User.addresses)).filter_by(name='jack').one()
















     
    


 

