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

"""
- add : 
addPersonne : OK
addEntreprise : OK
addTaf : OK

- getters : 
filtre : getList : OK
getPersonne : OK
getAlumnis : OK
getTuteurs : OK
getTuteurByStudentId : OK
getStageById : OK
getPositionById : OK
getOrganisationById : OK
getOrganisations : OK
getPersonnesOrganisation : OK
getTafs : OK
getPersonnesTafs : OK
getTafById : OK
getPromotion : OK
getNEntreprise : OK
getNTaf : OKg
getListPosition : OK
getPersonnePromo : OK
getOrganisationByName : OK
getPostesEntreprise : OK

- modify : 
modifyPersonne : à tester
modifyTaf : à Tester
modifyPosition : à tester
modifyPositionPersonne : à tester

- delete : 
deletePersonne : à tester
deleteTaf : à tester
enleverDeLaTaf : à tester
deletePosteEntreprise : à tester

"""
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
    return None
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
def getTuteurs():
    tuteurs=[]
    pfes = db.session.query(PFE).all()
    for pfe in pfes:
        if pfe.tuteur not in tuteurs:
            tuteurs.append(pfe.tuteur)
    return tuteurs

def deleteOrganisation(id):
    db.session.query(Organisation).filter(Organisation.id==id).delete()
    db.session.commit()
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
        return pfe.tuteur.name +" "+ pfe.tuteur.lastName
    return ""
#OK----------------------------------------------------------------------------------
def getList(id,name,lastName,promotion,taf1,taf2,entreprise_stage,tuteur,position,entreprise):
    #id, name, lastName, promotion, taf1, taf2, nomPfe, EtatCivil
    personnes = db.session.query(Personne)
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
        personne.append(str(p.id))
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
        personne.append(p.annee2)
        personne.append(p.annee3)
        personne.append(p.annee_position)
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
            if p[9]!=None:
                if entreprise_stage.lower() in p[9].entreprise_stage.name.lower():
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
            if entreprise.lower() in p[7][0].name.lower():
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
#OK-------------------------------------------------------------------------
def addTaf(nom):
    new_taf = TAF(nom)
    db.session.add(new_taf)
    db.session.commit()
    return 0
#OK-------------------------------------------------------------------------
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


def getTafByTafId(id):
    return db.session.query(TAF).filter(TAF.id==id).first()
def getPromotions():
    personnes = db.session.query(Personne).all()
    liste_promos = []
    for personne in personnes:
        if [personne.promotion] not in liste_promos and personne.promotion!=None:
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
def getOrganisationByName(nom):
    return db.session.query(Organisation).filter(Organisation.name==nom).first()
def addPersonne(name,lastname,genre,dateNaissance,promotion,tafa2,tafa3,annee2,annee3, titre_pfe, entreprise_pfe,description_pfe, tuteur_pfe,position_actuelle,annee_position, entreprise_actuelle):
    if annee2 !="":
        annee2 = int(annee2)
    else : annee2 = None
    if annee3 !="":
        annee3 = int(annee3)
    else : annee3 = None
    if annee_position !="":
        annee_position = int(annee_position)
    else : annee_position = None
    if promotion !="":
        promotion = int(annee2)
    else : promotion = None
    personne = Personne(name=name,lastName=lastname,genre=genre,dateNaissance=dateNaissance,promotion=promotion,annee2=annee2,annee3=annee3,annee_position=annee_position)


    tafs = db.session.query(TAF.name).all()
    print(tafs)
    taf2dejaexiste=False
    taf3dejaexiste=False
    for taf in tafs:
        if tafa2.lower()==taf[0].lower():
            taf2 = db.session.query(TAF).filter(TAF.name == taf[0]).first()
            taf2.personnes.append(personne)
            taf2dejaexiste=True
            break
    if not taf2dejaexiste:
        addTaf(tafa2)
        taf2 = db.session.query(TAF).filter(TAF.name==tafa2).first()
        taf2.personnes.append(personne)
    for taf in tafs:
        if tafa3.lower()==taf[0].lower():
            taf3 = db.session.query(TAF).filter(TAF.name == tafa2).first()
            taf3.personnes.append(personne)
            taf3dejaexiste = True
            break
    if not taf3dejaexiste:
        addTaf(tafa3)
        taf3 = db.session.query(TAF).filter(TAF.name==tafa3).first()
        taf3.personnes.append(personne)

    organisations = db.session.query(Organisation.name).all()
    if (entreprise_actuelle,) in organisations:
        orga = db.session.query(Organisation).filter(Organisation.name==entreprise_actuelle).first()
        orga.personnes.append(personne)
    else:
        orga = Organisation(entreprise_actuelle)
        orga.personnes.append(personne)

    if (position_actuelle,) in db.session.query(Position.titre).all():
        position = db.session.query(Position).filter(Position.titre==position_actuelle).first()
        position.personnes.append(personne)
        if orga not in position.organisations:
            position.organisations.append(orga)

    else:
        position = Position(position_actuelle)
        #position = db.session.query(Position).filter(Position.titre == position_actuelle).first()
        position.personnes.append(personne)
        position.organisations.append(orga)
    if titre_pfe != "" and tuteur_pfe !="":
        pfe = PFE(getOrganisationByName(entreprise_pfe), titre_pfe, description_pfe)
        pfe.tuteur=db.session.query(Personne).filter(Personne.name == tuteur_pfe.split(" ")[0] and Personne.lastName == tuteur_pfe.split(" ")[1]).first()
        pfe.tuteur_id = pfe.tuteur.id
        pfe.eleve = personne
        pfe.eleve_id = pfe.eleve.id
        db.session.add(pfe)
    db.session.add(orga)
    db.session.add(taf2)
    db.session.add(taf3)
    db.session.add(position)

    db.session.add(personne)
    db.session.commit()
    return 0


