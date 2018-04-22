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

###Listing and Searching For Company Records

This is the most simple one as it only requires you to input a link.

To use this function with curl, run the following in a terminal:

```
curl -i http://localhost:5000/api/companies
```

In Postman, there should be a dropdown button near the upper left. That's where we will be selecting our requests. For this function, pick GET and in the text field next to it enter the following then hit send:

```
http://localhost:5000/api/companies
```

![Displaying all companies with Postman](images/get_companies.png)

To see information about specific companies, you should just use the same URL in either method, but add the name of the company you want to see at the end:

```
http://localhost:5000/api/companies/COMPANY_NAME_GOES_HERE
```

You can also search for companies by using this URL (again this link will work for both curl and Postman):

```
http://localhost:5000/api/companies/search?q=SEARCH_GOES_HERE
```

This search will list all companies whose names contain the search query you entered.

### Adding Companies

To add companies, we'll be using a POST request. The link we'll be using however, is still going to be the one to see all companies. For this, a JSON will need to be sent to specify the details of the company to be added. At the very least a name will need to be specified. The other fields are employees, email, location, and industry. As an example, we could have something that looks like this: 

```json
{
  "name": "Siomai Gosh",
  "employees": 59,
  "location": "Metro Manila"
}
```

In curl, you would need to run a command like this:

```shell
curl -X POST -H "Content-Type: application/json" -d 'JSON_GOES_HERE' http://localhost:5000/api/companies
```

An important note when using curl is that the JSON should be enclosed in single quotes, and if properties and values need to be in quotes, they should be double quotes. This works on Linux, but on windows this may not run correctly. To remedy this, surround the JSON with double quotes instead, and instead of using a single double quote inside the JSON, use three. For example it might look like this on Windows:

```
'{
  """name""": """Siomai Gosh""",
  """employees""": 59,
  """location""": """Metro Manila"""
}'
```



```json
{
  "name": "Siomai Gosh",
  "employees": 59,
  "location": "Metro Manila"
}
```



```json
{
  "name": "Siomai Gosh",
  "employees": 59,
  "location": "Metro Manila"
}
```



## Built With

* [Flask][http://flask.pocoo.org]- The framework used
* [SQLAlchemy][https://www.sqlalchemy.org/] - SQL Toolkit and ORM

## Author

* **Anton Nikolai Tangan**
