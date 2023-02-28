from database.database import db
from sqlalchemy import  Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func



# Classe Company
class Company(db.Model):
    __tablename__ = 'company'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    description = Column(String)

    # Relations
    interns = relationship("Alumni", backref=db.backref('company',lazy="dynamic"))
    workers = relationship("Alumni", backref=db.backref('company',lazy="dynamic"))

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
    # Relations
    current_company_id = Column(Integer, ForeignKey('company.id'))
    internship_company_id = Column(Integer, ForeignKey('company.id'))

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

