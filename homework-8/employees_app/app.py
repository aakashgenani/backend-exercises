from flask import Flask

app = Flask(__name__)

from employees_app import views
