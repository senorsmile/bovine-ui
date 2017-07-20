#!/usr/bin/env bash
[[ -d ./venv/ ]] || {
  virtualenv venv/
  source ./venv/bin/activate
  pip install -U setuptools
  pip install -U pip
  pip install -r requirements.txt
  deactivate
}


source ./venv/bin/activate
pip install -r requirements.txt

#python app.py
export FLASK_APP=app.py
export FLASK_DEBUG=1
flask run -p 5001
