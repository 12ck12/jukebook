from flask import render_template, request, Flask
import database as db

app = Flask(__name__)

@app.route('/')
def index():
    films = db.get_all_oeuvres()
    return render_template("liste_all_oeuvres.html", films=films)


#essayez d'appeler cette route avec par exemple l'URL : http://127.0.0.1:5000/films_de/13848
#13848 est l'id de Charles Chaplin
@app.route('/ouevres_de_genre/<int:id_real>')
def ouevres_de_genre(id_real):
    print(id_real)
    oeuvres = db.get_films_by(id_real)
    print(films)
    return render_template("liste_films.html", films=films)


   
if __name__ == "__main__":
    app.run()
