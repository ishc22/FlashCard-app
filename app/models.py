from app import db, login 
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# ***EX:
# user1 = db.sessions.get(User, 1)  (gets the information from user with the the id of one.)
# user1.email   (will return the email.
# user1.decks.deckname (will return the deck names stored. looks at relationship)

# EX: deck1 = db.session.get(Deck, 1)
# deck1.
#deck1.user.email  (has to do with the relationship between user and deck, will return user)

 
#  user mixin, is a class from login_manager for getting the user id to validate other routes. will look at usermixin for get id
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(500), nullable=False, unique=True)
    password = db.Column(db.String(1000), nullable=False)
    #to be able to get the user from the posts.
    decks = db.relationship('Deck', backref='user', lazy=True)
    # cards = db.relationship('Card', backref='user', lazy=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.password = generate_password_hash(kwargs.get('password'))
        # automatically add user to database
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"<User {self.id}|{self.username}>"

    def check_password(self, password_guess):
        return check_password_hash(self.password, password_guess)
    

# when called stores id in session and returns user object or none.
@login.user_loader
def get_user_by_id(user_id):
    return db.session.get(User, user_id)

################################################################################################################################################################################################
 
class Deck(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    deck_name = db.Column(db.String(200), nullable=False)
    #to be able to get the deck from the cards.
    cards = db.relationship('Card', backref='deck', lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # automatically add user to database
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"<Deck {self.id}|{self.deck_name}>"
    
    # def to_dict(self):
    #     return {
    #         'id': self.id,
    #         'deck_name': self.deck_name,
    #         'user_id': self.user_id }

################################################################################################################################################################################################

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(800), nullable=False)
    answer = db.Column(db.Text, default=False, nullable=False)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    deck_id = db.Column(db.Integer, db.ForeignKey('deck.id'), nullable=False)


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # automatically add user to database
        db.session.add(self)
        db.session.commit()             

    def __repr__(self):
        return f"<Card {self.id}|{self.answer}|{self.question}>"
  

    # def to_dict(self):
    #     return {
    #         'id': self.id,
    #         'question': self.question,
    #         'answer': self.answer,
    #         'deck_id': self.deck_id
    #     }

