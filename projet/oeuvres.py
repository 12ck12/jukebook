from flask import render_template, request, Flask
import database as db

app = Flask(__name__)

@app.route('/')
def index():
    oeuvres = db.get_all_oeuvres()
    return render_template("liste_all_oeuvres.html", oeuvres=oeuvres)
@app.route('/admin_artistes')
def artistes():
    artistes=db.get_all_artistes()
    return render_template("liste_all_artistes.html", artistes=artistes)

@app.route('/admin_genres')
def genres():
    genres=db.get_all_genres()
    return render_template("liste_all_genres.html", genres=genres)
@app.route('/admin_keywords')
def keys():
    keys=db.get_all_keys()
    return render_template("liste_all_keys.html", keys=keys)
@app.route('/admin_caracteristiques')
def all_cars():
    cars=db.get_all_cars()
    return render_template("liste_all_cars.html", cars=cars)
@app.route('/caracteristiques')
def car():
    car=db.get_cars()
    return render_template("liste_cars.html", car=car)
# undone
@app.route('/oeuvres_de_genre/<int:id_genre>')
def ouevres_de_genre(id_genre):
    print(id_genre)
    oeuvres = db.oeuvres_de_genre(id_genre)
    print(oeuvres)
    return render_template("liste_oeuvres_genre.html", oeuvres=oeuvres)
@app.route('/oeuvres_de_type/<int:id_type>')
def oeuvres_de_type(id_type):
    print(id_type)
    oeuvres=db.oeuvres_de_type(id_type)
    print(oeuvres)
    return render_template('liste_oeuvres.html', oeuvres=oeuvres)


   
if __name__ == "__main__":
    app.run(debug=True)