def modifierPersonne(id, name,lastname,genre,dateNaissance,promotion,tafa2,tafa3,annee2,annee3, titre_pfe, entreprise_pfe,description_pfe, tuteur_pfe,position_actuelle,annee_position, entreprise_actuelle):
    deletePersonne(id)
    addPersonne(name,lastname,genre,
                dateNaissance,
                promotion,
                tafa2,tafa3,annee2,annee3,
                titre_pfe, entreprise_pfe,
                description_pfe, tuteur_pfe,position_actuelle,
                annee_position, entreprise_actuelle)
    db.session.commit()
def deletePersonne(id):
    db.session.query(PFE).filter_by(eleve_id=id).delete()
    db.session.query(Personne).filter_by(id=id).delete()
    db.session.commit()
def deleteTaf(tafid):
    db.session.query(TAF).filter_by(id=tafid).delete()
    db.session.commit()
def modifyTaf(old,new):
    taf = db.session.query(TAF).filter_by(name=old).first()
    taf.name=new
    db.session.add(taf)
    db.session.commit()
def enleverDeLaTaf(taf, id):
    for i in range(len(taf.personnes)):
        if(taf.personnes[i].id==int(id)):
            taf.personnes.pop(i)
            break
    db.session.commit()



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
            if getOrganisationById(personne.id)[0]==entreprise:
                personnes.append(personne)
        postes.append([poste,len(personnes)])
    return (entreprise,postes)

def deletePosteEntreprise(position,entreprise):
    for i in range(len(position.organisations)):
        if position.organisations[i].id == entreprise.id:
            position.organisations.pop(i)

    db.session.commit()
def modifyPosition(ancien, nouveau_nom, entreprise):
    positions_names = db.session.query(Position.name).all()
    if  nouveau_nom not in positions_names:# si la position n'existe pas
        nvlle = Position(nouveau_nom) # on fait une nouvelle
        nvlle.organisations.append(entreprise) #on l'ajoute

        for i in range(len(ancien.personnes)): # on prend toutes les personnes dans l'ancienne position et qui sont dans l'netreprsie
            if ancien.personnes[i] in entreprise.personnes:
                nvlle.organisations.append(ancien.personnes[i]) # on l'ajoute dans la nouvelle position
                ancien.personnes.pop(i) #On l'enlève de l'ancienne
        db.session.add(nvlle)
    else:
        nvlle = db.session.query(Position).filter_by(name=nouveau_nom)
        for i in range(len(ancien.personnes)):
            if ancien.personnes[i] in entreprise.personnes:
                nvlle.organisations.append(ancien.personnes[i])
                ancien.personnes.pop[i]

        if entreprise in ancien.organisations:
            nvlle.organisations.append(entreprise)
        db.session.add(nvlle)
    db.session.commit()

