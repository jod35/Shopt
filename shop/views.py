from shop import app, db, bcrypt
from flask import render_template, request, redirect, flash, url_for
from flask_login import login_user, login_required, logout_user, current_user
from .models import User, Product,Transaction,Unit,Category


# the home_page
@app.route('/shop/')
def index():
   return render_template('index.html', title="Your Convenient Shop Manager")

   # return "hello world"
# the signup page
@app.route('/shop/buy/')
def buy_products():
   products=Product.query.order_by(Product.name.desc()).limit(10).all()
   return render_template('shop.html',products=products,title="Buy Your Favourite Items")


#create an account
@app.route('/shop/signup/', methods=['GET', 'POST'])
def sign_up():
   if request.method == "POST":
      new_user = User(
          username=request.form.get('username'),
          email=request.form.get('email'),
          contact=request.form.get('contact'),
          location=request.form.get('location'),
          password=bcrypt.generate_password_hash(request.form.get('password'))
      )
      try:
         db.session.add(new_user)
         db.session.commit()
         flash("Account Created Successfully,You are free to Login")
         return redirect(url_for('login'))
      except:
         flash("There has been a little Problem! Check Your Credentials!")
   return render_template('sign.html', title="Create An Account")

# the login page
@app.route('/shop/login/', methods=['GET', 'POST'])
def login():
   email = request.form.get('email')
   password = request.form.get('pasword')
   user = User.query.filter_by(email=email).first()

   if user and bcrypt.check_password_hash(user.password, password):
      login_user(user)
      return redirect(url_for('user_dashboard'))

   return render_template('login.html', title="Login")

# home page after login


@app.route('/shop/home/')
@login_required
def user_dashboard():
   return render_template('dashboard.html',title="User Dashboard")


@app.route('/shop/products/')
@login_required
def products_page():
   all_products = Product.query.filter_by(seller=current_user).all()
   count = 0
   for i in all_products:
      count += 1
   products = Product.query.filter_by(seller=current_user).order_by(
       Product.id.desc()
   ).limit(3).all()
   return render_template('products.html', title="Products", products=products, count=count)

# logout any active user


@app.route('/logout')
def logout():
   logout_user()
   return redirect(url_for('index'))

# add a product to database
@app.route('/shop/products/add', methods=['GET', 'POST'])
@login_required
def add_product():
   categories=Category.query.all() 
   if request.method == 'POST':
      category = request.form.get('category')
      name = request.form.get('name')
      comm_type = request.form.get('comm_type')
      cost_price = int(request.form.get('cost_price'))
      markup = int(request.form.get('markup'))
      discount = int(request.form.get('discount'))
      stock = int(request.form.get('stock'))
      tax = request.form.get('tax')
      image_url=request.form.get('image_url')
      code1 = request.form.get('code1')
      code2 = request.form.get('code2')
      code3 = request.form.get('code3')

      # selling price calculation
      profit = (cost_price * (markup / 100))
      sel_price = cost_price + profit
      disc = (discount / 100) * cost_price
      gross_price = sel_price - disc

      new_product = Product(
          category=category,
          name=name,
          cost_price=cost_price,
          markup=markup,
          discount=discount,
          comm_type=comm_type,
          stock=stock,
          tax=tax,
          code1=code1,
          code2=code2,
          code3=code3,
          selling_price=gross_price,
          seller=current_user,
          image_url=image_url
      )

      db.session.add(new_product)
      db.session.commit()
      flash("Product Added Successfully")
      return redirect(url_for('add_product'))

   return render_template('addproduct.html',title="Add A Product To Your Shop",categories=categories)

# suppliers page

@login_required
@app.route('/shop/suppliers')
def suppliers_page():
   return render_template('suppliers.html', title="Suppliers")

# suppliers page

@login_required
@app.route('/shop/suppliers/add')
def add_supplier():
   countries = ['Uganda', 'Kenya', 'Tanzania', 'Mozambique',
                'USA', 'Spain', 'Madagascar', 'Egypt', 'UK']
   return render_template('addsupplier.html', countries=countries, title="Add Supplier")

@login_required
@app.route('/shop/products/manage', methods=['GET', 'POST'])
def manage_products():
   search = request.form.get('search')
   results = Product.query.filter_by(name=search)

   return render_template('manageproducts.html', results=results)


#update the product information
@login_required
@app.route('/shop/products/manage/<int:id>', methods=['GET', 'POST'])
def manage_product(id):
   product = Product.query.get_or_404(id)
   if request.method == 'POST':
      product.name = request.form.get('name')
      product.category = request.form.get('category')
      product.comm_type = request.form.get('comm_type')
      product.unit = request.form.get('unit')
      product.code1 = request.form.get('code1')
      product.code2 = request.form.get('code2')
      product.cod3 = request.form.get('code3')

      db.session.commit()
      flash("Details Updated Suceesfully")
      return redirect(url_for('products_page'))
   return render_template('prodinfo.html', product=product,title="Product Details")

#for all price changes
@login_required
@app.route('/shop/prices',methods=['GET', 'POST'])
def change_prices():
   search=request.form.get('search')
   return render_template('prices.html')


@login_required
@app.route('/shop/categories')
def add_category():
  return render_template('categories.html')


@login_required
@app.route('/shop/categories/add',methods=['POST'])
def create_category():
  name =request.form.get('name')
  new_category=Category(name=name, creator=current_user)
  db.session.add(new_category)
  db.session.commit()
  flash('New Category Created Successfully!!')
  return redirect(url_for('add_category'))
  