# Audition For Storm API Dev Internship

This is just an API for managing a list of companies.

You can view all company records or specific ones (either through search or using specific names). 
You can also add new company records, delete existing records or update them.

## Setting Up

Before running this project, there may be a few things that will need to be installed first.

### Prerequisites

[Python][https://www.python.org/downloads/]- To run the code

[MySQL][https://www.mysql.com/downloads/] - For the database

Once those are installed, you will then need to install the python libraries used. Open a terminal and run the following command:

```shell
pip install -r requirements.txt
```

The requirements.txt file from the repository should be in the same location you will be running this command in. If however, pip was unrecognized as a command, try the following instead:

```shell
python -m pip install -r requirements.txt
```

Another thing you would have to do is open up MySQL to create a new database. Once it's opened, enter the following command to have the database that will be used by the API:

```mysql
CREATE DATABASE company_db
```

## Running the API

Once the prerequisites have been properly installed, you will be able to run [Flask][http://flask.pocoo.org], the framework used to make this API.

Navigate to the directory where the app.py file is located, and run the following command:

```
python app.py
```

If successful, you should see a message similar to the following:

```
Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

That means you will be able to navigate to a web browser and open the URL seen in the message. Instead of "127.0.0.1" however, you should instead type localhost. Now to get to the actual API, you will need the following link:

```
http://localhost:5000/api/companies
```

This URL will display all the companies present in the database.

## Testing the API

Only using a web browser however, will only let you view things. To be able to use all the API's features we will need to use something else. In this I will explain two ways of testing out the API's functionality. By using [curl][https://curl.haxx.se/download.html] or [Postman][https://www.getpostman.com/apps]. If on a Linux system, curl should already be available to you, if not however, you will need to download it.

In the following sections I will list each function of the API, followed by how to use that function on both curl and Postman.

## Built With

* [Flask][http://flask.pocoo.org]- The framework used
* [SQLAlchemy][https://www.sqlalchemy.org/] - SQL Toolkit and ORM

## Author

* **Anton Nikolai Tangan**