def modifyPositionPersonne(personne, old, new):
    for i in range(len(old.personnes)):
        if(old.personnes[i].id==personne.id):
            old.personnes.pop(i)
    # new = string du nom
    positions_names=  db.session.query(Position.name).all()
    if new not in positions_names:
        nvlle = Position(new)
        nvlle.personnes.append(personne)
        orga = db.session.query(Organisation).filter(Organisation.personnes.contains(personne))
        nvlle.organisations.append(orga)
        db.session.add(nvlle)
    else:
        pos = db.session.query(Position).filter(Position.titre==new)
        pos.personnes.append(personne)
    db.session.commit()

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
    nombre_gens = len(persons)
    tafs = getTafs()
    entreprises = getOrganisations()
    nombre_entreprises=len(entreprises)
    promos=getPromotions()
    tuteurs = getTuteurs()
    return flask.render_template('Dashboard.html.jinja2',nombre_gens =nombre_gens,nombre_entreprises=nombre_entreprises, isAdmin=isAdmin,current_id=current_id,personnes=persons,tafs=tafs,entreprises=entreprises,promos=promos,tuteurs=tuteurs)

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
        tuteurs = getTuteurs()
        entreprises = getOrganisations()
        promos = getPromotions()
        personnes = getList(None,prenom,nom,promo,tafa2,None,stage,tuteur,position,entreprise)
        nombre_gens = len(personnes)
        nombre_entreprises = len(entreprises)
        return flask.render_template('Dashboard.html.jinja2',nombre_gens =nombre_gens,nombre_entreprises=nombre_entreprises, isAdmin=isAdmin, current_id=current_id, personnes=personnes,
                                     tafs=tafs, entreprises=entreprises, promos=promos,tuteurs=tuteurs)

@app.route('/DeletePersonne/<id>/<current_id>')
def deletepersonne(id,current_id):
    deletePersonne(id)
    return flask.redirect(flask.url_for('dashboard', isAdmin=True, current_id=current_id))

@app.route('/DeleteTaf/<id>/<current_id>')
def deletetaf(id,current_id):
    deleteTaf(id)
    return flask.redirect(flask.url_for('dashboard', isAdmin=True, current_id=current_id))

@app.route('/DeletEntreprsie/<id>/<current_id>')
def deleteentreprise(id,current_id):
    deleteOrganisation(id)
    return flask.redirect(flask.url_for('dashboard', isAdmin=True, current_id=current_id))

@app.route('/DeletPersonneTaf/<id>/<tafid>/<current_id>')
def deletepersonnetaf(id,tafid,current_id):
    enleverDeLaTaf(getTafByTafId(tafid),id)
    return flask.redirect(flask.url_for('tafModif',id=tafid,current_id=current_id))

@app.route('/EntrepriseModif/<id>/<current_id>')
def entrepriseModif(id,current_id):
    entreprise,postes = getPostesEntreprise(id)
    return flask.render_template('modifEntreprise.html.jinja2',entreprise=entreprise,postes=postes,current_id=current_id)

@app.route('/EntrepriseModif/<id>/<current_id>',methods=["Post"])
def entrepriseModifPost(id,current_id):
    entreprise,postes = getPostesEntreprise(id)
    entreprise.name = flask.request.form['nom']
    db.session.commit()
    return flask.render_template('modifEntreprise.html.jinja2',entreprise=entreprise,postes=postes,current_id=current_id)

@app.route('/UserModif/<id>/<isAdmin>/<current_id>')
def userModif(id,isAdmin,current_id):
    tafs = getTafs()
    entreprises = getOrganisations()
    promos = getPromotions()
    tuteurs = getTuteurs()
    personne=getList(id,None,None,None,None,None,None,None,None,None)[0]
    return flask.render_template('modifUserData.jinja2',isAdmin=isAdmin,personne=personne,tafs=tafs,entreprises=entreprises,promos=promos,tuteurs=tuteurs,current_id=current_id)

@app.route('/UserModif/<id>/<isAdmin>/<current_id>',methods=["POST"])
def userModifPost(id,isAdmin,current_id):
    genre = flask.request.form['Genre']
    nom = flask.request.form['nom']
    prenom = flask.request.form['prenom']
    naissance = flask.request.form['date']
    tafa2 = flask.request.form['tafa2']
    annee2 = flask.request.form['annee2']
    tafa3 = flask.request.form['tafa3']
    annee3 = flask.request.form['annee3']
    promo = flask.request.form['promo']
    titre_stage = flask.request.form['stage']
    description = flask.request.form['description']
    tuteur = flask.request.form['tuteur']
    entreprise_stage = flask.request.form['entreprise_stage']
    position = flask.request.form['position']
    annee_position = flask.request.form['anneePosition']
    entreprise = flask.request.form['entreprise']
    date = datetime(year=int(naissance[0:4]), month=int(naissance[5:7]), day=int(naissance[8:]))
    modifierPersonne(id,prenom, nom, genre, date, promo, tafa2, tafa3, annee2, annee3, titre_stage, entreprise_stage,
                description, tuteur, position, annee_position, entreprise)
    return flask.redirect(flask.url_for('dashboard', isAdmin=isAdmin, current_id=db.session.query(Personne.id).all()[-1][0]))

