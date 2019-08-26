from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///C:/Users/jodes/OneDrive/Desktop/flask/site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db =SQLAlchemy(app=app)

class Boy(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(255))
    age=db.Column(db.Integer)
    
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __repr__(self):
        return "{}".format(self.name)
@app.route('/')
def index():
    boys=Boy.query.all()
    return render_template('index.html',title='Add Boy',boys=boys)

@app.route('/add',methods=['GET', 'POST'])
def AddBoy():
    if request.method=='POST':
        name=request.form.get('name')
        age=request.form.get('age')

        new_boy=Boy(name=name,age=age)
        db.session.add(new_boy)
        db.session.commit()
        return redirect('/')

   
if __name__ == "__main__":
    app.run(debug=True)