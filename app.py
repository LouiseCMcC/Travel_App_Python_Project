from flask import Flask, render_template

from controllers.city_controller import cities_blueprint
from controllers.country_controller import countries_blueprint
from controllers.sight_controller import sights_blueprint
from controllers.blog_controller import blogs_blueprint
from controllers.photo_controller import photos_blueprint

app = Flask(__name__)

app.register_blueprint(cities_blueprint)
app.register_blueprint(countries_blueprint)
app.register_blueprint(sights_blueprint)
app.register_blueprint(blogs_blueprint)
app.register_blueprint(photos_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)