@app.route('/UserDetails/<isAdmin>/<id>/<current_id>')
def userDetails(isAdmin,id,current_id):
    personne=getList(id,None,None,None,None,None,None,None,None,None)[0]
    return flask.render_template('detailsStudent.jinja2',personne=personne,isAdmin=isAdmin,current_id=current_id)
@app.route('/EntrepriseDetails/<isAdmin>/<id>/<current_id>')
def entrepriseDetails(isAdmin,id,current_id):
    entreprise = getPersonnesOrganisation(id)
    return flask.render_template('detailsEntreprise.html.jinja2',entreprise=entreprise,isAdmin=isAdmin,current_id= current_id)

@app.route('/TafDetails/<isAdmin>/<id>/<current_id>')
def tafDetails(isAdmin,id,current_id):
    taf = getTafByTafId(id)
    gens = []
    for personne in taf.personnes:
        tafs = getTaf(personne.id)
        if taf == tafs[0]:
            gens.append([personne, personne.annee2])
        else:
            gens.append([personne, personne.annee3])
    return flask.render_template('detailsTaf.html.jinja2',isAdmin=isAdmin,taf=taf,gens=gens,current_id=current_id)

@app.route('/PromoDetails/<promotion>/<isAdmin>/<current_id>')
def promoDetails(promotion,isAdmin,current_id):
    promo=[promotion]
    promo.append(getPersonnesPromo(promotion))
    return flask.render_template('detailsPromo.html.jinja2',isAdmin=isAdmin,promo=promo,current_id=current_id)

@app.route('/TafModif/<id>/<current_id>')
def tafModif(id,current_id):
    taf = getTafByTafId(id)
    gens=[]
    for personne in taf.personnes:
        tafs = getTaf(personne.id)
        if taf == tafs[0]:
            gens.append([personne,personne.annee2])
        else : gens.append([personne,personne.annee3])

    return flask.render_template('modifTaf.html.jinja2',taf=taf,gens=gens,current_id=current_id)

@app.route('/TafModif/<id>/<current_id>', methods=["POST"])
def tafModifPost(id,current_id):
    taf = getTafByTafId(id)
    gens=[]
    for personne in taf.personnes:
        tafs = getTaf(personne.id)
        if taf == tafs[0]:
            gens.append([personne,personne.annee2])
        else : gens.append([personne,personne.annee3])
    new = flask.request.form['nom']
    modifyTaf(taf.name,new)
    return flask.render_template('modifTaf.html.jinja2',taf=taf,gens=gens,current_id=current_id)

@app.route('/PromoModif/<promotion>/<current_id>', methods=["POST"])
def promoModifPost(promotion,current_id):
    personnes = getPersonnesPromo(int(promotion))
    nom = flask.request.form['nom']
    for personne in personnes:
        personne.promotion = int(nom)
    db.session.commit()
    return flask.redirect(flask.url_for('promoModif',promotion=int(nom),current_id=current_id))
@app.route('/PromoModif/<promotion>/<current_id>')
def promoModif(promotion, current_id):
    return flask.render_template('modifPromo.html.jinja2',promo=promotion,current_id=current_id)
@app.route('/StudentAdd/<current_id>')
def addStudent(current_id):
    tafs = getTafs()
    entreprises = getOrganisations()
    promos = getPromotions()
    tuteurs = getTuteurs()
    return flask.render_template('createStudent.jinja2',current_id=current_id,tafs=tafs,entreprises=entreprises,promos=promos,tuteurs=tuteurs)


@app.route('/StudentAdd/<current_id>',methods=["POST"])
def addStudentPost(current_id):
    genre=flask.request.form['Genre']
    nom = flask.request.form['nom']
    prenom = flask.request.form['prenom']
    naissance=flask.request.form['date']
    tafa2 = flask.request.form['tafa2']
    annee2=flask.request.form['annee2']
    tafa3 = flask.request.form['tafa3']
    annee3=flask.request.form['annee3']
    promo = flask.request.form['promo']
    titre_stage = flask.request.form['stage']
    description = flask.request.form['description']
    tuteur = flask.request.form['tuteur']
    entreprise_stage=flask.request.form['entreprise_stage']
    position = flask.request.form['position']
    annee_position=flask.request.form['anneePosition']
    entreprise = flask.request.form['entreprise']
    date= datetime(year=int(naissance[0:4]),month=int(naissance[5:7]),day=int(naissance[8:]))
    addPersonne(prenom,nom,genre,date,promo,tafa2,tafa3,annee2,annee3,titre_stage,entreprise_stage,description,tuteur,position,annee_position,entreprise)
    return flask.redirect(flask.url_for('dashboard', isAdmin=True, current_id=current_id))


if __name__ == '__main__':
    app.run()

