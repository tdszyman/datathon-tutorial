# Data2App Tutorial

Melbourne Datathon 2018  
Presented by ANZ  
Terrence.Szymanski@anz.com

## Quickstart

Before you start, you should have Python (3.6 or greater) installed, as well as virtualenv (`pip install virtualenv`).
Clone the repository:

    git clone git@github.com:tdszyman/datathon-tutorial.git
    
Then, run the scripts to setup your Python environment (which creates a virtualenv environment and installs some 
dependencies), then run the pipeline, and then run the app.

Windows:

    setup.bat
    python pipeline.py
    run.bat

Mac / Linux:

    ./setup.sh
    python pipeline.py
    ./run.sh
    
You should then be able to view the app at <http://localhost:5000>.


## Running the Dockerfile locally

You can also run the app by building and running the Dockerfile locally:

    docker build -t datathon .
    docker run -p 5000:5000 datathon

## Deploying to Elastic Beanstalk

It is also possible to deploy this app to AWS Elastic Beanstalk, using the configuration stored in the 
`.elasticbeanstalk` directory. You will need to have an AWS account and install the EB command line utilities. These 
resources are helpful to get started:

* https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/docker-singlecontainer-deploy.html#docker-singlecontainer-pythonsample
* https://github.com/aws-samples/eb-py-flask-signup/tree/docker

You can run these commands to deploy the app:

    eb init
    eb create dev-env
