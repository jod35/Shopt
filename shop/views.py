from . import app
from flask import(
    render_template,
    redirect,url_for,request,
)

@app.route('/')
def index():
   return render_template('index.html')