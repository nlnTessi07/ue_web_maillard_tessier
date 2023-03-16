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
#OK------------------------------------------------------------------------------
def getAlumnis(positions, organisations, personnes):
    alumnis = db.session.query(Personne).filter(Personne.promotion<2024).all()
    return alumnis
#OK------------------------------------------------------------------------------
def getStageById(id):
    stages = db.session.query(PFE).all()
    for stage in stages:
        if stage.eleve.id == id:
            return stage
#OK------------------------------------------------------------------------------
def getPositionById(id):
    position = Position.query.join(Personne).filter(Personne.id==id).all()
    return position
#OK------------------------------------------------------------------------------
def getOrganisationById(id):
    organisation = Organisation.query.join(Personne).filter(Personne.id==id).all()
    return organisation
#OK------------------------------------------------------------------------------
def getOrganisations(): # [[Organisation, nombre gens]]
    organisations =  db.session.query(Organisation).all()
    liste_orga = [[] for i in range(len(organisations))]
    for i in range(len(organisations)):
        liste_orga[i].append(organisations[i])
        liste_orga[i].append(getNEntreprise(None,None,organisations[i]))
    return liste_orga
#OK------------------------------------------------------------------------------
def getPersonnesOrganisation(id):
    entreprise = db.session.query(Organisation).filter(Organisation.id==id).first()
    travailleurs = entreprise.personnes
    personnes=[]
    for personne in travailleurs:
        personnes.append([personne, personne.annee_position, getPositionById(personne.id)])
    return [entreprise, personnes]

def getTuteurByStudentId(id):
    pfe = db.session.query(PFE).filter(PFE.eleve_id==id).first()
    if pfe != None:
        return pfe.tuteur.name + pfe.tuteur.lastName
    return ""

def getList(id,name,lastName,promotion,taf1,taf2,entreprise_stage,tuteur,position,entreprise):
    #id, name, lastName, promotion, taf1, taf2, nomPfe, EtatCivil
    personnes = db.session.query(Personne.id, Personne.name, Personne.lastName, Personne.promotion, Personne.genre,Personne.dateNaissance)
    if(id):
        personnes = personnes.filter(Personne.id==id).all()
    if(promotion):
        personnes = personnes.filter(Personne.promotion==promotion).all()
    if(name):
        personnes = personnes.filter(Personne.name.contains(name)).all()
    if(lastName):
        personnes = personnes.filter(Personne.lastName.contains(lastName)).all()
    #remise en forme des données et ajout des tafs :
    liste_personnes = []

    for p in personnes:
        personne = []
        tafs = getTaf(p.id)

        personne.append(p.id)
        personne.append(p.name)
        personne.append(p.lastName)
        personne.append((p.promotion))
        for taf in tafs:
            personne.append(taf)
        personne.append(p.genre)
        personne.append(getOrganisationById(p.id))
        personne.append(getPositionById(p.id))
        personne.append(getStageById(p.id))
        personne.append(p.dateNaissance)
        # stage, tuteur de stage, pfe, description du pfe
        liste_personnes.append(personne)


    #Avec les données remises en forme on continue avec les filtres des tafs si les champs sont rentrés:
    if(taf1):
        nouvelle_liste = []
        for p in (liste_personnes):
                if taf1.lower() in str(p[4:6]).lower():
                    nouvelle_liste.append(p)
        liste_personnes = nouvelle_liste

    if (entreprise_stage):
        nouvelle_liste=[]
        for p in (liste_personnes):
            if personne[9]!=None:
                entr= personne[9].entreprise_stage
                if entreprise_stage.lower() in entr.name.lower():
                    nouvelle_liste.append(p)
        liste_personnes=nouvelle_liste
    if (tuteur):
        nouvelle_liste=[]
        for p in liste_personnes:
            if tuteur.lower() in getTuteurByStudentId(p[0]).lower():
                nouvelle_liste.append(p)
        liste_personnes=nouvelle_liste
    if (entreprise):
        nouvelle_liste=[]
        for p in liste_personnes:
            if entreprise in p[7][0].name.lower():
                nouvelle_liste.append(p)
        liste_personnes= nouvelle_liste

    if (position):
        nouvelle_liste=[]
        for p in liste_personnes:
            if position.lower() in p[8][0].titre.lower():
                nouvelle_liste.append(p)
        liste_personnes= nouvelle_liste
    return liste_personnes
#OK------------------------------------------------------------------------------
def  addEntreprise(nom):
    nvlle_entreprise = Organisation(nom)
    db.session.add(nvlle_entreprise)
    db.session.commit()
    print(nom + "créee")
    return 0
#OK
def addTaf(nom):
    new_taf = TAF(nom)
    db.session.add(new_taf)
    db.session.commit()
    return 0
