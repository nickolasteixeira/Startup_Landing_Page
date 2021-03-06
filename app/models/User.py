from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), index=True, unique=False)
    last_name = db.Column(db.String(64), index=True, unique=False)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    # Producer for User from json (dict). Expects password in plaintext and hashes
    @classmethod
    def from_json(cls, json):
        return cls(first_name=json['first_name'],
                   last_name=json['last_name'],
                   email=json['email'],
                   password_hash=generate_password_hash(json['password']))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

