#!/usr/bin/env bash

source venv/bin/activate
export FLASK_APP="awesomeapp/api.py"
export FLASK_DEBUG="true"
flask run
