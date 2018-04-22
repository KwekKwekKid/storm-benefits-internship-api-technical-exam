from flask import Flask, jsonify, request, abort
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)

#TODO: Make it so that it creates a database if it doesn't exist'
engine = create_engine(
    "mysql://root@localhost/company_db", convert_unicode=True)

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

#made a constant so that it'd be easier to change the directory in the future.
BASE_DIR = "/api/companies"


#Stores a row in the database.
#considered making a models.py file, but didn't since it'd just have one class.
class Company(Base):
    __tablename__ = "company"

    name = Column(String(255), primary_key=True, unique=True)
    employees = Column(Integer)
    location = Column(String(255))
    email = Column(String(255))
    industry = Column(String(255))

    def __init__(self, name, employees, location, email, industry):
        self.name = name
        self.employees = employees
        self.location = location
        self.email = email
        self.industry = industry

    def to_dict(self):
        return dict(
            name=self.name, employees=self.employees, location=self.location,
            email=self.email, industry=self.industry)


@app.route("/")
def index():
    return Company.__repr__


@app.route(BASE_DIR, methods=["GET"])
def get_companies():
    companies = session.query(Company).all()
    return jsonify(
        {"companies": [company.to_dict() for company in companies]})


@app.route(BASE_DIR + "/<company_name>", method=["GET"])
def get_company(company_name):
    company = session.query(Company).filter_by(name=company_name).one()
    return jsonify({"company": company.to_dict()})


@app.route(BASE_DIR, method =["POST"])
def add_company():
    if not request.get_json() or "name" not in request.get_json():
        abort(400)
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
    company_name = request.get_json().get("name")
    company_employees = request.get_json().get("employees", 0)
    company_location = request.get_json().get("location")
    company_email = request.get_json().get("email")
    company_industry = request.get_json().get("industry")

    company = Company(
        company_name,
        company_employees,
        company_location,
        company_email,
        company_industry)

    session.add(company)
    session.commit()

    return jsonify({"company": company.to_dict()}), 201


@app.route(BASE_DIR + "/<company_name>", methods=["PUT"])
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

    company = session.query(Company).filter_by(name=company_name).ome()
    company.update(request.get_json())
    session.commit()

    return jsonify({"company": company.to_dict()})


@app.route(BASE_DIR + "/<company_name>", methods=["DELETE"])
def remove_company(company_name):
    company = session.query(Company).filter_by(name=company_name).one()
    company.delete()
    session.commit()

    return jsonify({"result": True})


if(__name__ == "__main__"):
    Base.metadata.create_all(engine)
    app.run()
    session.close()
