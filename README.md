# flask-suade

This repository contains the Flask application for the Suade interview for candidate Ruben Perez.

This Flask application implements a Report generator API. It allows inventory reports to be generated in PDF and XML
format.

## Requirements

This project has been tested with Python 3.7 on Ubuntu 19.10.

Dependencies:

- flask
- flask_sqlalchemy
- flask_weasyprint
- psycopg2
- PyPDF2 (for the tests)

## Running the application

To run this application, clone the repository, cd to the
cloned directory, and run:

```
$ export FLASK_APP=suade.py
$ flask run
```

## Endpoints

The API defines the following endpoints:

- `/reports/pdf/<report_id>`: generates a report in PDF format.
- `/reports/xml/<report_id>`: generates a report in XML format.

Both endpoints return HTTP 404 if the report_id does not 
identify a valid report.

## Running the tests

To be able to run the tests, you need a PostgreSQL server
running in localhost, with a database called "suade".

Given this, run:
```
python3 PYTHONPATH=$(pwd) app/tests/test_api.py
```
