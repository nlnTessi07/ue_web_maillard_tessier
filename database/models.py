from database.database import db
from sqlalchemy import  Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func




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
    current_company_id = Column(Integer, ForeignKey('company.id'))
    internship_company_id = Column(Integer, ForeignKey('company.id'))
    promo_id = Column(Integer, ForeignKey('promo.id'))

    # Relations
    current_company = relationship("Company", foreign_keys=[current_company_id])
    internship_company = relationship("Company", foreign_keys=[internship_company_id])
    promo = relationship("Promo", back_populates="alumnis", foreign_keys=[promo_id])

    def __repr__(self):
        return self.name + ' was in ' + self.tafa2
    def __init__(self, name,tafa2,tafa3,end_year,project_name,project_summary,project_company,tutor,current_position,current_company):
        self.name=name
        self.tafa2=tafa2
        self.tafa3=tafa3
        self.end_year=end_year
        self.project_name=project_name
        self.project_summary=project_summary
        self.project_company=project_company
        self.tutor=tutor
        self.current_position=current_position
        self.current_company=current_company

# Classe Promotion
class Promo(db.Model):
    __tablename__ = 'promo'
    id = Column(Integer, primary_key=True)
    end_year = Column(String)
    alumnis = relationship("Alumni", back_populates="promo")
    def __repr__(self):
        return  str(self.end_year)


# Classe Company
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