from datetime import datetime

import flask
from flask import Flask
from database.database import db, init_database
from database.models import *
from fun import createBase

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
def getAlumnis(positions, organisations, personnes):
    alumnis_json = db.session.query(Personne.name, Personne.lastName).filter(Personne.promotion<2024).all()
    alumnis = []
    for al in alumnis_json:
        alumnis.append(al[0]+ ' '+al[1])
    return alumnis

def getInformationOf(name,lastName,promotion):

    personne = db.session.query(
        Personne.name,
        Personne.lastName,
        Personne.promotion,
        Personne.genre,
        Personne.dateNaissance)\
        .filter(
        Personne.name.like(name),

        Personne.promotion==promotion).all()
    return personne

def  addEntreprise(nom):
    nvlle_entreprise = Organisation(nom)
    db.session.add(nvlle_entreprise)
    db.session.commit()
    print(nom + "créee")
    return 0

def addPromotion(): ### DEMANDER
    return 0
def addTaf():
    return 0

def getTaf():
    return 0
# retour pour chaque eleve = [name, lastName, dateNaissance, tafa2, tafa2]
def getPromotion(annee):
    promo = db.session.query(Personne.id, Personne.name, Personne.lastName,Personne.dateNaissance).filter(Personne.promotion==annee).all()
    liste_eleves = []
    for eleve in promo:
        caract_eleve = []
        caract_eleve.append(eleve[1]) #prénom
        caract_eleve.appedn(eleve[2]) #nom
        caract_eleve.append(eleve[3]) #dateNaissance
        #Récupération des tafs:
        for taf in TAF:
            print('qsdq')
        tafs_eleve = db.session.query(TAF.name).filter(TAF.personnes.id==eleve[0]).all()


        liste_eleves.append(caract_eleve)
    return liste_eleves
def modifyPromotion(eleve):
    return 0

#filtres :

# modifier les 4 (enlever de la promotion
def addStudent(name,lastname,genre,annee,mois,jour,promotion,annee2,annee3):
    return 0

@app.route('/test')
def test():
    return db.session.query(TAF.name).filter(TAF.personnes.id==2).all()
@app.route('/clean')
def routeClean():
    clean()
    return 'Database Cleaned'
@app.route('/testadd')
def routeAdd():

    addEntreprise('QMSDJKQSDJ')

    db.session.commit()
    return 'blalba'


@app.route('/testbdd')
def testbdd2():
    organisations, positions, pfes, tafs, personnes = createBase()
    alumnis = getAlumnis(positions,organisations,personnes)
    testp = getInformationOf('Rory', '',2024)

    return(flask.render_template('testPrint.html.jinja2', organisations=organisations,positions=positions,pfes=pfes,tafs=tafs,personnes=personnes,alumnis=alumnis, testp=testp))
"""
@app.route('/old' )
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

    return flask.render_template("testPrint.html.jinja2",organisations=organisations,
                                 positions=positions,
                                 pfes=pfes,
                                 tafs = tafs,
                                 personnes=personnes)
"""
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

