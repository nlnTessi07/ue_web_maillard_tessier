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








@app.route('/base' )
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
                   '1950',
                   'cigarette',
                   'comment fumer des gens',
                   Dassault,
                   'Momo',
                   'ingenieur_qualité',
                   Safran)
    db.session.add(bob)
    Dassault.interns.append(bob)
    Safran.workers.append(bob)




    #create an Alumni:
    std1 = Alumni(name="Magnus",
                  tafa2="DechetL",
                  tafa3='tktBienspasser',
                  promo='2021',
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

    std2 = Alumni(name="Magnette",tafa2="DechetL",
                  tafa3="tktBienspasserAussi",
                  promo='2021',
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

    std3 = Alumni(name="Rory Maillard",
                  tafa2="DCL",
                  tafa3="Login",
                  promo='2021',
                  project_name="LiqueurCafe",
                  project_summary="from10to40degrees",
                  project_company=CreditSuisse,
                  tutor="marty",current_position="influenceur",
                   current_company=Carouf
                  )
    db.session.add(std3)
    CreditSuisse.interns.append(std3)
    Carouf.workers.append(std3)

    marty = Alumni('Marty',
                   'Arnaud Parion',
                   'Rory Maillard',
                   2018,
                   "objectif traction",
                   'project déjà accomplit',
                   poliakov,
                   'SalmonLePoisson',
                   'BG',
                   CreditSuisse)
    db.session.add(marty)
    poliakov.interns.append(marty)
    CreditSuisse.workers.append(marty)

    db.session.commit()
    print("after student commit")







    alumnis = Alumni.query.all()
    return flask.render_template("testPrint.html.jinja2",alumnis=alumnis,companies=companies)

@app.route('/drop')
def drop_page():
    clean()


@app.route('/companies')
def testCompany():
    # Create companies:


    companies= Company.query.all()
    return flask.render_template("test_print_company.html.jinja2",companies=companies)


def filtrer(name, tafa2,tafa3, promo, internship_company,current_company):
    #enlever les chanmps vides
    #ordre : nom, taf, promo, entrerpise-stage, entreprise alumni
    interns = db.session.query(Company.interns).filter(Company.name==internship_company)

    return interns.query(Alumni).filter(Alumni.name.contains(name),
                                         Alumni.tafa2.contains(tafa2),
                                     Alumni.tafa3.contains(tafa3),
                                     Alumni.promo.contains(promo))
                                  #   Alumni.current_company.name.contains(current_company))


@app.route('/base',methods=['POST'])
def taMaman():
    name = flask.request.form['testFiltrer']
    print(name)
    ans = filtrer(name,'','','','','')
    print(ans)
    return flask.render_template('testPrint.html.jinja2', ans = ans)

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

