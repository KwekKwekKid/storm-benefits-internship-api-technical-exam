from flask import Flask, jsonify, request, abort
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)

engine = create_engine(
    "mysql://root@localhost/company_db", convert_unicode = True)
    
Session = sessionmaker(bind = engine)
session = Session()
Base = declarative_base()

BASE_DIR = "/api/companies"


class Company(Base):
    __tablename__ = "Company"

    name = Column(String(100), primary_key = True, unique = True)
    employees = Column(Integer)
    location = Column(String(100))
    email = Column(String(100))
    industry = Column(String(100))

    def __init__(self, name=None, employees=None):
        self.name = name
        self.employees = employees

    def __repr__(self):
        return "COMPANY: {}".format(self.name)
        
    def to_json(self):
        return dict(
            name = self.name, 
            employees = self.employees,
            location = self.location,
            email = self.email,
            industry = self.industry)


@app.route("/")
def index():
    return Company.__repr__


@app.route(BASE_DIR, methods = ["GET"])
def get_companies():
    query = session.query(Company).all()
    return jsonify({"Companies": query})


@app.route(BASE_DIR + "/<company_name>", methods = ["GET"])
def get_company(company_name):
    query = session.query(Company).filter_by(name = company_name)
    return jsonify({"Companies": query.column_descriptions})


@app.route(BASE_DIR, methods = ["POST"])
def add_company():
    if not request.get_json() or "name" not in request.get_json():
        abort(400)
    company_name = request.get_json().get("name")
    company = Company(company_name, 500)
    session.add(company)
    session.commit()
    
    return jsonify({"Company": company.to_json()})


@app.route(BASE_DIR + "/<company_name>", methods = ["PUT"])
def update_company(company_name):
    if(not request.get_json()): 
        abort(400)
    if("name" in request.get_json() and type(request.get_json()["name"]) != str):
        abort(400)
    if("employees" in request.get_json() and type(request.get_json()["employees"]) != int):
        abort(400)
    if("location" in request.get_json() and type(request.get_json()["location"]) != str):
        abort(400)
    if("email" in request.get_json() and type(request.get_json()["email"]) is not str):
        abort(400)
    if("industry" in request.get_json() and type(request.get_json()["industry"]) is not str):
        abort(400)

    query = session.query(Company).filter_by(name = company_name)
    query.update(request.get_json())
    session.commit()
    #TODO: Fix JSON return, place check for when property is not in model
    return ""


@app.route(BASE_DIR + "/<company_name>", methods = ["DELETE"])
def remove_company(company_name):
    query = session.query(Company).filter_by(name = company_name)
    query.delete()
    session.commit()
    #TODO: Fix JSON return
    return jsonify(Company = query.all())


if(__name__ == "__main__"):
    Base.metadata.create_all(engine)
    app.run()
    session.close()
