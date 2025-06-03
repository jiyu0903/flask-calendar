# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    start_time = db.Column(db.String(100), nullable=False)
    end_time = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'description': self.description
        }
