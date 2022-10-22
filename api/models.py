from database import db, ma

class Individual(db.Model):
    __tablename__ = "individual"

    id = db.Column(db.Integer, primary_key=True)
    forenames = db.Column(db.Text)
    surname = db.Column(db.Text)
    fullname = db.Column(db.Text)
    gender = db.Column(db.Text)
    dob = db.Column(db.Date)
    dod = db.Column(db.Date)
    age = db.Column(db.Integer)

    def __init__(self, **kwargs):
        super(Individual, self).__init__(**kwargs)