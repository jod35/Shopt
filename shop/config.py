class DevConfig:
    mydb_user='jon'
    mydb='shopt'
    mydb_password='nathanoj35'

    SQLALCHEMY_DATABASE_URI='mysql+pymysql://{}:{}/{}'.format(mydb_user,mydb_password,mydb)
    SQLALCHEMY_ECHO=True
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY='48f7cfada988c81e3091a31cecc6187a19ef968e439eaa537f739f6cf2be6605'
    DEBUG=True
