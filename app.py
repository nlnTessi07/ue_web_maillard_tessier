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








@app.route('/' )
def testInput():
    clean()

    # CREATION DES ORGANISATIONS:
    Dassault = Organisation('Dassault')
    Safran = Organisation('Safran')
    Labo=Organisation('Labo')
    Carouf=Organisation('Carouf')
    CDiscount=Organisation('CDiscount')
    NASA=Organisation('NASA')
    ESA=Organisation('ESA')
    FTX=Organisation('FTX')
    CreditSuisse=Organisation('CreditSuisse')
    poliakov = Organisation('Poliakov (RoryCorporation)')
    edf = Organisation('EDF')
    engie = Organisation('ENGIE')
    total = Organisation('TotalEnergie')
    imt = Organisation('IMT-Atlantique')


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
    db.session.add(imt)

    db.session.commit()
    organisations = Organisation.query.all()   ### AFFICHAGE OK

    # CREATION POSITIONS
    inge_nuc = Position('inge_nuc')
    inge_bat = Position('inge_bat')
    inge_info = Position('inge_info')
    patron = Position('patron')
    etudiant = Position('etudiant')
    chercheur = Position('chercheur')
    enseignant = Position('enseignant')
    tuteur = Position('tuteur')
    RH = Position('RH (707574650a)')
    stagiaire_pfe = Position('stagiaire_pfe')

    db.session.add(inge_nuc)
    db.session.add(inge_bat)
    db.session.add(inge_info)
    db.session.add(patron)
    db.session.add(etudiant)
    db.session.add(chercheur)
    db.session.add(enseignant)
    db.session.add(tuteur)
    db.session.add(RH)
    db.session.add(stagiaire_pfe)

    db.session.commit()
    positions = Position.query.all()    ### AFFICHAGE OK

    # LIEN POSITIONS/ORGANISATION
    imt.postes.append(enseignant)
    imt.postes.append(chercheur)
    imt.postes.append(etudiant)

    edf.postes.append(inge_bat)
    edf.postes.append(inge_nuc)
    edf.postes.append(inge_info)
    edf.postes.append(chercheur)
    edf.postes.append(tuteur)
    edf.postes.append(RH)

    poliakov.postes.append(patron)
    poliakov.postes.append(tuteur)  ### Affichage OK

    # CREATION PFE
    crabes = PFE('crabes','Je veux manger des baleresques toute l annee voila le projet.')
    plancton = PFE('plancton', 'Je veux que les baleines ne s echouent psa psq cest chiant woula')
    chaussettes = PFE('chaussettes', 'J ai froid svp remettez le chauffage °_°')
    chuckNorris = PFE('chuckNorris', 'ATTAATATATATATATAAATA !!!!!!!!!!!!')

    db.session.add(crabes)
    db.session.add(plancton)
    db.session.add(chaussettes)
    db.session.add(chuckNorris)

    db.session.commit()
    pfes = PFE.query.all()  ### AFFICHAGE OK

    # CREATION TAFs
    dcl = TAF('DCL')
    login = TAF('Login')
    ascii = TAF('ascii')
    demain = TAF('demain')
    nemo = TAF('nemo')
    TEE = TAF('TEEH')
    sheesh = TAF('sheesh')
    cyber = TAF('cyber')

    db.session.add(dcl)
    db.session.add(login)
    db.session.add(ascii)
    db.session.add(demain)
    db.session.add(nemo)
    db.session.add(TEE)
    db.session.add(sheesh)
    db.session.add(cyber)

    db.session.commit()
    tafs = TAF.query.all() ### Affichage OK

    # CREATION PERSONNES
    tom= Personne('tom')
    rory = Personne('rory')
    marty= Personne('marty')
    alexis= Personne('alexis')
    julien= Personne('julien')
    eugenie= Personne('eugenie')
    raoul= Personne('raoul')
    theo = Personne('theo')

    db.session.add(tom)
    db.session.add(rory)
    db.session.add(marty)
    db.session.add(alexis)
    db.session.add(julien)
    db.session.add(eugenie)
    db.session.add(raoul)
    db.session.add(theo)

    db.session.commit()
    personnes = Personne.query.all()

    # LIEN PFE/PERSONNES
    inge_info.personnes.append(rory)
    inge_info.personnes.append(alexis)
    inge_info.personnes.append(julien)
    etudiant.personnes.append(eugenie)
    etudiant.personnes.append(tom)
    enseignant.personnes.append(theo)
    tuteur.personnes.append(raoul)
    inge_bat.personnes.append(marty)
    etudiant.personnes.append(marty)
    db.session.commit() ### AFFICHAGE OK


    # LIEN TAFs PERSONNES
    dcl.personnes.append(rory)
    dcl.personnes.append(alexis)
    dcl.personnes.append(eugenie)
    login.personnes.append(marty)
    ascii.personnes.append(tom)
    demain.personnes.append(julien)
    TEE.personnes.append(raoul)
    sheesh.personnes.append(raoul)

    db.session.commit() ### AFFICHAGE OK


    # LIEN POSITIONS PERSONNES
    # LIEN PERSONNES/POSITION (poste)
    # LIEN
    """
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
    """
    return flask.render_template("testPrint.html.jinja2",organisations=organisations,
                                 positions=positions,
                                 pfes=pfes,
                                 tafs = tafs,
                                 personnes=personnes)

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
def TestFilter():
    name = flask.request.form['testFiltrer']
    print(name)
    ans = filtrer(name,'','','','','')
    print(ans)
    return flask.render_template('testPrint.html.jinja2', ans = ans)

