import flask
from flask import Flask
from database.database import db, init_database
from database.models import *


app = Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////home/nolann/PycharmProjects/ue_web_maillard_tessier/database/database.db"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///E:\\Documents\\Programming\\Python\\ue_web_maillard_tessier\\database\\database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "secret_key1234"

db.init_app(app)

with app.test_request_context():
    init_database()

def clean():
    db.drop_all()
    db.create_all()
    return "Cleaned!"
def add_student(nom,tafa2,tafa3,end_year,projet,des_projet,entreprise_projet,tuteur,post_actuel,entreprise_actuelle):
    promos = Promo.query.all()
    existing_years = db.session.query(promos.end_year).all()
    if existing_years.contains(end_year):
        std_promo=db.session.query(promos).filter(Promo.end_year==end_year)
        std = Alumni(nom,
                 tafa2,
                 tafa3,
                 std_promo,
                 projet,
                 des_projet,
                 entreprise_projet,
                 tuteur,
                 post_actuel,
                 entreprise_actuelle,
                 )
        db.session.add(std)
        std_promo.alumnis.alappend(std)
        entreprise_projet.interns.append(std)
        db.session.commit()








@app.route('/base' )
def testInput():
    clean()
    #Create proms:
    p2022 = Promo(end_year=2022)
    p2021 = Promo(end_year=2021)
    p2020 = Promo(end_year=2020)
    p2019 = Promo(end_year=2019)
    p2018 = Promo(end_year=2018)
    p2017 = Promo(end_year=2017)
    p2005 = Promo(end_year=2005)
    p1950 = Promo(end_year=1950)
    p2000 = Promo(end_year=2000)
    db.session.add(p2022)
    db.session.add(p2021)
    db.session.add(p2020)
    db.session.add(p2019)
    db.session.add(p2018)
    db.session.add(p2017)
    db.session.add(p2005)
    db.session.add(p1950)
    db.session.add(p2000)
    db.session.commit()

    promos = Promo.query.all()



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
    edf = Company('EDF')
    engie = Company('ENGIE')
    total = Company('TotalEnergie')


    db.session.add(edf)
    db.session.add(engie)
    db.session.add(total)
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
    bob = Alumni('Bob Marley',
                   'TEE',
                   'TEE*',
                   p1950,
                   'cigarette',
                   'comment fumer des gens',
                   Dassault,
                   'Momo',
                   'ingenieur_qualité',
                   Safran)
    db.session.add(bob)
    Dassault.interns.append(bob)
    Safran.workers.append(bob)
    p1950.alumnis.append(bob)




    #create an Alumni:
    std1 = Alumni(name="Magnus",
                  tafa2="DechetL",
                  tafa3='tktBienspasser',
                  end_year=p2021,
                  project_name="Gobblers",
                  project_summary="UwU",
                  project_company=FTX,
                  tutor="absent",
                  current_position="debout",
                  current_company=CreditSuisse
                  )
    db.session.add(std1)
    FTX.interns.append(std1)
    CreditSuisse.workers.append(std1)
    p2021.alumnis.append(std1)

    std2 = Alumni(name="Magnette",tafa2="DechetL",
                  tafa3="tktBienspasserAussi",
                  end_year=p2021,
                  project_name="Morpion",
                  project_summary="UwU",
                  project_company=FTX,
                  tutor="Jesuislà",
                  current_position="assis",
                  current_company=NASA
                  )
    db.session.add(std2)
    FTX.interns.append(std2)
    NASA.workers.append(std2)
    p2021.alumnis.append(std2)

    std3 = Alumni(name="Rory Maillard",
                  tafa2="DCL",
                  tafa3="Login",
                  end_year=p2021,
                  project_name="LiqueurCafe",
                  project_summary="from10to40degrees",
                  project_company=CreditSuisse,
                  tutor="marty",current_position="influenceur",
                   current_company=Carouf
                  )
    db.session.add(std3)
    CreditSuisse.interns.append(std3)
    Carouf.workers.append(std3)
    p2021.alumnis.append(std3)

    marty = Alumni('Marty',
                   'Arnaud Parion',
                   'Rory Maillard',
                   p2018,
                   "objectif traction",
                   'project déjà accomplit',
                   poliakov,
                   'SalmonLePoisson',
                   'BG',
                   CreditSuisse)
    db.session.add(marty)
    poliakov.interns.append(marty)
    CreditSuisse.workers.append(marty)
    p2018.alumnis.append(marty)

    db.session.commit()
    print("after student commit")







    alumnis = Alumni.query.all()
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
def testAdmin():
    a = testInput
    return('hello')

def filtrer(name, tafa2,tafa3, promo, intership_company,current_company):
    #enlever les chanmps vides
    #ordre : nom, taf, promo, entrerpise-stage, entreprise alumni
    return db.session.query(Alumni).filter(Alumni.name.contains(name),
                                           Alumni.tafa2.contains(tafa2),
                                           Alumni.tafa3.contains(tafa3),
                                           Alumni.promo.contains(promo),
                                           Alumni.internship_company.contains(intership_company),
                                           Alumni.current_company.contains(current_company))
  #test
@app.route('/menu')
def menu():
    return flask.render_template("mainMenu.html.jinja2")

@app.route('/menu', methods=['POST'])
def loginPost():
    flask.redirect(flask.url_for("recherche"))
@app.route('/recherche')
def recherche():
    return flask.render_template("main_layout.html.jinja2")

@app.route('/recherche',methods=["POST"])
def recherchePost():
    name = flask.request.form['name']
    taf1 = flask.request.form['taf1']
    taf2 = flask.request.form['taf2']
    promo = flask.request.form['promo']
    stage = flask.request.form['stage']
    entreprise = flask.request.form['entreprise']
    resultats = filtrer(name,taf1,taf2,promo,stage,entreprise)
    return flask.render_template("resultat.html.jinja2",name=name, taf1=taf1,taf2=taf2,promo=promo,stage=stage,entreprise=entreprise)
if __name__ == '__main__':
    app.run()

