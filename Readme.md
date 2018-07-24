# Data2App Tutorial

Melbourne Datathon 2018  
Presented by ANZ  
Terrence.Szymanski@anz.com

## Quickstart

    git clone git@github.com:tdszyman/datathon-tutorial.git
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ./run.sh

## Contents

    .
    ├── Dockerfile
    ├── Readme.md
    ├── awesomeapp
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-36.pyc
    │   │   └── api.cpython-36.pyc
    │   ├── api.py
    │   ├── static
    │   │   ├── css
    │   │   │   ├── awesomeapp.css
    │   │   │   └── bootstrap.css
    │   │   ├── img
    │   │   │   └── datathonLogoPB.png
    │   │   └── js
    │   │       ├── awesomeapp.js
    │   │       ├── bootstrap.js
    │   │       ├── jquery.js
    │   │       └── popper.js
    │   └── templates
    │       ├── base.html
    │       └── index.html
    ├── data
    │   └── datafile.csv
    ├── pipeline.py
    ├── requirements.txt
    └── run.sh