import flask
from flask import Flask
from database.database import db, init_database
from database.models import *
from datetime import datetime

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////home/nolann/PycharmProjects/ue_web_maillard_tessier/database/database.db"
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///E:\\Documents\\Programming\\Python\\ue_web_maillard_tessier\\database\\database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "secret_key1234"
db.init_app(app)


with app.test_request_context():
    init_database()

def clean():
    db.drop_all()
    db.create_all()
    return "Cleaned!"

# CREATION DE LA BASE DE DONNÉES :

def createBase():

    ## CREATION ORGANISATIONS
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

       ### AFFICHAGE OK

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



    # Attribution entrerpise :

    enseignant.organisations.append(imt)
    tuteur.organisations.append(imt)
    chercheur.organisations.append(imt)
    etudiant.organisations.append(imt)

    inge_bat.organisations.append(edf)
    inge_bat.organisations.append(poliakov)
    inge_bat.organisations.append(Dassault)
    inge_bat.organisations.append(Safran)

    inge_nuc.organisations.append(edf)
    inge_nuc.organisations.append(imt)


    inge_info.organisations.append(Dassault)
    inge_info.organisations.append(Safran)
    inge_info.organisations.append(Labo)
    inge_info.organisations.append(Carouf)
    inge_info.organisations.append(CDiscount)
    inge_info.organisations.append(NASA)
    inge_info.organisations.append(ESA)
    inge_info.organisations.append(FTX)
    inge_info.organisations.append(CreditSuisse)
    inge_info.organisations.append(poliakov)
    inge_info.organisations.append(edf)
    inge_info.organisations.append(engie)
    inge_info.organisations.append(total)
    inge_info.organisations.append(imt)

    RH.organisations.append(Dassault)
    RH.organisations.append(Safran)
    RH.organisations.append(Labo)
    RH.organisations.append(Carouf)
    RH.organisations.append(CDiscount)
    RH.organisations.append(NASA)
    RH.organisations.append(ESA)
    RH.organisations.append(CreditSuisse)
    RH.organisations.append(FTX)
    RH.organisations.append(poliakov)
    RH.organisations.append(edf)
    RH.organisations.append(engie)
    RH.organisations.append(total)

    stagiaire_pfe.organisations.append(Dassault)
    stagiaire_pfe.organisations.append(Safran)
    stagiaire_pfe.organisations.append(Labo)
    stagiaire_pfe.organisations.append(Carouf)
    stagiaire_pfe.organisations.append(CDiscount)
    stagiaire_pfe.organisations.append(NASA)
    stagiaire_pfe.organisations.append(ESA)
    stagiaire_pfe.organisations.append(CreditSuisse)
    stagiaire_pfe.organisations.append(FTX)
    stagiaire_pfe.organisations.append(poliakov)
    stagiaire_pfe.organisations.append(edf)
    stagiaire_pfe.organisations.append(engie)
    stagiaire_pfe.organisations.append(total)

    patron.organisations.append(Dassault)
    patron.organisations.append(Safran)
    patron.organisations.append(Labo)
    patron.organisations.append(Carouf)
    patron.organisations.append(CDiscount)
    patron.organisations.append(NASA)
    patron.organisations.append(ESA)
    patron.organisations.append(CreditSuisse)
    patron.organisations.append(FTX)
    patron.organisations.append(poliakov)
    patron.organisations.append(edf)
    patron.organisations.append(engie)
    patron.organisations.append(total)

    """
    poliakov.postes.append(inge_bat)
    poliakov.postes.append(inge_nuc)
    poliakov.postes.append(inge_info)
    poliakov.postes.append(chercheur)
    poliakov.postes.append(tuteur)
    poliakov.postes.append(RH)
    poliakov.postes.append(stagiaire_pfe)
    poliakov.postes.append(patron)

    Dassault.postes.append(inge_bat)
    Dassault.postes.append(inge_nuc)
    Dassault.postes.append(inge_info)
    Dassault.postes.append(chercheur)
    Dassault.postes.append(tuteur)
    Dassault.postes.append(RH)
    Dassault.postes.append(stagiaire_pfe)
    Dassault.postes.append(patron)

    Safran.postes.append(inge_bat)
    Safran.postes.append(inge_nuc)
    Safran.postes.append(inge_info)
    Safran.postes.append(chercheur)
    Safran.postes.append(tuteur)
    Safran.postes.append(RH)
    Safran.postes.append(stagiaire_pfe)
    Safran.postes.append(patron)
    """


    # CREATION TAFs
    dcl = TAF('DCL')
    login = TAF('Login')
    ascii = TAF('ascii')
    demain = TAF('demain')
    nemo = TAF('nemo')
    TEE = TAF('TEE')
    cyber = TAF('cyber')




    # CREATION PERSONNES
    #élèves actuels
    tom= Personne(name='Tom',lastName='Dupont',genre='Mr',dateNaissance=datetime(year=2002,month=12,day=11),promotion=2024,annee2=2023,annee3=2024,annee_position=2015)
    rory = Personne(name='Rory',lastName='Maillard',genre='Mr',dateNaissance=datetime(year=2002,month=12,day=11),promotion=2024,annee2=2023,annee3=2024,annee_position=2015)
    marty= Personne(name='Marty',lastName='Dubois',genre='Mr',dateNaissance=datetime(year=2000,month=11,day=11),promotion=2024,annee2=2023,annee3=2024,annee_position=2015)
    alexis= Personne(name='Alexis',lastName='Bernard',genre='Mr',dateNaissance=datetime(year=1999,month=11,day=11),promotion=2024,annee2=2022,annee3=2024,annee_position=2015) # Césure
    julien= Personne(name='Julien',lastName='Rousseau',genre='Mr',dateNaissance=datetime(year=2000,month=4,day=11),promotion=2024,annee2=2022,annee3=2024,annee_position=2015) # Césure
    eugenie= Personne(name='Eugenie',lastName='Petit',genre='Mme',dateNaissance=datetime(year=2001,month=5,day=11),promotion=2024,annee2=2023,annee3=2024,annee_position=2015)
    Mael = Personne(name='Mael',lastName='Lefebvre',genre='Mr',dateNaissance=datetime(year=2001,month=7,day=11),promotion=2024,annee2=2023,annee3=2024,annee_position=2015)
    #profs :
    Theo = Personne(name='Theo',lastName='Moreau',genre='Mr',dateNaissance=datetime(year=1970,month=1,day=24),annee_position=2015)
    Mario = Personne(name='Mario',lastName='Fournier',genre='Mr',dateNaissance=datetime(year=1972,month=2,day=27),annee_position=2015)
    Safou = Personne(name='Safouana',lastName='Girard',genre='Mr',dateNaissance=datetime(year=1570,month=3,day=7),annee_position=2015)


    #alumnis
    Lilian = Personne(name='Lilian',lastName='Laurent',genre='Mr',dateNaissance=datetime(year=1998,month=12,day=21),promotion=2020,annee2=2018,annee3=2020,annee_position=2015) #Cesure
    Nino = Personne(name='Nino',lastName='Simon',genre='Mr',dateNaissance=datetime(year=1999,month=1,day=23),promotion=2020,annee2=2018,annee3=2020,annee_position=2015) #Cesure
    Pablo = Personne(name='Pablo',lastName='Durand',genre='Mr',dateNaissance=datetime(year=2000,month=4,day=14),promotion=2020,annee2=2018,annee3=2019,annee_position=2015)
    Emma = Personne(name='Emma',lastName='Roux',genre='Mme',dateNaissance=datetime(year=1999,month=6,day=15),promotion=2019,annee2=2017,annee3=2018,annee_position=2015)
    Gregoire = Personne(name='Gregoire',lastName='Leclerc',genre='Mr',dateNaissance=datetime(year=1999,month=9,day=16),promotion=2020,annee2=2018,annee3=2020,annee_position=2015)
    Lea = Personne(name='Lea',lastName='Lambert',genre='Mme',dateNaissance=datetime(year=1998,month=10,day=21),promotion=2019,annee2=2018,annee3=2019,annee_position=2015)
    Nathan = Personne(name='Nathan',lastName='Mercier',genre='Mr',dateNaissance=datetime(year=1997,month=10,day=22),promotion=2018,annee2=2016,annee3=2018,annee_position=2015)
    Octave = Personne(name='Octave',lastName='Vidal',genre='Mr',dateNaissance=datetime(year=1998,month=6,day=28),promotion=2022,annee2=2021,annee3=2022,annee_position=2015)
    Thibault = Personne(name='Thibault',lastName='Caron',genre='Mr',dateNaissance=datetime(year=1999,month=1,day=3),promotion=2020,annee2=2019,annee3=2020,annee_position=2015)


    # Attribution des positions :
    etudiant.personnes.append(tom)
    etudiant.personnes.append(rory)
    etudiant.personnes.append(marty)
    etudiant.personnes.append(alexis)
    etudiant.personnes.append(julien)
    etudiant.personnes.append(eugenie)
    etudiant.personnes.append(Mael)

    stagiaire_pfe.personnes.append(alexis)
    stagiaire_pfe.personnes.append(julien)

    enseignant.personnes.append(Theo)
    enseignant.personnes.append(Mario)
    enseignant.personnes.append(Safou)

    tuteur.personnes.append(Theo)
    tuteur.personnes.append(Mario)

    inge_info.personnes.append(Nino)
    inge_info.personnes.append(Pablo)
    inge_info.personnes.append(Emma)
    inge_bat.personnes.append(Lilian)
    inge_nuc.personnes.append(Gregoire)
    patron.personnes.append(Nathan)
    RH.personnes.append(Thibault)
    inge_bat.personnes.append(Lea)
    patron.personnes.append(Octave)



    #Creation PFE
    reco = PFE(Dassault,'Développement dun système de reconnaissance de la parole pour les personnes atteintes de troubles de la communication',
                 ' Ce projet consiste en la création dun logiciel qui peut aider les personnes atteintes de troubles de la communication à communiquer plus facilement en utilisant leur voix.')
    sysSurv = PFE(Safran,'Conception dun système de surveillance et de contrôle pour les cultures maraîchères ',
                   'Ce projet implique la mise en place dun système de surveillance et de contrôle pour les cultures maraîchères qui permettra de surveiller lhumidité, la température, et la qualité du sol pour maximiser les récoltes.')
    secu = PFE(imt,'Évaluation de la sécurité des systèmes de contrôle industriel', 'Ce projet porte sur lévaluation de la sécurité des systèmes de contrôle industriel pour assurer la sécurité des travailleurs et des installations industrielles.')
    ia = PFE(Dassault,'Étude de la performance de lintelligence artificielle pour la classification des maladies cardiaques ',
                      'Ce projet vise à évaluer la performance de lintelligence artificielle dans la classification des maladies cardiaques à partir de données de santé.')
    jeuSimu = PFE(Dassault,'Conception dun jeu de simulation pour lapprentissage des langues étrangères'
                 ,'Ce projet implique la création dun jeu de simulation pour aider les étudiants à apprendre une langue étrangère de manière plus interactive et amusante.')
    etudeDistance = PFE(edf,'Évaluation de lefficacité de lenseignement à distance pour les étudiants en ligne',
                   'Ce projet vise à évaluer lefficacité de lenseignement à distance pour les étudiants en ligne en comparaison à lenseignement traditionnel en classe.')
    appli = PFE(edf,'Développement dune application de gestion des tâches pour les travailleurs indépendants ',
                      'Ce projet consiste en la création dune application de gestion des tâches pour aider les travailleurs indépendants à organiser leur travail et à suivre leur temps.')

    reaVirt = PFE(NASA,'Étude de limpact de lutilisation de la réalité virtuelle dans la formation des soins infirmiers', 'Ce projet vise à étudier limpact de lutilisation de la réalité virtuelle dans la formation des soins infirmiers sur la qualité des soins et lefficacité de la formation.')

    mouvement = PFE(ESA,'Conception dun dispositif de détection des objets en mouvement pour la sécurité routière','Ce projet implique la création dun dispositif de détection des objets en mouvement pour améliorer la sécurité routière en détectant les véhicules et les piétons.')

    depression = PFE(NASA,'Étude de lefficacité de la thérapie par lart pour le traitement de la dépression', 'Ce projet vise à étudier lefficacité de la thérapie par lart pour le traitement de la dépression en comparaison aux traitements traditionnels.')
    anim = PFE(NASA,'Développement dun système de suivi des animaux de compagnie ', 'Ce projet consiste en la création dun système de suivi des animaux de compagnie qui permettra aux propriétaires de suivre la localisation et lactivité de leur animal en temps réel.')





    # Attribution PFE tuteur/eleve
    #reco.tuteur_id= db.session.query(Personne).filter(Personne.name=='Theo')

    reco.tuteur = Theo
    sysSurv.tuteur = Theo
    secu.tuteur = Theo
    ia.tuteur = Theo
    jeuSimu.tuteur = Theo
    etudeDistance.tuteur = Mario
    appli.tuteur = Theo
    reaVirt.tuteur = Theo
    mouvement.tuteur = Mario
    depression.tuteur = Mario
    anim.tuteur = Mario

    reco.eleve = alexis
    sysSurv.eleve = julien
    secu.eleve = Nino
    ia.eleve = Pablo
    jeuSimu.eleve = Emma
    etudeDistance.eleve = Lilian
    appli.eleve=Gregoire
    reaVirt.eleve=Nathan
    mouvement.eleve=Thibault
    depression.eleve=Lea
    anim.eleve=Octave

    # Attributions organisation
    imt.personnes.append(Theo)
    imt.personnes.append(Theo)
    imt.personnes.append(Mario)
    imt.personnes.append(Safou)
    imt.personnes.append(tom)
    imt.personnes.append(rory)
    imt.personnes.append(alexis)
    imt.personnes.append(julien)
    imt.personnes.append(eugenie)
    imt.personnes.append(Mael)
    imt.personnes.append(marty)

    Dassault.personnes.append(alexis)
    Safran.personnes.append(julien)
    NASA.personnes.append(Pablo)
    NASA.personnes.append(Emma)
    Carouf.personnes.append(Gregoire)
    FTX.personnes.append(Lea)
    CreditSuisse.personnes.append(Nathan)
    ESA.personnes.append(Octave)
    edf.personnes.append(Thibault)

    # Attribution des tafs : (deux tafs pour les alumnis, une pour les élèves).
    for ele in [alexis,julien,eugenie,rory]:
        dcl.personnes.append(ele)
    ascii.personnes.append(tom)
    ascii.personnes.append(marty)
    demain.personnes.append(Mael)

    demain.personnes.append(Lilian)
    cyber.personnes.append(Lilian)
    nemo.personnes.append(Nino)
    ascii.personnes.append(Nino)
    nemo.personnes.append(Pablo)
    cyber.personnes.append(Pablo)
    dcl.personnes.append(Emma)
    login.personnes.append(Emma)
    dcl.personnes.append(Gregoire)
    login.personnes.append(Gregoire)
    dcl.personnes.append(Lea)
    login.personnes.append(Lea)
    login.personnes.append(Nathan)
    ascii.personnes.append(Nathan)
    demain.personnes.append(Octave)
    TEE.personnes.append(Octave)
    demain.personnes.append(Thibault)
    cyber.personnes.append(Thibault)



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

    db.session.add(reco)
    db.session.add(sysSurv)
    db.session.add(secu)
    db.session.add(ia)
    db.session.add(jeuSimu)
    db.session.add(etudeDistance)
    db.session.add(mouvement)
    db.session.add(appli)
    db.session.add(reaVirt)
    db.session.add(depression)
    db.session.add(anim)
    db.session.add(tom)
    db.session.add(rory)
    db.session.add(marty)
    db.session.add(alexis)
    db.session.add(julien)
    db.session.add(eugenie)
    db.session.add(Mael)
    db.session.add(Theo)
    db.session.add(Lilian)
    db.session.add(Nino)
    db.session.add(Pablo)
    db.session.add(Emma)
    db.session.add(Gregoire)
    db.session.add(Lea)
    db.session.add(Nathan)
    db.session.add(Octave)
    db.session.add(Thibault)
    db.session.add(Mario)
    db.session.add(Safou)
    db.session.add(dcl)
    db.session.add(login)
    db.session.add(ascii)
    db.session.add(demain)
    db.session.add(nemo)
    db.session.add(TEE)
    db.session.add(cyber)
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

    organisations = db.session.query(Organisation).all()
    positions = db.session.query(Position).all()
    pfes = db.session.query(PFE).all()
    tafs = db.session.query(TAF).all()
    personnes = db.session.query(Personne).all()

    return(organisations,positions,pfes,tafs,personnes)



 # liste des étudiants avec toutes les infos (sous forme de personne) = tout le monde sauf le personnel
 # que les étudiants [personnes]
 # que les alumnis [personnes]
 # Toutes les entreprises

