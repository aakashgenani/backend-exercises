from app import db


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    year_of_birth = db.Column(db.Integer, nullable=True)
    location = db.Column(db.String(80), nullable=True)
    telephone = db.Column(db.String(80), unique=True, nullable=True)
    primary_publisher = db.Column(db.String(80), nullable=True)

    def __init__(self, name, year_of_birth, location, telephone, primary_publisher):
        self.name = name
        self.year_of_birth = year_of_birth
        self.location = location
        self.telephone = telephone
        self.primary_publisher = primary_publisher

    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'name': self.name,
            'year_of_birth': self.year_of_birth,
            'location': self.location,
            'telephone': self.telephone,
            'primary_publisher': self.primary_publisher,
        }


class Publisher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    location = db.Column(db.String(80), nullable=True)
    telephone = db.Column(db.String(80), unique=True, nullable=True)
    founding_year = db.Column(db.Integer, nullable=False)

    def __init__(self, name, location, telephone, founding_year):
        self.name = name
        self.location = location
        self.telephone = telephone
        self.founding_year = founding_year

    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'name': self.name,
            'location': self.location,
            'telephone': self.telephone,
            'founding_year': self.founding_year,
        }


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    first_author = db.Column(db.String(80), nullable=False)
    second_author = db.Column(db.String(80), nullable=True)
    publisher = db.Column(db.String(80), nullable=True)
    year_of_publication = db.Column(db.String(80), nullable=True)

    author_id1 = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    author_rel1 = db.relationship('Author', foreign_keys='Book.author_id1')
    author_id2 = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=True)
    author_rel2 = db.relationship('Author', foreign_keys='Book.author_id2')
    publisher_id = db.Column(db.Integer, db.ForeignKey('publisher.id'), nullable=True)
    publisher_rel = db.relationship('Publisher', foreign_keys='Book.publisher_id')

    def __init__(self, title, first_author, second_author, publisher, year_of_publication, author_id1,
                 author_id2, publisher_id):
        self.title = title
        self.first_author = first_author
        self.second_author = second_author
        self.publisher = publisher
        self.year_of_publication = year_of_publication
        self.author_id1 = author_id1
        self.author_id2 = author_id2
        self.publisher_id = publisher_id

    def __repr__(self):
        return f"{self.title}, {self.first_author}, {self.second_author}, {self.publisher}"

    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'title': self.title,
            'first_author': self.first_author,
            'second_author': self.second_author,
            'publisher': self.publisher,
        }
