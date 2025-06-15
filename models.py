from extensions import db
class Restaurant(db.Model):
    __tablename__ = 'restaurant'
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.String(100), nullable=False)
    year_create = db.Column(db.Integer)
    def __repr__(self):
        return f'<restaurant {self.title}>'
class Menu(db.Model):
    __tablename__ = 'menu'
    id = db.Column(db.Integer, primary_key=True)
    dish = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer)
    description = db.Column(db.String(100), nullable=False)
    def __repr__(self):
        return f'<menu {self.title}>'
class Orders(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    client = db.Column(db.String(100), nullable=False)
    Restaurant = db.Column(db.String(100), nullable=False)
    compound = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(100), nullable=False)
    def __repr__(self):
        return f'<orders {self.title}>'