#OK
def getTaf(eleve_id):
    tafs = db.session.query(TAF).all()
    res = []
    for taf in tafs:
        for p in taf.personnes:
            if p.id==eleve_id:
                res.append(taf)
    if len(res)==0:
        res.append('')
        res.append('')
    if len(res)==1:
        res.append('')
    return res
def getTafs():
    tafs = db.session.query(TAF).all()
    liste_tafs = [[] for i in range(len(tafs))]
    for i in range(len(tafs)):
        liste_tafs[i].append(tafs[i])
        liste_tafs[i].append(getNTaf(tafs[i].id))
    return liste_tafs
#OK------------------------------------------------------------------------------

# [[Taf, nombre de personnes dans la taf], ...]
# retour pour chaque eleve = [name, lastName, dateNaissance, [tafs]]

def getPersonnesTaf(id):
    taf = db.session.query(TAF).filter(TAF.id==id).first()
    gens= taf.personnes
    personnes=[]
    for personne in gens:
        tafs = getTaf(personne.id)
        tab= [personne]
        if tafs[0] == taf.name:
            tab.append(personne.annee2)
        elif tafs[1] == taf.name:
            tab.append(personne.annee3)
        personnes.append(tab)
    return [taf, personnes]
def getPromotion(annee):
    promo = db.session.query(Personne.id, Personne.name, Personne.lastName,Personne.dateNaissance).filter(Personne.promotion==annee).all()
    liste_eleves = []
    tafs = db.session.query(TAF.name)
    for eleve in promo:
        caract_eleve = []
        caract_eleve.append(eleve[1]) #prénom
        caract_eleve.append(eleve[2]) #nom
        caract_eleve.append(eleve[3]) #dateNaissance
        caract_eleve.append(getTaf(eleve[0]))

        tafs_eleve = db.session.query(TAF.name).filter(TAF.personnes.id==eleve[0]).all()


        liste_eleves.append(caract_eleve)
    return liste_eleves
#OK------------------------------------------------------------------------------
def getPromotions():
    personnes = db.session.query(Personne).all()
    liste_promos = []
    for personne in personnes:
        if [personne.promotion] not in liste_promos:
            liste_promos.append([personne.promotion])
    for i in range(len(liste_promos)):
        liste_promos[i].append([])
        for personne in personnes:
            if personne.promotion == liste_promos[i][0]:
                liste_promos[i][1].append(personne)

    for promo in liste_promos:
        promo.append(len(promo[1]))
    return liste_promos
# [[annee, [élèves], nombre eleves], ...]
# OK ----------------------------------------------------------------------------
def getNEntreprise(id,name,organisation):
    if(id):
        entreprise = db.session.query(Organisation).filter(Organisation.id==id).first()
        nombre = len(entreprise.personnes)
        return nombre
    if(organisation):
        nombre = len(organisation.personnes) #doit venir d'un .first()
        return nombre
    if(name):
        entreprise = db.session.query(Organisation).filter(Organisation.name.contains(name)).first()
        nombre = len(entreprise.personnes)
        return nombre
#OK------------------------------------------------------------------------------
def getNTaf(id):
    taf = db.session.query(TAF).filter(TAF.id==id).first()
    nombre = len(taf.personnes)
    return nombre
#OK------------------------------------------------------------------------------

def getListPosition(titre):
    personnes = Personne.query.join(Position).filter(Position.titre == titre).all()
    return personnes
#OK------------------------------------------------------------------------------
def getPersonnesPromo(annee):
    personnes = Personne.query.filter_by(promotion=annee).all()
    return personnes
#OK------------------------------------------------------------------------------
#def
#   liste entreprise, étudiants, promo, personnes position
# modifier les 4 (enlever de la promotion
def addStudent(name,lastname,genre,annee,mois,jour,promotion,annee2,annee3):
    return 0

#getPromotions #[[annee, [élèves], nombre eleves], ...] ok
#add, modify, delete
def getPostesEntreprise(id):
    entreprise = db.session.query(Organisation).filter(Organisation.id==id).first()
    list_postes = db.session.query(Position).filter(Position.organisations.contains(entreprise))
    postes=[]
    for poste in list_postes:
        personnes_poste = poste.personnes
        personnes=[]
        for personne in personnes_poste:
            print(personne)
            print(personne.id)
            print(getOrganisationById(personne.id))
            if getOrganisationById(personne.id)[0]==entreprise:
                personnes.append(personne)
        postes.append([poste,len(personnes)])
    return (entreprise,postes)

@app.route('/clean')
def routeClean():
    clean()
    return 'Database Cleaned'
@app.route('/build')
def build():
    createBase()
    return 'ok'

