from app.store.database.models import db


class InfoAboutDevice(db.Model):

    __tablename__ = 'aboutdevice'

    id = db.Column(db.Integer, primary_key=True)
    devicetype = db.Column(db.Unicode)
    manufacture = db.Column(db.Unicode)
    model = db.Column(db.Unicode)
    storage = db.Column(db.Integer)
    grade_a = db.Column(db.Float)
    grade_b = db.Column(db.Float)
    grade_c = db.Column(db.Float)
    grade_d = db.Column(db.Float)


class Users(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.Unicode)
    password = db.Column(db.Unicode)


