from shop import db,app,login_manager,bcrypt
from shop.models import User,Supplier,Product,Admin
from flask import render_template,request,redirect,url_for
from flask_login import login_user,login_required,logout_user

@app.route('/shop/admin',methods=['GET', 'POST'])
def admin_login():
   email=request.form.get('email')
   password=request.form.get('password')
   admin=Admin.query.filter_by(email=email).first()

   if admin and bcrypt.check_password_hash(admin.password,password):
       login_user(admin)
       return redirect(url_for('admin_home'))

   return render_template('adminlogin.html',title="Admin Login Page")

@app.route('/admin/shop/admin/home')
def admin_home():
   return render_template('admin-dashboard.html')