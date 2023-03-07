import flask
from flask import Flask
from database.database import db, init_database
from database.models import *
from datetime import datetime

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////home/nolann/PycharmProjects/ue_web_maillard_tessier/database/database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "secret_key1234"


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
    positions = Position.query.all()

    # Attribution entrerpise :
    imt.postes.append(enseignant)
    imt.postes.append(chercheur)
    imt.postes.append(etudiant)
    imt.postes.append(tuteur)

    edf.postes.append(inge_bat)
    edf.postes.append(inge_nuc)
    edf.postes.append(inge_info)
    edf.postes.append(chercheur)
    edf.postes.append(tuteur)
    edf.postes.append(RH)
    edf.postes.append(stagiaire_pfe)
    edf.postes.append(patron)

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

    # CREATION TAFs
    dcl = TAF('DCL')
    login = TAF('Login')
    ascii = TAF('ascii')
    demain = TAF('demain')
    nemo = TAF('nemo')
    TEE = TAF('TEE')
    cyber = TAF('cyber')

    db.session.add(dcl)
    db.session.add(login)
    db.session.add(ascii)
    db.session.add(demain)
    db.session.add(nemo)
    db.session.add(TEE)
    db.session.add(cyber)

    db.session.commit()
    tafs = TAF.query.all()

    # CREATION PERSONNES
    #élèves actuels
    tom= Personne('Tom','Dupont','Mr',datetime(year=2002,month=12,day=11),promotion=2024,annee2=2023,annee3=2024)
    rory = Personne('Rory','Martin','Mr',datetime(year=2002,month=12,day=11),promotion=2024,annee2=2023,annee3=2024)
    marty= Personne('Marty''Dubois','Mr',datetime(year=2000,month=11,day=11),promotion=2024,annee2=2023,annee3=2024)
    alexis= Personne('Alexis','Bernard','Mr',datetime(year=1999,month=11,day=11),promotion=2024,annee2=2022,annee3=2024) # Césure
    julien= Personne('Julien','Rousseau','Mr',datetime(year=2000,month=4,day=11),promotion=2024,annee2=2022,annee3=2024) # Césure
    eugenie= Personne('Eugenie','Petit','Mme',datetime(year=2001,month=5,day=11),promotion=2024,annee2=2023,annee3=2024)
    Mael = Personne('Mael','Lefebvre','Mr',datetime(year=2001,month=7,day=11),promotion=2024,annee2=2023,annee3=2024)

    #profs :
    Theo = Personne('Theo','Moreau','Mr',datetime(year=1970,month=1,day=24))
    Mario = Personne('Mario','Fournier','Mr',datetime(year=1972,month=2,day=27))
    Safou = Personne('Safouana','Girard','Mr',datetime(year=1570,month=3,day=7))


    #alumnis
    Lilian = Personne('Lilian','Laurent','Mr',datetime(year=1998,month=12,day=21),promotion=2020,annee2=2018,annee3=2020) #Cesure
    Nino = Personne('Nino','Simon','Mr',datetime(year=1999,month=1,day=23),promotion=2020,annee2=2018,annee3=2020) #Cesure
    Pablo = Personne('Pablo','Durand','Mr',datetime(year=2000,month=4,day=14),promotion=2020,annee2=2018,annee3=2019)
    Emma = Personne('Emma','Roux','Mme',datetime(year=1999,month=6,day=15),promotion=2019,annee2=2017,annee3=2018)
    Gregoire = Personne('Gregoire','Leclerc','Mr',datetime(year=1999,month=9,day=16),promotion=2020,annee2=2018,annee3=2020)
    Lea = Personne('Lea','Lambert','Mme',datetime(year=1998,month=10,day=21),promotion=2019,annee2=2018,annee3=2019)
    Nathan = Personne('Nathan','Mercier','Mr',datetime(year=1997,month=10,day=22),promotion=2018,annee2=2016,annee3=2018)
    Octave = Personne('Octave','Vidal','Mr',datetime(year=1998,month=6,day=28),promotion=2022,annee2=2021,annee3=2022)
    Thibault = Personne('Thibault','Caron','Mr',datetime(year=1999,month=1,day=3),promotion=2020,annee2=2019,annee3=2020)


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

    db.session.commit()
    personnes = Personne.query.all()

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
    reco = PFE('Développement dun système de reconnaissance de la parole pour les personnes atteintes de troubles de la communication','Je veux manger des baleresques toute l annee voila le projet.',
                 ' Ce projet consiste en la création dun logiciel qui peut aider les personnes atteintes de troubles de la communication à communiquer plus facilement en utilisant leur voix.')
    sysSurv = PFE('Conception dun système de surveillance et de contrôle pour les cultures maraîchères ',
                   'Ce projet implique la mise en place dun système de surveillance et de contrôle pour les cultures maraîchères qui permettra de surveiller lhumidité, la température, et la qualité du sol pour maximiser les récoltes.')
    secu = PFE('Évaluation de la sécurité des systèmes de contrôle industriel', 'Ce projet porte sur lévaluation de la sécurité des systèmes de contrôle industriel pour assurer la sécurité des travailleurs et des installations industrielles.')
    ia = PFE('Étude de la performance de lintelligence artificielle pour la classification des maladies cardiaques ',
                      'Ce projet vise à évaluer la performance de lintelligence artificielle dans la classification des maladies cardiaques à partir de données de santé.')
    jeuSimu = PFE('Conception dun jeu de simulation pour lapprentissage des langues étrangères'
                 ,'Ce projet implique la création dun jeu de simulation pour aider les étudiants à apprendre une langue étrangère de manière plus interactive et amusante.')
    etudeDistance = PFE('Évaluation de lefficacité de lenseignement à distance pour les étudiants en ligne',
                   'Ce projet vise à évaluer lefficacité de lenseignement à distance pour les étudiants en ligne en comparaison à lenseignement traditionnel en classe.')
    appli = PFE('Développement dune application de gestion des tâches pour les travailleurs indépendants ',
                      'Ce projet consiste en la création dune application de gestion des tâches pour aider les travailleurs indépendants à organiser leur travail et à suivre leur temps.')

    reaVirt = PFE('Étude de limpact de lutilisation de la réalité virtuelle dans la formation des soins infirmiers', 'Ce projet vise à étudier limpact de lutilisation de la réalité virtuelle dans la formation des soins infirmiers sur la qualité des soins et lefficacité de la formation.')

    mouvement = PFE('Conception dun dispositif de détection des objets en mouvement pour la sécurité routière','Ce projet implique la création dun dispositif de détection des objets en mouvement pour améliorer la sécurité routière en détectant les véhicules et les piétons.')

    depression = PFE('Étude de lefficacité de la thérapie par lart pour le traitement de la dépression', 'Ce projet vise à étudier lefficacité de la thérapie par lart pour le traitement de la dépression en comparaison aux traitements traditionnels.')
    anim = PFE('Développement dun système de suivi des animaux de compagnie ', 'Ce projet consiste en la création dun système de suivi des animaux de compagnie qui permettra aux propriétaires de suivre la localisation et lactivité de leur animal en temps réel.')

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

    db.session.commit()
    pfes = PFE.query.all()

    # Attribution PFE tuteur/eleve
    reco.tuteur.append(Theo)
    sysSurv.tuteur.append(Theo)
    secu.tuteur.append(Theo)
    ia.tuteur.append(Theo)
    jeuSimu.tuteur.append(Theo)
    etudeDistance.tuteur.append(Theo)
    appli.tuteur.append(Mario)
    reaVirt.tuteur.append(Mario)
    mouvement.tuteur.append(Mario)
    depression.tuteur.append(Mario)
    anim.tuteur.append(Mario)

    reco.eleve.append(alexis)
    sysSurv.eleve.append(julien)
    secu.eleve.append(Nino)
    ia.eleve.append(Pablo)
    jeuSimu.eleve.append(Emma)
    etudeDistance.eleve.append(Lilian)
    appli.eleve.append(Gregoire)
    reaVirt.eleve.append(Nathan)
    mouvement.eleve.append(Thibault)
    depression.eleve.append(Lea)
    anim.eleve.append(Octave)

    db.session.commit()

    # Attributions organisation
    imt.postes.append(Theo)
    imt.postes.append(Mario)
    imt.postes.append(Safou)
    imt.postes.append(tom)
    imt.postes.append(rory)
    imt.postes.append(alexis)
    imt.postes.append(julien)
    imt.postes.append(eugenie)
    imt.postes.append(Mael)
    imt.postes.append(marty)

    Dassault.postes.append(alexis)
    Safran.postes.append(julien)
    NASA.postes.append(Pablo)
    NASA.postes.append(Emma)
    Carouf.postes.append(Gregoire)
    FTX.postes.append(Lea)
    CreditSuisse.postes.append(Nathan)
    ESA.postes.append(Octave)
    edf.postes.append(Thibault)

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


    return(organisations,positions,pfes,tafs,personnes)