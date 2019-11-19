from shop import db,login_manager,app
from flask_migrate import Migrate
from flask_login import UserMixin
from datetime import datetime


migrate=Migrate(app,db)
login_manager.login_view='login'

#many to many realtioship of user and a suppier
relationship_table=db.Table(
    'relationship_table',
    db.Column('supplier_id',db.Integer(),db.ForeignKey('supplier.id'),nullable=False),
    db.Column('user_id',db.Integer(),db.ForeignKey('user.id'),nullable=False),
    db.PrimaryKeyConstraint('supplier_id','user_id')

)

class Admin(db.Model,UserMixin):
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(40),nullable=False,unique=True)
    age=db.Column(db.Integer(),nullable=False)
    email=db.Column(db.String(255),nullable=False,unique=True)
    password=db.Column(db.Text,nullable=False)

    def __repr__(self):
        return "admin user {}".format(self.name)

class User(db.Model,UserMixin):
    id=db.Column(db.Integer(),primary_key=True)
    username=db.Column(db.String(40),unique=True,nullable=False)
    email=db.Column(db.String(80),unique=True,nullable=False)
    contact=db.Column(db.String(20),unique=True,nullable=False)
    location=db.Column(db.String(40),nullable=False)
    password=db.Column(db.String(255),unique=True)
    products=db.relationship('Product',backref='seller',lazy=True)  
    transactions=db.relationship('Transaction',backref='actor',lazy=True)
    categories=db.relationship('Category',backref='creator',lazy=True)
    suppliers=db.relationship('Supplier',secondary=relationship_table,backref='suppliers')

    

    def __repr__(self):
        return 'user {}'.format(self.username)
class Product(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    category=db.Column(db.String(255),nullable=False)
    name=db.Column(db.String(255),nullable=False)
    comm_type=db.Column(db.String(255),nullable=False)
    cost_price=db.Column(db.Text,nullable=False)
    markup=db.Column(db.Text,nullable=False)
    discount=db.Column(db.Text,nullable=False)
    selling_price=db.Column(db.Text,nullable=False)
    stock=db.Column(db.Text,nullable=False)
    unit=db.Column(db.Text)
    tax=db.Column(db.String(255),nullable=False)
    code1=db.Column(db.String(255),nullable=False)
    code2=db.Column(db.String(255),nullable=False)
    code3=db.Column(db.String(255),nullable=False)
    image_url=db.Column(db.Text(),nullable=False)
    user_id=db.Column(db.Integer(),db.ForeignKey('user.id')) #the seller

    def __repr__(self):
        return 'product {}'.format(self.name)

class Transaction(db.Model):
    transaction_id=db.Column(db.Integer(),primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    d_of_occurence=db.Column(db.DateTime(),default=datetime.utcnow)

    def __repr__(self):
        return "transaction {}".format(self.transaction_id)

class Unit(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(30),nullable=False)
    date_created=db.Column(db.DateTime(),default=datetime.utcnow)

class Category(db.Model):
    category_id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(40),nullable=False)
    user_id = db.Column(db.Integer(),db.ForeignKey('user.id'))

    def __repr__(self):
        return "category {}".format(self.category_id)

class Supplier(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(30),nullable=False)
    stype=db.Column(db.String(30),nullable=False)
    email=db.Column(db.String(30),nullable=False)
    contact=db.Column(db.String(30),nullable=False)
    address=db.Column(db.String(100),nullable=False)
    nationality=db.Column(db.String(25),nullable=False) 
    def __repr__(self):
        return "supplier {}".format(self.name)
    

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
