# BMS
Parsing and display service for a battery module system

<img width="556" alt="screen shot 2018-10-21 at 5 36 00 pm" src="https://user-images.githubusercontent.com/2002882/47274370-6f3eea80-d559-11e8-8829-38395631c17e.png">
<img width="1280" alt="screen shot 2018-10-21 at 5 40 21 pm" src="https://user-images.githubusercontent.com/2002882/47274371-6fd78100-d559-11e8-9606-0524e1225506.png">
<img width="1223" alt="screen shot 2018-10-21 at 5 40 33 pm" src="https://user-images.githubusercontent.com/2002882/47274374-70701780-d559-11e8-9a13-b627d4c46f0a.png">

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
