from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://kavi:iit123@database:3306/ds'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)
print('Hello')
print(db)

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(40), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Rating %r>' % self.id

@app.route('/rating', methods=['POST'])
def rating():
    data = request.form
    location = data['location']
    rating = int(data['rating'])
    print(rating)

    #rating = random.randint(1,100)
    #insert_to_table(id,rating)

    new_rating = Rating(rating=rating, location=location)
    #new_rating = Rating(rating=rating)
    db.session.add(new_rating)
    db.session.commit()

    return str(db.session)

if __name__ == "__main__":
    #db.create_all()
    app.run(debug=True, host="0.0.0.0", port=7000)