@app.route('/login')
def loginMain():
    return flask.render_template('loginMain.html.jinja2')

@app.route('/loginUser')
def loginUser():
    return flask.render_template('loginUser.html.jinja2')

@app.route('/loginAdmin')
def loginAdmin():
    return flask.render_template('loginAdmin.html.jinja2')

@app.route('/loginUser', methods=['POST'])
def loginUserPost():
    return flask.redirect('/UserDashboard')

@app.route('/loginAdmin', methods=['POST'])
def loginAdminPost():
    return flask.redirect('/AdminDashboard')
@app.route('/UserDashboard')
def userDashboard():
    return flask.render_template('userDashboard.html.jinja2')

@app.route('/AdminDashboard')
def adminDashboard():
    return flask.render_template('adminDashboard.html.jinja2')
@app.route('/UserDashboard',methods=["POST"])
def userDashboardPost():
    if 'modifier' in flask.request.form:
        return flask.redirect('/UserModif')
    elif 'rechercher' in flask.request.form:
        name = flask.request.form['name']
        taf1 = flask.request.form['taf1']
        taf2 = flask.request.form['taf2']
        promo = flask.request.form['promo']
        stage = flask.request.form['stage']
        entreprise = flask.request.form['entreprise']
        resultats = filtrer(name,taf1,taf2,promo,stage,entreprise)
        return flask.render_template('resultat.html.jinja2',name=name, taf1=taf1,taf2=taf2,promo=promo,stage=stage,entreprise=entreprise)


@app.route('/UserModif')
def userModif():
    return flask.render_template('modifUserData.jinja2')

@app.route('/UserModif',methods=["POST"])
def userModifPost():
    return()

@app.route('/AdminDashboard',methods=["POST"])
def adminRecherchePost():
    if 'modifier' in flask.request.form:
        return flask.redirect('/UserModif')
    elif 'ajouterEtudiant' in flask.request.form:
        return flask.redirect('/StudentAdd')
    elif 'modifEtudiant' in flask.request.form:
        return flask.redirect('/StudentFind')
    elif 'rechercher' in flask.request.form:
        name = flask.request.form['name']
        taf1 = flask.request.form['taf1']
        taf2 = flask.request.form['taf2']
        promo = flask.request.form['promo']
        stage = flask.request.form['stage']
        entreprise = flask.request.form['entreprise']
        resultats = filtrer(name,taf1,taf2,promo,stage,entreprise)
        return flask.render_template('resultat.html.jinja2',name=name, taf1=taf1,taf2=taf2,promo=promo,stage=stage,entreprise=entreprise)

@app.route('/StudentAdd')
def addStudent():
    return flask.render_template('createStudent.jinja2')

@app.route('/StudentFind')
def findStudent():
    return flask.render_template('findStudent.jinja2')

if __name__ == '__main__':
    app.run()

