from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://kavi:iit123@localhost/ds'
db = SQLAlchemy(app)

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Rating %r>' % self.id

@app.route('/rating', methods=['POST'])
def rating():
    data = request.form
    rating = int(data['rating'])
    print(rating)

    #rating = random.randint(1,100)
    #insert_to_table(id,rating)

    new_rating = Rating(rating=rating)
    db.session.add(new_rating)
    db.session.commit()

    return ''

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=7000)