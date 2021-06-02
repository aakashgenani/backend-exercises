from flask import make_response, jsonify, request
from app import app, db
from sqlalchemy import func, desc, or_
from models import Book, Author


@app.route('/')
@app.route('/home')
def home():
    return "<h1>Welcome to the books homepage!</h1>"


# 1. Get books (allow filtering by title)
@app.route('/book/title/<string:title>', methods=['GET'])
def get_books_by_title(title):
    books = Book.query.filter(Book.title.like(f'%{title}%')).all()
    return make_response(jsonify(data=[m.serialize() for m in books]), 200)


# 1. Get books (allow filtering by author)
@app.route('/author/<string:author>', methods=['GET'])
def get_books_by_author(author):
    books = Book.query.filter(or_(Book.first_author.like(f'%{author}%'), Book.second_author.like(f'%{author}%'))).all()
    return make_response(jsonify(data=[m.serialize() for m in books]), 200)


# 2. Get Best-selling authors (authors with most books)
@app.route('/author/best', methods=['GET'])
def get_author_most_books():
    books = Book.query.group_by(Book.first_author_rel1).order_by(desc(func.count(Book.first_author))).limit(3)
    return make_response(jsonify(data=[m.serialize()['first_author'] for m in books]), 200)


# 3. Get authors affiliated to a publication
@app.route('/author/publisher/<string:publisher>', methods=['GET'])
def get_authors_by_publisher(publisher):
    authors = Author.query.filter_by(primary_publisher=publisher)
    return make_response(jsonify(data=[m.serialize() for m in authors]), 200)


# 4. Get Books affiliated to a publication
@app.route('/book/publisher/<string:publisher_name>', methods=['GET'])
def get_books_by_publisher(publisher_name):
    books = Book.query.filter_by(publisher=publisher_name).all()
    return make_response(jsonify(data=[m.serialize() for m in books]), 200)


# 5. Get list of authors from a country
@app.route('/author/country/<string:country>', methods=['GET'])
def get_authors_by_country(country):
    authors = Author.query.filter_by(location=country).all()
    return make_response(jsonify(data=[m.serialize() for m in authors]), 200)


# 6. Get books released between a start_date and end_date
@app.route('/book/year/<int:start_year>-<int:end_year>', methods=['GET'])
def get_book_in_year_range(start_year, end_year):
    books = Book.query.filter(Book.year_of_publication < end_year,
                              Book.year_of_publication > start_year).all()
    return make_response(jsonify(data=[m.serialize() for m in books]), 200)


# 7. Add new book
@app.route('/add-book', methods=['POST'])
def insert_book():
    book = Book(title=request.json['title'], first_author=request.json['first_author'],
                second_author=request.json['second_author'], publisher=request.json['publisher'],
                year_of_publication=request.json['year_of_publication'], author_id1=request.json['author_id1'],
                author_id2=request.json['author_id2'], publisher_id=request.json['publisher_id'])
    db.session.add(book)
    db.session.commit()
    return make_response(jsonify(response='OK'), 200)


# 8. Update the telephone number of an author
@app.route('/author/update/<string:author_name>/telephone', methods=['PUT'])
def update_author_telephone(author_name):
    telephone = request.json['telephone']
    author = Author.query.filter_by(name=author_name).first()
    author.telephone = telephone
    db.session.commit()
    return make_response(jsonify(response='OK'), 200)
