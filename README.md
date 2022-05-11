# Open Banking Deep Backend

This project houses the deep backend for NUS FinTech Openbanking project. It consists of PostgreSQL db to store news and fx data and exposes some APIs for other components of the project to interact with the database. This project is developed using Python, Flask, PostgreSQL and Heroku.

## Setting up the project locally
The set up was done by following this tutorial: 
https://medium.com/@dushan14/create-a-web-application-with-python-flask-postgresql-and-deploy-on-heroku-243d548335cc

### Requirements
1. PostgreSQL installed in your system
2. Heroku CLI installed in your system
3. virtualenv installed in your system

### Set up
1. `source env/Scripts/activate`
2. export the variables in `.env` file by copy pasting the export commands into terminal and running them
3. `py app.py`

## Viewing content in remote heroku db
1. `heroku pg:psql --app openbanking-application`

# Exposed APIs

## Adding forex data
