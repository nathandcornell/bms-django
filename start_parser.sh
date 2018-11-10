#!/bin/bash
SCRIPT_PATH="$(dirname "$BASH_SOURCE")"
PIPENV=$( which pipenv )

cd "$SCRIPT_PATH"
"$PIPENV" run python manage.py runscript parse_messages