@app.route('/testbdd')
def testbdd2():
    clean()
    organisations, positions, pfes, tafs, personnes = createBase()
    testp = getList(None,None,None,None,None ,None,None,None,None,None)
    #testp = getList('R',None,None,'dcl','login')
    testGetTaf = getTaf(4)
    testGetSafran = getNEntreprise(None,'Safran',None)
    imt = db.session.query(Organisation).filter(Organisation.name.contains('IMT-Atlantique')).first()
    testGetNIMT = getNEntreprise(None,None,imt)
    testGetNNASA = getNEntreprise(10,None,None)
    testGetListPosition = getListPosition('etudiant')
    testGetAlumnis = getAlumnis(None,None,None)
    testPromo = getStageById(3)
    tom = getList(None,'tom',None,None,None,None,None,None,None,None)

    return(flask.render_template('testPrint.html.jinja2', organisations=organisations,
                                 positions=positions,
                                 pfes=pfes,
                                 tafs=tafs,
                                 personnes=personnes,
                                 testp=testp,
                                 testGetTaf=testGetTaf,
                                 testGetSafran=testGetSafran,
                                 testGetNIMT=testGetNIMT,
                                 testGetNNASA=testGetNNASA,
                                 testGetListPosition=testGetListPosition,
                                 testgetAlumnis=testGetAlumnis,
                                 testPromo=testPromo,
                                 tom=tom
                                ))





@app.route('/')
def main():
    clean()
    createBase()
    return flask.redirect('/login')
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
    return flask.redirect(flask.url_for('dashboard', isAdmin=False,current_id=1))

@app.route('/loginAdmin', methods=['POST'])
def loginAdminPost():
    return flask.redirect(flask.url_for('dashboard', isAdmin=True,current_id=2))

@app.route('/dashboard/<isAdmin>/<current_id>')
def dashboard(isAdmin, current_id):
    persons=getList(None,None,None,None,None,None,None,None,None,None)
    tafs = getTafs()
    entreprises = getOrganisations()
    promos=getPromotions()
    return flask.render_template('Dashboard.html.jinja2',isAdmin=isAdmin,current_id=current_id,personnes=persons,tafs=tafs,entreprises=entreprises,promos=promos)

@app.route('/dashboard/<isAdmin>/<current_id>', methods = ["POST"])
def dashboardPost(isAdmin,current_id):
    if 'filtrer' in flask.request.form:
        nom= flask.request.form['nom']
        prenom= flask.request.form['prenom']
        tafa2= flask.request.form['tafa2']
        promo= flask.request.form['promo']
        stage= flask.request.form['stage']
        tuteur= flask.request.form['tuteur']
        position= flask.request.form['position']
        entreprise= flask.request.form['entreprise']
        tafs = getTafs()
        entreprises = getOrganisations()
        promos = getPromotions()
        personnes = getList(None,prenom,nom,promo,tafa2,None,stage,tuteur,position,entreprise)
        return flask.render_template('Dashboard.html.jinja2', isAdmin=isAdmin, current_id=current_id, personnes=personnes,
                                     tafs=tafs, entreprises=entreprises, promos=promos)

@app.route('/EntrepriseModif/<id>')
def entrepriseModif(id):
    entreprise,postes = getPostesEntreprise(id)
    return flask.render_template('modifEntreprise.html.jinja2',entreprise=entreprise,postes=postes)

@app.route('/UserModif/<id>')
def userModif(id):
    personne=getList(id,None,None,None,None,None,None,None,None,None)[0]
    return flask.render_template('modifUserData.jinja2',personne=personne)

@app.route('/UserModif',methods=["POST"])
def userModifPost():
    return()

@app.route('/UserDetails/<isAdmin>/<id>/<current_id>')
def userDetails(isAdmin,id,current_id):
    personne=getList(id,None,None,None,None,None,None,None,None,None)[0]
    return flask.render_template('detailsStudent.jinja2',personne=personne,isAdmin=isAdmin,current_id=current_id)
@app.route('/EntrepriseDetails/<isAdmin>/<id>')
def entrepriseDetails(isAdmin,id):
    entreprise = getPersonnesOrganisation(id)
    return flask.render_template('detailsEntreprise.html.jinja2',entreprise=entreprise,isAdmin=isAdmin)

@app.route('/TafDetails/<isAdmin>/<id>')
def tafDetails(isAdmin,id):
    taf = getPersonnesTaf(id)
    return flask.render_template('detailsTaf.html.jinja2',isAdmin=isAdmin,taf=taf)
@app.route('/StudentAdd')
def addStudent():
    return flask.render_template('createStudent.jinja2')


if __name__ == '__main__':
    app.run()

