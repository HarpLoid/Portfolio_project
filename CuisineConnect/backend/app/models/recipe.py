from app.db import db
from datetime import datetime


class Recipe(db.Model):
    """Recipe Model for Database Table"""
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    ingredients = db.Column(db.Text, nullable=True)
    instructions = db.Column(db.Text, nullable=True)
    timestamp = db.Column(db.DateTime, default=datetime.now())
    likes = db.relationship('Like', backref='recipe',
                            lazy=True, cascade="all, delete-orphan")
    comments = db.relationship('Comment', backref='recipe',
                               lazy=True, cascade="all, delete-orphan")
