from app import db


class BetaEmailSubscriber(db.Model):
    __tablename__ = "beta_email_subscribers"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), index=True, unique=False)
    last_name = db.Column(db.String(64), index=True, unique=False)
    email = db.Column(db.String(120), index=True, unique=True)

    @classmethod
    def from_json(cls, json):
        return cls(first_name=json['first_name'],
                   last_name=json['last_name'],
                   email=json['email'])

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __repr__(self):
        return "beta email subscriber: " + \
               self.first_name + " " + \
               self.last_name + " -> " + \
               self.email
