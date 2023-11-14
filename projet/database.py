import sqlite3

DBNAME = "projet.db"

def _select(requete, params=None):
    """ Exécute une requête type select"""
    with sqlite3.connect(DBNAME) as db:
        c = db.cursor()
        if params is None:
            c.execute(requete)
        else:
            c.execute(requete, params)
        res = c.fetchall()
    return res


def oeuvres_de_genre(id_genre):
    requete = """select oeuvre.titre, genre.nom
                        from oeuvre, genre
                        where oeuvre.id_Genre=? and oeuvre.id_Genre=genre.id
                        order by oeuvre.titre asc"""
    return _select(requete, params=(id_genre,))

def get_all_oeuvres():
    requete = """select oeuvre.titre, genre.nom, genre.id, oeuvre.id_Artiste, (SELECT artiste.nom from artiste WHERE oeuvre.id_Artiste=artiste.id), oeuvre.id_type, (SELECT type.oeuvre from type WHERE oeuvre.id_Type=type.id)
                        from oeuvre inner join genre on oeuvre.id_Genre=genre.id"""
    return _select(requete)

def get_all_artistes():
    requete="""select artiste.nom, type.artiste, type.id
                        from artiste inner join type on artiste.id_type=type.id"""
    return _select(requete)
def get_all_genres():
    requete="""select genre.nom, type.oeuvre, type.id
                        from genre inner join type on genre.id_type=type.id"""
    return _select(requete)
def get_all_keys():
    requete="""select keywords.id, keywords.KeyMusique, keywords.KeyLivre
                        from keywords"""
    return _select(requete)
def get_cars():
    requete="""SELECT acommecaracteristique.id_Oeuvre, oeuvre.titre, oeuvre.id, acommecaracteristique.id_Keywords, (SELECT Keywords.KeyMusique from Keywords WHERE acommecaracteristique.id_Keywords=Keywords.id AND oeuvre.id_type=1), (SELECT Keywords.KeyLivre from Keywords WHERE acommecaracteristique.id_Keywords=keywords.id AND oeuvre.id_type=2) 
                        from acommecaracteristique inner join oeuvre on acommecaracteristique.id_Oeuvre=oeuvre.id"""
    return _select(requete)

def oeuvres_de_genre(id_genre):
    requete = """select oeuvre.titre, oeuvre.id_Artiste, (SELECT artiste.nom FROM Artiste WHERE artiste.id=oeuvre.id_Artiste), (SELECT genre.nom FROM genre WHERE genre.id=oeuvre.id_genre)
                        from oeuvre, artiste, genre where artiste.id=oeuvre.id_artiste AND genre.id=oeuvre.id_Genre AND oeuvre.id_genre=?
                        order by oeuvre.titre"""
    return _select(requete, params=(id_genre,))
def oeuvres_de_type(id_type):
    requete = """select oeuvre.titre, oeuvre.id_Artiste, (SELECT artiste.nom FROM Artiste WHERE artiste.id=oeuvre.id_Artiste), (SELECT type.oeuvre FROM Type WHERE type.id=oeuvre.id_type), (SELECT genre.nom FROM Genre WHERE oeuvre.id_genre=genre.id)
                        from oeuvre, artiste, genre, type where artiste.id=oeuvre.id_artiste AND genre.id=oeuvre.id_Genre AND type.id=oeuvre.id_type AND oeuvre.id_type=?
                        order by oeuvre.titre"""
    return _select(requete, params=(id_type,))

def get_all_cars():
    requete="""select acommecaracteristique.id_Oeuvre, acommecaracteristique.id_Keywords
                        from acommecaracteristique"""