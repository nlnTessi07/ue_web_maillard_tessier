from database.database import db
from sqlalchemy import  Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


jun_taf_personnes = db.Table('tafs',
                             Column('taf_id', Integer, ForeignKey('taf.id')),
                             Column('personne_id',Integer, ForeignKey('personne.id'))
                             )

jun_orga_pos = db.Table('positions_orga',
                        Column('orga_id',Integer, ForeignKey('organisation.id')),
                        Column('pos_id', Integer, ForeignKey('position.id')))

class TAF(db.Model):
    id = Column(Integer, primary_key = True)
    name = Column(String)
    personnes = relationship('Personne', backref='taf',secondary=jun_taf_personnes)
    def __repr__(self):
        return self.name
    def __init__(self, name):
        self.name=name
    # Relation: jointure avec la table Personnes entre le nom de taf et l'id de l'élève
    # voir la jointure jun_taf

class Position(db.Model):
    id = Column(Integer, primary_key = True)
    id_personne = Column(Integer)
    id_Organisation = Column(Integer)
    titre = Column(String)

    ### Relation Many to One vers Personne (poste)
    personnes = relationship('Personne', backref='postes')

    ### Relation Many to Many vers Organisation
    #organisation_id = Column(Integer, ForeignKey('organisation.id'))
    organisations = relationship('Organisation', backref='orga',secondary=jun_orga_pos)

    def __init__(self,titre):
        self.titre=titre
    def __repr__(self):
        return self.titre
class Organisation(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    entreprise_stage_id = Column(Integer, ForeignKey('pfe.id'))

    personnes = relationship('Personne', backref='personnes')
    def __init__(self, name):
        self.name=name
    def __repr__(self):
        return self.name

class PFE(db.Model):
    id = Column(Integer, primary_key=True)
    titre = Column(String)
    description = Column(String)
    link_rapport = Column(String)
    eleve_id  = Column(Integer, ForeignKey("personne.id"))
    tuteur_id  = Column(Integer, ForeignKey("personne.id"))
    eleve = relationship('Personne', backref='eleve',foreign_keys=[eleve_id])
    tuteur = relationship('Personne', backref='tuteur',foreign_keys=[tuteur_id])
    entreprise_stage_id = Column(Integer,ForeignKey("organisation.id"))
    entreprise_stage = relationship('Organisation', backref ='entreprise_de_stage', foreign_keys=[entreprise_stage_id])
    def __repr__(self):
        return self.titre + ' : ' + self.description
    def __init__(self,entreprise_stage, titre, description):
        self.titre=titre
        self.description=description
        self.entreprise_stage=entreprise_stage
    ### Relation Many to Many vers PFE (tuteur peut avoir plusieurs PFE en charge)
    ### voir haut-dessus jointure jun_personnes_pfe


class Personne(db.Model):

    id = Column(Integer, primary_key=True)
    name = Column(Integer)
    lastName = Column(String)
    dateNaissance = Column(DateTime)
    genre = Column(String)
    email = Column(String)
    promotion = Column(Integer)
    annee2 = Column(Integer)
    annee3 = Column(Integer)
    annee_position = Column(Integer) # A ajouter sur la database
###  One to Many vers Position (role)
    position_id = Column(Integer, ForeignKey('position.id'))
    eleve_id = Column(Integer, ForeignKey('pfe.id'))
    tuteur_id = Column(Integer, ForeignKey('pfe.id'))
    organisation_id = Column(Integer, ForeignKey('organisation.id'))

    def __repr__(self):
        return self.name + ' ' + self.lastName

    """def __init__(self, name, lastName,dateNaissance,genre):
        self.dateNaissance=dateNaissance
        self.lastName=lastName
        self.genre=genre
        self.name = name
        """
    ### Relation Many to Many vers TAF voir la jointure jun_taf_personnes
    ### Relation One to Many vers PFE voir la jointure jun_personnes_pfe







