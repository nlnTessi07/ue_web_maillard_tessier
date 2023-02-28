import flask
from flask import Flask
from database.database import db, init_database
from database.models import *


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////home/nolann/PycharmProjects/ue_web_maillard_tessier/database/database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "secret_key1234"

db.init_app(app)

with app.test_request_context():
    init_database()

def clean():
    db.drop_all()
    db.create_all()
    return "Cleaned!"
def add_student():
    return None






@app.route('/' )
def testInput():
    clean()
    #create companies:
    Dassault = Company('Dassault')
    Safran = Company('Safran')
    Labo=Company('Labo')
    Carouf=Company('Carouf')
    CDiscount=Company('CDiscount')
    NASA=Company('NASA')
    ESA=Company('ESA')
    FTX=Company('FTX')
    CreditSuisse=Company('CreditSuisse')
    poliakov = Company('Poliakov (RoryCorporation)')
    db.session.add(poliakov)
    db.session.add(Dassault)
    db.session.add(Safran)
    db.session.add(Labo)
    db.session.add(Carouf)
    db.session.add(CDiscount)
    db.session.add(NASA)
    db.session.add(ESA)
    db.session.add(FTX)
    db.session.add(CreditSuisse)

    db.session.commit()
    companies = Company.query.all()

    #Student creation:
    eleve = Alumni('Bob Marley',
                   'DCL',
                   'TEE',
                   2023,
                   'cigarette',
                   'comment fumer des gens',
                   Dassault,
                   'Momo',
                   'ingenieur_qualité',
                   Safran)
    db.session.add(eleve)
    Dassault.interns.append(eleve)
    Safran.workers.append(eleve)

    db.session.commit()

    #create an Alumni:
    std1 = Alumni(name="Magnus",
                  tafa1="DechetL",
                  tafa2='tktBienspasser',
                  end_year=2021,
                  project_name="Gobblers",
                  project_summary="UwU",
                  project_company=FTX,
                  tutor="absent",
                  current_position="debout",
                  current_company=CreditSuisse
                  )
    std2 = Alumni(name="Magnette",tafa1="DechetL",
                  tafa2="tktBienspasserAussi",
                  end_year=2021,
                  project_name="Morpion",
                  project_summary="UwU",
                  project_company=FTX,
                  tutor="Jesuislà",
                  current_position="assis",
                  current_company=NASA
                  )
    std3 = Alumni(name="Rory Maillard",
                  tafa1="DCL",
                  tafa2="Login",
                  end_year="2024",
                  project_name="LiqueurCafe",
                  project_summary="from10to40degrees",
                  project_company=CreditSuisse,
                  tutor="marty",current_position="influenceur",
                   current_company=Carouf
                  )
    marty = Alumni('Marty',
                   'Arnaud Parion',
                   'Rory Maillard',
                   2026,
                   "objectif traction",
                   'project déjà accomplit',
                   poliakov,
                   'SalmonLePoisson',
                   'BG',
                   CreditSuisse)
    db.session.add(std2)
    db.session.add(std1)
    db.session.add(std3)
    db.session.add(marty)
    db.session.commit()
    print("after student commit")


    #Create proms:
    p2022 = Promo(end_year=2022)
    p2021 = Promo(end_year=2021)
    db.session.add(p2022)
    db.session.add(p2021)
    db.session.commit()

    #add alumnis to p2021:
    p2021.alumnis.append(std1)
    p2021.alumnis.append(std2)
    p2022.alumnis.append(std3)
    db.session.add(p2021)
    db.session.commit()
    print("after proms commit")





    alumnis = Alumni.query.all()
    promos = Promo.query.all()
    return flask.render_template("testPrint.html.jinja2",alumnis=alumnis,promos=promos)

@app.route('/drop')
def drop_page():
    clean()


@app.route('/companies')
def testCompany():
    # Create companies:


    #dassault.list_alumnis_internship.append(std1)
    #poliakov.current_workers.append(std3)
    companies= Company.query.all()
    return flask.render_template("test_print_company.html.jinja2",companies=companies)


@app.route('/admin')
def backToMenu():
    return

if __name__ == '__main__':
    app.run()
