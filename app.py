from flask import Flask, jsonify, request, abort, redirect
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)

#TODO: Make it so that it creates a database if it doesn't exist'

#This assumes your mysql doesn't have a password.
#If the app doesn't work, try replacing "root" with username:password.
engine = create_engine(
    "mysql://root@localhost/company_db", convert_unicode=True)

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

#Made a constant so that it'd be easier to change the directory in the future.
BASE_DIR = "/api/companies"


#Stores a row in the database.
#Considered making a models.py file, but didn't since it'd just have one class.
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

    #Made this so it would be easier to jsonify instances of Company.
    def to_dict(self):
        return dict(
            name=self.name, employees=self.employees, location=self.location,
            email=self.email, industry=self.industry)


@app.route("/")
@app.route("/index")
def index():
    return redirect("http://localhost:5000" + BASE_DIR, code=302)


@app.route(BASE_DIR, methods=["GET"])
def get_companies():
    companies = session.query(Company).all()
    return jsonify(
        {"companies": [company.to_dict() for company in companies]})


@app.route(BASE_DIR + "/<company_name>", methods=["GET"])
def get_company(company_name):
    company = session.query(Company).filter_by(name=company_name).one()
    return jsonify({"company": company.to_dict()})


@app.route(BASE_DIR, methods=["POST"])
def add_company():
    if not request.get_json() or "name" not in request.get_json():
        abort(400)

    if("name" in request.get_json()
            and type(request.get_json()["name"]) != str):
        abort(400)

    if("employees" in request.get_json()
            and type(request.get_json()["employees"]) != int):
        abort(400)

    if("location" in request.get_json()
            and type(request.get_json()["location"]) != str):
        abort(400)

    if("email" in request.get_json()
            and type(request.get_json()["email"]) != str):
        abort(400)

    if("industry" in request.get_json()
            and type(request.get_json()["industry"]) != str):
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

    if("name" in request.get_json()
            and type(request.get_json()["name"]) != str):
        abort(400)

    if("employees" in request.get_json()
            and type(request.get_json()["employees"]) != int):
        abort(400)

    if("location" in request.get_json()
            and type(request.get_json()["location"]) != str):
        abort(400)

    if("email" in request.get_json()
            and type(request.get_json()["email"]) != str):
        abort(400)

    if("industry" in request.get_json()
            and type(request.get_json()["industry"]) != str):
        abort(400)

    company = session.query(Company).filter_by(name=company_name)
    company.update(request.get_json())
    company = company.one()
    session.commit()

    return jsonify({"company": company.to_dict()})


@app.route(BASE_DIR + "/<company_name>", methods=["DELETE"])
def remove_company(company_name):
    company = session.query(Company).filter_by(name=company_name)
    company.delete()
    session.commit()

    return jsonify({"result": True})


if(__name__ == "__main__"):
    Base.metadata.create_all(engine)  # creates the required tables
    app.run()
    session.close()
