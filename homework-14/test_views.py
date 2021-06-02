import pytest
import os
from app import app, db
import models


@pytest.fixture
def client():
    """
    Create a temporary db with some data in it for using in the tests.
    """
    app.config["TESTING"] = True
    app.testing = True

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"

    client = app.test_client()
    with app.app_context():
        db.create_all()
        book = models.Book('Letters to a Young Contrarian', 'Christopher Hitchens', None,
                           'Basic Books', 2003, 1, None, 1)
        publisher = models.Publisher('Basic Books', None, None, 1950)
        author = models.Author('Christopher Hitchens', 1949, 'England', None, 'Basic Books')
        db.session.add(book)
        db.session.add(author)
        db.session.add(publisher)
        db.session.commit()
    yield client

    with app.app_context():
        db.session.remove()
        db.drop_all()
        os.remove('test.db')


def test_update_author_telephone(client):
    response = client.put("/author/update/Christopher Hitchens/telephone", json={"telephone": "123456"})
    assert response.json == {"response": "OK"}
    author = models.Author.query.filter_by(name='Christopher Hitchens').first()
    assert author.telephone == "123456"


def test_insert_book(client):
    response = client.post("/add-book", json={"title": "Letters to a Young Contrarian",
                                              "first_author": "Christopher Hitchens",
                                              "second_author": None, "publisher": "Basic Books",
                                              "year_of_publication": 2003, "author_id1": 1, "author_id2": None,
                                              "publisher_id": 1})
    assert response.json == {"response": "OK"}
    author = models.Author.query.filter_by(name='Christopher Hitchens').first()
    assert author.name == "Christopher Hitchens"


def test_get_book_in_year_range(client):
    response = client.get("/book/year/2002-2004")
    assert response.json['data'][0]['year_of_publication'] == '2003'


def test_get_authors_by_country(client):
    response = client.get("/author/country/England")
    for i in range(len(response.json['data'])):
        assert response.json['data'][i]['location'] == 'England'


def test_get_books_by_publisher(client):
    response = client.get("/book/publisher/Basic Books")
    for i in range(len(response.json['data'])):
        assert response.json['data'][i]['publisher'] == 'Basic Books'


def test_get_authors_by_publisher(client):
    response = client.get("/author/publisher/Basic Books")
    for i in range(len(response.json['data'])):
        assert response.json['data'][i]['primary_publisher'] == 'Basic Books'


def test_get_books_by_author(client):
    response = client.get("/author/Christopher Hitchens")
    for i in range(len(response.json['data'])):
        assert response.json['data'][i]['first_author'] == 'Christopher Hitchens'


def test_get_books_by_title(client):
    response = client.get("/book/title/Letters to a Young Contrarian")
    for i in range(len(response.json['data'])):
        assert response.json['data'][i]['title'] == 'Letters to a Young Contrarian'
