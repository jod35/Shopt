from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from shop.config import DevConfig
from flask_migrate import Migrate

app=Flask(__name__)
app.config.from_object(DevConfig)

db=SQLAlchemy(app)
login_manager=LoginManager()
login_manager.init_app(app)
bcrypt=Bcrypt(app)
migrate=Migrate(app,db)



from shop import views


