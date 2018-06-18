# BMS
Parsing and display service for a battery module system

## Getting started
1. Clone this repo
2. Install Python 3, PostgreSQL and pipenv
3. Run `pipenv install` to install dependencies
4. Create a PostgreSQL database, user, and password for the application
5. Copy .env.example to .env and enter the database details

## Start the log parser service
Run `start_parser.sh`

## Start the web server
Run `start_server.sh`

## Digging deeper
Start the django console by running `pipenv run python manage.py shell`
