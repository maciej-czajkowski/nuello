import json

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
#                                                        change below if address differs
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:admin@localhost:5432/postgres"
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class TablesModel(db.Model):
    __tablename__ = 'tables'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return '<Table %r, %r>' % (self.id, self.name)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/tables', methods=['GET'])
def get_tables():
    if request.method == "GET":
        tables = TablesModel.query.all()
        results = [
            {
                "id": table.id,
                "name": table.name,
            } for table in tables ]

        return json.dumps(results)


if __name__ == '__main__':
    app.run()
