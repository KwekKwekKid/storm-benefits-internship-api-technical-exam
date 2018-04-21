from flask import Flask, jsonify, request

app = Flask(__name__)

BASE_DIR = "/api/companies"


@app.route("/")
def index():
    return "test"


@app.route(BASE_DIR, methods = ["GET"])
def get_companies():
    return ""


@app.route(BASE_DIR + "/<company_name>", methods = ["GET"])
def get_company(company_name):
    return ""


@app.route(BASE_DIR, methods = ["POST"])
def add_company():
    return ""


@app.route(BASE_DIR + "/<company_name>", methods = ["PUT"])
def update_company(company_name):
    return ""


@app.route(BASE_DIR + "/<company_name>", methods = ["DELETE"])
def remove_company(company_name):
	return ""


if(__name__ == "__main__"):
    app.run()
