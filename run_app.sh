#!/usr/bin/env bash
#[[ -d ./venv/ ]] || {
#  virtualenv venv/
#  source ./venv/bin/activate
#  pip install -U setuptools
#  pip install -U pip
#  pip install -r requirements.txt
#  deactivate
#}
#
#
#source ./venv/bin/activate
#pip install -r requirements.txt

# pipenv
which pipenv || {
  echo "Must pip install pipenv in order to run this.  Exiting."
  exit 1
}


#python app.py
export FLASK_APP=app.py
export FLASK_DEBUG=1
pipenv run flask run -p 5001
