# Data2App Tutorial

Melbourne Datathon 2018  
Presented by ANZ  
Terrence.Szymanski@anz.com

## Quickstart

Download and install dependencies:

    git clone git@github.com:tdszyman/datathon-tutorial.git
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    
Run the pipeline to download the data and build the database:

    python pipeline.py

Run the webserver:

    ./run.sh
    
You should then be able to view the app at <http://localhost:5000>.

## Contents
    
`$ tree -I "data|venv|__pycache__" .`

    .
    ├── Dockerfile
    ├── Readme.md
    ├── awesomeapp
    │   ├── __init__.py
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
    ├── pipeline.py
    ├── requirements.txt
    └── run.sh

