from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from extensions import db
import models
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)
@app.route("/")
def index():
    return render_template("index.html", current_page="main")
@app.route('/menu')
def menu():
    menus = models.Menu.query.all()
    return render_template('menu.html', menus=menus,current_page="menu")
@app.route('/restaurant')
def restaurants():
    restaurants = models.Restaurant.query.all()
    return render_template('restaurant.html', restaurants=restaurants, current_page="restaurant")
@app.route('/order')
def orders():
    orders = models.Orders.query.all()
    return render_template('orders.html', orders=orders,current_page="orders")







@app.route('/menu/add', methods=['POST'])
def add_menu():
    if request.method == 'POST':
        menu = models.Menu(
            dish=request.form['dish'],
            description=request.form['description'],
            price=request.form['price'],
        )
        db.session.add(menu)
        db.session.commit()
        return redirect(url_for('menu'))
    
    
@app.route('/order/add', methods=['POST'])
def add_order():
    if request.method == 'POST':
        order = models.Orders(
            client=request.form['client'],
            Restaurant=request.form['restaurant'],
            compound=request.form['compound'],
            status=request.form['status'],
        )
        db.session.add(order)
        db.session.commit()
        return redirect(url_for('orders'))
    
@app.route('/restaurant/add', methods=['POST'])
def add_restaurant():
    if request.method == 'POST':
        restaurant = models.Restaurant(
            Name=request.form['name'],
            rating=request.form['rating'],
            year_create=request.form['year_create'],
        )
        db.session.add(restaurant)
        db.session.commit()
        return redirect(url_for('restaurants'))
    





@app.route("/menu/<int:id>", methods=["POST", "DELETE"])
def delete_menu(id):
    if request.method == 'POST':
        menu = db.session.query(models.Menu).filter(models.Menu.id == id).first()
        db.session.delete(menu)
        db.session.commit()
        return redirect(url_for('menu'))


@app.route("/order/<int:id>", methods=["POST", "DELETE"])
def delete_order(id):
    if request.method == 'POST':
        order = db.session.query(models.Orders).filter(models.Orders.id == id).first()
        db.session.delete(order)
        db.session.commit()
        return redirect(url_for('orders'))


@app.route("/restaurant/<int:id>", methods=["POST", "DELETE"])
def delete_restaurant(id):
    if request.method == 'POST':
        restaurant = db.session.query(models.Restaurant).filter(models.Restaurant.id == id).first()
        db.session.delete(restaurant)
        db.session.commit()
        return redirect(url_for('restaurants'))



















def main():
    app.run("0.0.0.0", port=8060, debug=True)
if __name__ == "__main__":
    main()