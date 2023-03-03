from database.database import db
from sqlalchemy import  Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


jun_taf_personnes = db.Table('tafs',
                             Column('taf_id', Integer, ForeignKey('taf.id')),
                             Column('personne_id',Integer, ForeignKey('personne.id'))
                             )
jun_personnes_pfe = db.Table('pfe_personnes',
                             Column('pfe_id',Integer, ForeignKey('pfe.id')),
                             Column('personne_id', Integer, ForeignKey('personne.id'))
                             )

class TAF(db.Model):
    id = Column(Integer, primary_key = True)
    name = Column(String)
    annee = Column(String)
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
    date_entree = Column(Integer)
    ### Relation Many to One vers Organisation
    organisation_id = Column(Integer, ForeignKey('organisation.id'))
    ### Relation Many to One vers Personne (poste)
    personnes = relationship('Personne',backref='postes')
    def __init__(self,titre):
        self.titre=titre


class Organisation(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    ### Relation One to Many vers Position
    postes = relationship('Position', backref='postes')
    def __init__(self, name):
        self.name=name

class PFE(db.Model):
    id = Column(Integer, primary_key=True)
    titre = Column(String)
    description = Column(String)
    def __repr__(self):
        return self.titre + ' : ' + self.description
    def __init__(self, titre, description):
        self.titre=titre
        self.description=description
    ### Relation Many to Many vers PFE (tuteur peut avoir plusieurs PFE en charge)
    ### voir haut-dessus jointure jun_personnes_pfe


class Personne(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(Integer)
###  One to Many vers Position (role)
    position_id = Column(Integer, ForeignKey('position.id'))
    def __repr__(self):
        return self.name
    def __init__(self, name):
        self.name = name
    ### Relation Many to Many vers TAF voir la jointure jun_taf_personnes
    ### Relation One to Many vers PFE voir la jointure jun_personnes_pfe
















#------------------------- ANCIEN ------------------------------------------------#
"""

class Company(db.Model):
    __tablename__ = 'company'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    description = Column(String)

    # Relations
    interns = relationship("Alumni", foreign_keys="[Alumni.current_company_id]")
    workers = relationship("Alumni", foreign_keys="[Alumni.internship_company_id]")

    def __repr__(self):
        return self.name
    def __init__(self, name):
        self.name=name
# Classe Alumni
class Alumni(db.Model):
    __tablename__ = 'alumni'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    tafa2= Column(String)
    tafa3 = Column(String)
    project_name = Column(String)
    project_summary = Column(String)
    tutor = db.Column(String)
    promo = Column(String)
    current_company_id = Column(Integer, ForeignKey('company.id'))
    internship_company_id = Column(Integer, ForeignKey('company.id'))

    # Relations
    current_company = relationship("Company", foreign_keys=[current_company_id])
    internship_company = relationship("Company", foreign_keys=[internship_company_id])

    def __repr__(self):
        return self.name + ' was in ' + self.tafa2
    def __init__(self, name,tafa2,tafa3,promo,project_name,project_summary,project_company,tutor,current_position,current_company):
        self.name=name
        self.tafa2=tafa2
        self.tafa3=tafa3
        self.promo=promo
        self.project_name=project_name
        self.project_summary=project_summary
        self.project_company=project_company
        self.tutor=tutor
        self.current_position=current_position
        self.current_company=current_company
"""
