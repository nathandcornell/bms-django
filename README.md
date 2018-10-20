# BMS
Parsing and display service for a battery module system

## Getting started
1. Clone this repo
2. Install Python 3, PostgreSQL and pipenv
3. Run `pipenv install` to install dependencies
4. Create a PostgreSQL database, user, and password for the application
5. Copy .env.example to .env and enter the database details
6. Run `pipenv run python manage.py migrate` to set up the database
7. Run `npm install && ./node_modules/.bin/webpack --config webpack.config.js` to install and compile JavaScript assets

## Start the log parser service
Run `start_parser.sh`

## Start the web server
Run `start_server.sh`

## Digging deeper
Start the django console by running `pipenv run python manage.py shell`
